# The `.braid` Specification — v0

**Status:** Draft v0 — 2026-10-30
**Implementation:** `braid/` (Python reference simulator)
**Examples:** `examples/`

A `.braid` file describes one braiding job completely enough that (a) the
simulator can predict the resulting braid's geometry and first-order
mechanics, and (b) a braiding machine can be scheduled from it: carrier
count, track, materials, core, and the take-up profile. It is the file
format at the centre of the design-to-braid pipeline — the open counterpart
to the proprietary "slicer" step in closed tissue-braiding platforms.

## Format

JSON (`.braid.json`). JSON was chosen for v0 over YAML for one reason: the
reference implementation must run on the Python standard library alone.
The schema is field-for-field identical if a YAML serialisation is added
later.

## Fields

| Field | Type | Required | Meaning |
|---|---|---|---|
| `spec_version` | int | yes | Format version. Currently `0`. |
| `name` | string | yes | Human-readable job name. |
| `carriers` | int | yes | Total carrier count. Must be even; half run clockwise, half counter-clockwise in a standard biaxial maypole braid. |
| `yarn` | object | yes | See below. |
| `yarn.material` | string | yes | Free text, e.g. `"PET"`, `"UHMWPE"`, `"silicone-coated fibreglass"`. |
| `yarn.width_mm` | number | yes | Effective yarn width (flat width for tapes/ribbons, diameter for round yarns) in millimetres. Drives cover factor. |
| `yarn.linear_density_tex` | number | no | Yarn size in tex (g/km). Used for mass estimates. |
| `yarn.modulus_gpa` | number | no | Young's modulus of the yarn material. Used only for the first-order stiffness estimate. |
| `core` | object | yes | The mandrel / skeletal core the braid is laid over. |
| `core.diameter_mm` | number | yes | Core outside diameter in millimetres. v0 assumes a circular cross-section (see Limitations). |
| `target` | object | yes | What the job is trying to produce. |
| `target.braid_angle_deg` | number | yes | Desired braid angle in degrees, measured between the yarn and the braid (core) axis. Valid range (0, 90); practical maypole range ~20–70. |
| `target.length_mm` | number | yes | Finished braid length in millimetres. |
| `machine` | object | no | Machine-side parameters, when known. |
| `machine.carrier_rpm` | number | no | Carrier rotation rate about the main axis, rev/min. Together with take-up speed this *determines* the as-built braid angle. |
| `machine.takeup_mm_per_min` | number | no | Take-up (axial draw-off) speed. Together with carrier rpm this determines the as-built braid angle. |

## Derived quantities (simulator outputs)

Given the spec, the reference simulator computes:

- **As-built braid angle** — if machine parameters are present,
  `tan θ = (carrier surface speed at the core) / (take-up speed)`, where
  carrier surface speed = carrier rpm × π × core diameter. If machine
  parameters are absent, the target angle is used.
- **Cover factor** — fraction of the core surface covered by yarn,
  from the standard two-system overlap model:
  per-direction coverage `f = (N/2 · w) / (π · D · cos θ)` (capped at 1),
  total `K = 1 − (1 − f)²`. See Limitations.
- **Yarn consumption** — metres of yarn per metre of finished braid
  = `1 / cos θ` per yarn, × carrier count for the whole braid.
- **Picks per unit length** — yarn crossovers per millimetre along the
  axis, proportional to `tan θ / (π · D)` per carrier pair.
- **Braid mass** — when `linear_density_tex` is present:
  yarn length × tex for all carriers.
- **First-order axial stiffness index** — a normalised estimate scaling
  with `cos⁴ θ` (the classical angle-ply transform). A *comparison*
  index between specs, not an engineering modulus. See Limitations.
- **McKibben geometry helpers** — for actuator work: given inextensible
  yarn length and turn count, length and diameter of a braided sleeve as
  functions of its current braid angle (`L = b·cos θ`,
  `D = b·sin θ / (n·π)`), from which contraction follows.

## Validation rules (enforced by the reference loader)

- `spec_version` must be `0`.
- `carriers` must be a positive even integer ≥ 4.
- All dimensions must be positive; `braid_angle_deg` must be in (5, 85)
  for v0 — outside that range the geometry model is not meaningful.
- Unknown top-level fields are rejected in v0. Strictness now prevents
  silent divergence between implementations later.

## Limitations — read before trusting a number

v0 is a geometry model, not a physics engine. Known gaps, in the order we
intend to close them:

1. **Circular cores only.** Real skeletal cores are not round. An
   arbitrary-cross-section model (perimeter-based, then full surface
   mapping) is the Phase 0 follow-on.
2. **Cover factor is the ideal-helix model.** It ignores yarn flattening,
   nesting between layers, and friction-driven angle drift at the fell
   point. Treat it as ±10–15% until the Phase 0 physical validation
   (three hand-braided samples) says otherwise.
3. **Stiffness is an index, not a prediction.** Real braided-sleeve
   stiffness depends on inter-yarn friction and jamming at high cover
   factors, which v0 does not model. The Phase 2 angle-sweep dataset
   exists precisely to replace this index with measured curves.
4. **No tension model.** Carrier tension consistency is the known #1
   quality variable in DIY braiding; v0 assumes it away. A tension field
   (and per-carrier settings in the spec) is planned for v1.
5. **Single layer, biaxial only.** Triaxial (axial inlay) yarns and
   multi-layer braids are v1+.

## Versioning

Breaking field changes bump `spec_version`. The loader must refuse a
version it does not implement rather than guess.
