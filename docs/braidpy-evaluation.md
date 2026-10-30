# braidpy — Evaluation and Adoption Decision

**Status:** Evaluated hands-on — 2026-10-30
**Package:** `braidpy` 0.3.0 on PyPI, by Baptiste Labat
**Licence:** MPL-2.0 (Mozilla Public License 2.0)
**Verdict:** Adopt as a Phase 1 dependency for machine modelling. Do not
fork. Do not depend on it in the v0 geometry simulator.

## What it is

braidpy is an alpha Python library that spans braid theory and practical
braid-making: kumihimo, marudai, sinnets — and, the part that matters here,
**horn-gear (maypole) braiding machines**. Per its PyPI documentation and
verified in the installed package:

- `braidpy.horn_gear` models a braiding machine: gears, carriers, tracks.
- `compute_tracks` / `simulation_period` derive the closed carrier paths;
  the paths decide which carriers can meet, which decides the braid.
- Threading is solved as a search (`load_carriers`): placements are tried
  and simulated, keeping the fullest arrangement that never collides.
- Visualisation and animation of machines; worked examples including
  `tubular_braid_8` (flat, tubular, soutache, diamond, and a Jacquard lace
  machine are also described).
- **Braid Studio** runs braidpy in the browser: describe a braid or a
  machine and see it laid and tightened in 3D.

Verified locally (2026-10-30): installed 0.3.0 in a clean venv;
`tubular_braid_8()` constructs a `BraidingMachine`;
`simulation_period` returns 8 for it. Dependencies: numpy, sympy,
networkx, dataclasses-json, math-braid.

## What it is not

- **Not machine control.** No carrier schedule export for a physical
  machine, no take-up profile, no firmware anything. It models and
  visualises; it does not drive hardware.
- **Not a mechanics model.** No braid-angle → stiffness/force prediction,
  no tendon model, no cover-factor engineering output of the kind the
  `.braid` simulator computes.
- **Not stable.** Alpha: the author states the API may change between
  versions. Pin the version; do not build load-bearing code on
  unreleased behaviour.

## Decision

1. **Our v0 simulator stays independent and standard-library-only**
   (`braid/` in this repo). Geometry prediction (angle, cover factor,
   consumption, McKibben relations) is our core and carries no third-party
   API risk.
2. **Phase 1 will use braidpy for what it is uniquely good at:** track
   layout, collision checking, and threading search for the desktop
   braider's horn-gear plate — the problems DIY builders currently solve
   by trial and error. Pin `braidpy==0.3.0` (or later, after a re-check)
   in the machine-design tooling, not in the core package.
3. **Bridge, don't fork.** The integration point is a translator from a
   `.braid` spec (carrier count, core, target angle) to a braidpy machine
   description, so a design validated geometrically in our simulator can
   be validated kinematically in braidpy before anyone prints a gear.
   Forking is unjustified while the upstream is active and the API is
   still moving; if we need changes, upstream contributions come first.
4. **Licence hygiene.** MPL-2.0 is file-level copyleft: using braidpy as
   a library dependency is fully compatible with this repo's MIT
   licensing of our own code. If braidpy source files are ever vendored
   or modified here, those files keep their MPL-2.0 headers and terms —
   they do not become MIT by being in this repo.

## Revisit when

- braidpy reaches a stable (non-alpha) release, or
- we need track geometries it cannot express (e.g. braiding over
  non-circular skeletal cores), or
- upstream goes unmaintained for >12 months.
