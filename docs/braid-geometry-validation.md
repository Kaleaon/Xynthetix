# Braid Geometry Validation — Simulator vs Published Relations

**Date:** 2026-11-23
**Scope:** `braid/geometry.py` (reference simulator, spec v0) checked
quantity-by-quantity against published maypole-braid geometry relations
from the textile/composites literature, the cable-shield standards
literature, and the McKibben-muscle literature. Worked numbers for all
three files in `examples/`, plus carrier-count, take-up, and angle
sweeps. All simulator numbers below were produced by running the
simulator and by independent re-implementation of the published
formulas in a scratch script (not by reading the code and assuming).

**Verdict up front:** the simulator's core formulas are *algebraically
identical* to the standard published relations for braid angle, cover
factor, yarn consumption, and the McKibben helper. There is no wrong
sign, no swapped sin/cos, and no missing factor of 2 or π anywhere we
looked. The real findings are about *conventions and silent limits*,
not wrong math:

1. **Diameter convention (main flag).** Every simulator quantity is
   evaluated at the bare core diameter `D`. The cable-shield standards
   evaluate the same relations at the diameter *over the braid build*,
   `D + 2d`, and a yarn-centreline argument gives `D + t` (t = yarn
   thickness). On the repo's own examples this moves the machine angle
   by up to **+5.2°**, picks by **−9 % to −25 %**, and cover factor by
   **−0.04 to −0.10 absolute**. The simulator has no yarn-thickness
   field, so it cannot express the correction.
2. **Silent jamming cap.** When the per-direction coverage `f`
   exceeds 1 the simulator caps it at 1 and reports a perfect braid.
   `f > 1` is the published *jamming* condition — the yarns cannot all
   lie in one layer at that angle on that core. The cap is more
   sensible than the literal published formula (which turns back down
   for `f > 1`, see §3), but the infeasibility must be reported, not
   hidden.
3. **No diameter prediction for overbraids.** The main simulator takes
   diameter as an input and outputs none — no outer diameter
   (`D + 2t`), no free-braid diameter. Only the McKibben helper
   predicts a diameter, and it matches Chou & Hannaford exactly.
4. **Known physical bias (inherited from the published ideal model).**
   In Rawal et al.'s own experimental check of these same formulas,
   predicted angles ran **+1.8 % to +14.7 % high** and predicted cover
   factors **−13.6 % to −25 % low** against measured braids. The
   simulator will inherit that bias against physical samples; the
   spec's ±10–15 % warning is the right order of magnitude but does
   not state the direction.

---

## 1. What the simulator actually computes

Extracted from `braid/geometry.py` and `docs/braid-spec.md`
(θ = braid angle **from the braid axis**, `N` = total carriers,
`D` = core diameter, `w` = yarn width):

| Quantity | Simulator formula |
|---|---|
| Machine angle | `tan θ = rpm · π · D / take-up` (`angle_from_machine`) |
| Per-direction cover | spacing `= (π D / (N/2)) · cos θ`; `f = w / spacing = N w / (2 π D cos θ)`, capped at 1 |
| Total cover factor | `K = 1 − (1 − f)²` |
| Yarn consumption | `1 / cos θ` m of yarn per metre of braid, per carrier; total `× N × length` |
| Picks per mm | `(N/2) · tan θ / (π D)` |
| Braid mass | total yarn length × tex / 1000 |
| Axial stiffness index | `cos⁴ θ` (labelled comparison-only in code and spec) |
| McKibben helper | `L = b · cos θ`, `D = b · sin θ / (n · π)` (`b` = yarn length, `n` = turns) |

Note what is **not** in `BraidResult`: any diameter. Diameter enters
only as the input `core.diameter_mm`.

## 2. Published relations used

Every relation below is cited to a source that was opened and read
for this check.

**(P1) Machine angle — Rawal, Potluri & Steele (2005).**
`θ = tan⁻¹(ω r / v)`, with ω the bobbin angular speed, r the mandrel
radius, v the take-up speed. With ω = 2π·rpm and r = D/2 this is
`tan θ = π D · rpm / v` — the simulator's formula, term for term.
The same relation appears as `tan(θ) = π · Dm · ωc / Vm` in US Patent
8,960,065, and as `braidAngle = atan(π × mandrelDiameter × carrierSpeed
/ takeUpSpeed)` in the Textile School braiding calculator.
Sources:
https://sagecnp.cnpereading.com/paragraph/download/?doi=10.1177/1528083705057574
· https://patents.justia.com/patent/8960065
· https://www.textileschool.com/calculators/braiding-angle/

**(P2) Cover factor — Rawal/Potluri, restated in the composites
literature.** `CF = 1 − (1 − Wy·Nc / (4 π R cos α))²`, R = mandrel
radius. With R = D/2 the inner term is `N w / (2 π D cos θ)` — exactly
the simulator's `f`. The same form appears in US Patent 9,217,538
(`cf = 1 − (1 − w n / (4 π R cos θ))²`) and in the CANCOM 2026 unit-cell
treatment following Potluri et al.
Sources:
https://www.springerprofessional.de/numerical-and-experimental-investigation-of-the-hydrostatic-perf/11695652
· https://patents.justia.com/patent/9217538
· https://cacsma.ca/wp-content/uploads/2026/07/CANCOM2026_paper_137-1.pdf

**(P3) Cable-shield standards — ANSI/SCTE 51, A-A-59569, MIL-DTL-13777.**
These define, with α measured from the cable axis, D = diameter
*under* the braid, d = strand diameter, C = carriers, P = picks per
unit length, Nₑ = ends (strands) per carrier:

- `α = tan⁻¹[ 2π (D + 2d) · P / C ]`, i.e. **`P = C · tan α / (2π (D + 2d))`**
- `F = Nₑ · P · d / sin α`; coverage `K = (2F − F²) × 100 %`
  (A-A-59569 writes the same F as `N P W / (C sin A)` with N = *total*
  ends, so N/C = Nₑ — the two forms are the same formula.)

Sources:
https://wagtail-prod-storage.s3.amazonaws.com/documents/ANSI_SCTE_51_2018_R2024.pdf
· https://weaponssupportapps.dla.mil/Downloads/MilSpec/Docs/A-A-59569/aa59569.pdf
· https://quicksearch.dla.mil/Transient/B180DC7036D04F6A98780D4BE6D4BD17.pdf
· https://www.digikey.com/Site/Global/Layouts/DownloadPdf.ashx?pdfUrl=ECA84DAD2D7F4C94A8F2563BBDFB50D6

**(P4) Yarn consumption.** Textile School: yarn feed per carrier
`= take-up / cos θ` — i.e. yarn length per unit braid length
`= 1 / cos θ`, and total consumption `= carriers × feed × tex`
(scaled) — the simulator's consumption and mass formulas. The cable
literature's shield-weight formula `W = n·C·l / cos U` carries the
same `1 / cos` length factor.
Sources: https://www.textileschool.com/calculators/braiding-angle/
· https://www.digikey.com/Site/Global/Layouts/DownloadPdf.ashx?pdfUrl=ECA84DAD2D7F4C94A8F2563BBDFB50D6

**(P5) McKibben / free-braid diameter.** Chou & Hannaford's
inextensible-braid model, as restated in the fascicle-pack literature:
`L = b cos θ`, `D = b sin θ / (N π)`, hence the ratio forms
`L₂/L₁ = cos θ₂ / cos θ₁` and `D₂/D₁ = sin θ₂ / sin θ₁` (the same
ratios the Textile School extension calculator evaluates), and the
neutral (maximum-volume) angle at `tan²θ = 2`, θ = 54.7356°.
Sources: https://arxiv.org/pdf/2302.01455
· https://iris.polito.it/bitstream/11583/2673347/3/Numerical%20modelling%20and%20experimental%20validataion%20of%20a%20McKibben%20pneumatic%20muscle%20actuator_to%20publish.pdf
· https://www.textileschool.com/calculators/braid-extension-geometry/

**(P6) Measured-vs-predicted evidence — Rawal et al. (2005), Table 3.**
The same paper that publishes P1/P2 measured braids made on a
24-carrier maypole machine over a 20 mm cylinder and compared:
predicted angle error **+1.81 %, +8.28 %, +14.7 %** at take-up speeds
0.035 / 0.050 / 0.067 m/s (predicted always high — yarn interlacing
near the braid point), and predicted cover-factor error **−13.6 %,
−20.0 %, −25.0 %** (predicted low — low-twist yarns flatten and cover
more). Error grows with take-up speed (yarn slip).
Source: https://sagecnp.cnpereading.com/paragraph/download/?doi=10.1177/1528083705057574

**(P7) Crimp magnitude.** An ICCM-19 braid-topology study measured
crimp in finished braided composites at 0.17–0.34 % — the ideal-helix
yarn-length model (P4) misses a real but sub-percent length term in
that setting; angle and cover errors (P6) dominate.
Source: https://zenodo.org/records/15439036/files/NAW81578.pdf

**(P8) Worked industry cross-check.** A LIGO engineering note applies
the Alpha Wire form of P3 to a real braid (24 carriers, 5 ends/carrier,
12 picks/inch, 0.005 in wire) and obtains angle 26.7° and coverage
89 % from the formulas, with a derived DC resistance (12.7 mΩ/m)
matching measurement (13.4 mΩ/m) — evidence the P3 formula family is
the one industry actually builds to.
Source: https://dcc-llo.ligo.org/public/0001/T0900158/001/T0900158.pdf

## 3. Worked comparisons — the three examples

Simulator output (run 2026-11-23) vs the published relations evaluated
independently. "Rawal" = P1/P2 at the core diameter. "Standards" =
P3, i.e. the same algebra evaluated at the over-build diameter
`D + 2w` (using yarn width as the only thickness proxy the spec has).

### 3.1 `finger-tendon` — N = 8, D = 3 mm, w = 0.5 mm, θ = 35° (target)

| Quantity | Simulator | Published | Δ |
|---|---|---|---|
| Cover f / K | 0.259 / 0.451 | Rawal 0.259 / 0.451 | 0 (identical formula) |
| Cover K via standards route | — | 0.351 (at D + 2w = 4 mm) | −0.100 |
| Picks / mm | 0.297 | Standards 0.223 (at D + 2w) | −25.0 % |
| Yarn per m per carrier | 1.221 | 1/cos 35° = 1.221 (P4) | 0 |

### 3.2 `mckibben-sleeve` — N = 24, D = 20 mm, w = 1.5 mm, θ = 45° (target)

| Quantity | Simulator | Published | Δ |
|---|---|---|---|
| Cover f / K | 0.405 / 0.646 | Rawal 0.405 / 0.646 | 0 (identical formula) |
| Cover K via standards route | — | 0.581 (at D + 2w = 23 mm) | −0.066 |
| Picks / mm | 0.191 | Standards 0.166 (at D + 2w) | −13.0 % |
| Yarn per m per carrier | 1.414 | 1/cos 45° = 1.414 (P4) | 0 |

### 3.3 `tube-sleeve` — N = 16, D = 10 mm, w = 1.0 mm, machine 12 rpm / 377 mm·min⁻¹

| Quantity | Simulator | Published | Δ |
|---|---|---|---|
| Machine angle | 45.00° | Rawal P1 at D: 45.00°; at D + w: 47.73°; at D + 2w: 50.19° | 0 / +2.7° / +5.2° |
| Cover f / K | 0.360 / 0.591 | Rawal 0.360 / 0.591 | 0 (identical formula) |
| Cover K via standards route | — | 0.510 (at D + 2w = 12 mm) | −0.081 |
| Picks / mm | 0.255 | Standards 0.212 (at D + 2w) | −16.7 % |
| Yarn per m per carrier | 1.414 | 1/cos 45° = 1.414 (P4) | 0 |

**Reading of §3:** against the academic process model (Rawal/Potluri)
the simulator is *exact* — unsurprising, it implements that model.
Against the standards model the differences are entirely the diameter
at which the shared formulas are evaluated: the standards put the
yarn path on the outside of the braid build (`D + 2d`); a centreline
argument (yarn centre sits half a thickness above the core surface on
each side) puts it at `D + t`. The truth for a real braid lies between
`D + t` and `D + 2t` depending on nesting/flattening — but it is never
at bare `D`, which is where the simulator evaluates everything. The
error is worst exactly where Xynthetix cares most: small cores
(finger tendon: −25 % on picks).

## 4. Parameter sweeps

### 4.1 Carrier count (D = 10 mm, w = 1.0 mm, θ = 45°)

| N | Sim f | Sim K | Rawal f | Rawal K | Picks/mm sim | Picks/mm std |
|---|---|---|---|---|---|---|
| 8 | 0.180 | 0.328 | 0.180 | 0.328 | 0.127 | 0.106 |
| 12 | 0.270 | 0.467 | 0.270 | 0.467 | 0.191 | 0.159 |
| 16 | 0.360 | 0.591 | 0.360 | 0.591 | 0.255 | 0.212 |
| 24 | 0.540 | 0.789 | 0.540 | 0.789 | 0.382 | 0.318 |
| 32 | 0.720 | 0.922 | 0.720 | 0.922 | 0.509 | 0.424 |
| 48 | **1.000 (capped)** | **1.000** | 1.080 | 0.994* | 0.764 | 0.637 |
| 64 | **1.000 (capped)** | **1.000** | 1.441 | 0.806* | 1.019 | 0.849 |

\* For f > 1 the literal published expression `1 − (1 − f)²` *decreases*
again (it is a parabola peaking at f = 1) — a modelling artefact, not
physics. Physically f > 1 means the yarns jam: they flatten, nest, or
ride up into a second layer. Full cover first becomes geometrically
possible at `D_min = N·w / (2π cos θ)` (set f = 1 in P2; the CANCOM
unit-cell paper derives the same minimum-diameter condition). For the
N = 48 row, D_min = 10.8 mm > the 10 mm core — that spec cannot be
braided as a single layer at 45°, and the simulator currently reports
it as a perfect braid (K = 1.000) with no indication anything is wrong.

### 4.2 Take-up sweep (tube-sleeve machine: 12 rpm, D = 10 mm, N = 16, w = 1.0 mm)

| Take-up (mm/min) | Sim angle | Rawal at D | Rawal at D + 2w | K (sim) | Yarn/m | Picks/mm sim | Picks/mm std | Pitch (mm/rev) |
|---|---|---|---|---|---|---|---|---|
| 100 | 75.14° | 75.14° | 77.54° | 1.000 | 3.900 | 0.960 | 0.800 | 8.3 |
| 200 | 62.05° | 62.05° | 66.15° | 0.791 | 2.134 | 0.480 | 0.400 | 16.7 |
| 377 | 45.00° | 45.00° | 50.19° | 0.591 | 1.414 | 0.255 | 0.212 | 31.4 |
| 500 | 37.02° | 37.02° | 42.14° | 0.536 | 1.252 | 0.192 | 0.160 | 41.7 |
| 750 | 26.69° | 26.69° | 31.10° | 0.489 | 1.119 | 0.128 | 0.107 | 62.5 |
| 1000 | 20.66° | 20.66° | 24.34° | 0.470 | 1.069 | 0.096 | 0.080 | 83.3 |
| 1500 | 14.11° | 14.11° | 16.78° | 0.456 | 1.031 | 0.064 | 0.053 | 125.0 |

The angle formula itself is confirmed at every row (sim = Rawal at D,
to the digit). The diameter-convention gap (§3) is worth +2.4° to
+5.2° across the working range — larger than the entire physical
prediction error Rawal measured at low take-up (+1.8 %, ≈ +0.9° at
~50°). Pitch (take-up ÷ rpm) is not a simulator output; the standards
route to picks runs through it, and it is the quantity a machine
schedule actually needs.

### 4.3 Angle sweep (N = 16, D = 10 mm, w = 1.0 mm)

| θ | Sim f | Sim K | Rawal f | Rawal K | 1/cos θ | cos⁴ θ |
|---|---|---|---|---|---|---|
| 20° | 0.271 | 0.469 | 0.271 | 0.469 | 1.064 | 0.780 |
| 30° | 0.294 | 0.502 | 0.294 | 0.502 | 1.155 | 0.563 |
| 35° | 0.311 | 0.525 | 0.311 | 0.525 | 1.221 | 0.450 |
| 45° | 0.360 | 0.591 | 0.360 | 0.591 | 1.414 | 0.250 |
| 54.74° | 0.441 | 0.688 | 0.441 | 0.688 | 1.732 | 0.111 |
| 60° | 0.509 | 0.759 | 0.509 | 0.759 | 2.000 | 0.063 |
| 70° | 0.745 | 0.935 | 0.745 | 0.935 | 2.924 | 0.014 |

No divergence anywhere in the range the loader accepts (5–85°).

### 4.4 McKibben helper (sleeve from `mckibben-sleeve`: L₀ = 300 mm, D₀ = 20 mm at θ₀ = 45°, giving b = 424.3 mm, n = 4.775 turns)

| Move | Helper L (mm) | Helper D (mm) | L/L₀ vs cos-ratio (P5) | D/D₀ vs sin-ratio (P5) |
|---|---|---|---|---|
| 45° → 35° | 347.5 | 16.22 | 1.1585 vs 1.1585 | 0.8112 vs 0.8112 |
| 45° → 54.74° | 244.9 | 23.09 | 0.8165 vs 0.8165 | 1.1547 vs 1.1547 |
| 35° → 25° (b = 366.2, n = 3.343) | 331.9 | 14.74 | 1.1064 vs 1.1064 | 0.7368 vs 0.7368 |

The helper *is* the Chou & Hannaford model (P5), exactly, including
the contraction identity `1 − cos θ / cos θ₀` stated in its docstring.
The 45° → 54.74° row contracts 18.3 % and lands on the neutral angle —
consistent with P5's maximum-volume condition.

## 5. Discrepancies and recommendations

**No formula in `braid/geometry.py` disagrees with the published
relations it implements.** The following are the specific corrections
recommended (recommendations only — no code was changed in this run):

- **R1 — Evaluate geometry at a yarn-path diameter, not the bare core.**
  Add `yarn.thickness_mm` to the spec; compute a centreline diameter
  `D_c = D + thickness` and use `D_c` in `angle_from_machine`,
  `cover_factor`, and `picks_per_mm`; document that the standards
  bound is `D + 2·thickness`. Expected effect on today's examples:
  angle +2.7° (centreline) to +5.2° (standards bound) on tube-sleeve,
  picks −9 % to −25 %, cover −0.05 to −0.10. This is the single
  largest validated error source in the simulator — larger than the
  physical model error in P6 at moderate take-up speeds.
- **R2 — Report jamming instead of capping silently.** Return the
  uncapped `f`; when `f > 1`, flag the spec as jammed and report
  `D_min = N·w / (2π cos θ)`. Do *not* "fix" this by removing the cap
  and using the literal published `K` — for f > 1 that formula is
  non-monotonic and returns K < 1 for an over-full braid (§4.1).
- **R3 — Clarify "picks".** The simulator's value equals the industry
  pick count P in P3 — *same-direction* carrier crossings per unit
  length (A-A-59569's definition). The spec text "yarn crossovers per
  millimetre" invites a reader to count all crossover points, which
  is a different (larger) number. Rename or define explicitly.
- **R4 — Output a diameter.** Add braid outer diameter `D + 2t`
  (needs R1's thickness field) to `BraidResult`, and for free
  (mandrel-less) braids the P5 sin-ratio diameter change. Today a
  user asking the simulator "how thick is the finished braid?" gets
  no answer.
- **R5 — State the direction of physical bias.** Per P6, against
  physical braids this model family over-predicts angle (up to
  ~+15 % at high take-up) and under-predicts cover (up to ~−25 %,
  because real yarns flatten — which also means R1's correction and
  the flattening effect partly cancel on cover, and do not cancel on
  angle). The spec's Limitations §2 should carry the direction, not
  just "±10–15 %". Yarn consumption (P4) is a lower bound: crimp adds
  a sub-percent to few-percent term (P7) the model omits by design.
- **R6 — Guard the angle convention at boundaries.** Everything here
  measures θ from the axis, and the simulator does too — but part of
  the wider literature measures from the circumferential direction,
  and Rawal's own text also describes the helix angle as half the
  included angle between interlacing yarns (2θ). The spec already
  states "from the axis"; keep that sentence attached to any future
  import/export of angles (e.g. braidpy, machine schedules), where a
  silent convention flip would look like a 40° error at 45°.

## 6. Sources

13 sources opened/read for this validation:

1. Rawal, Potluri & Steele, *Geometrical Modeling of the Yarn Paths
   in Three-Dimensional Braided Structures*, J. Industrial Textiles
   35(2), 2005 — P1, P2, P6. https://sagecnp.cnpereading.com/paragraph/download/?doi=10.1177/1528083705057574
2. *Numerical and Experimental Investigation of the Hydrostatic
   Performance of Fibre Reinforced Tubes*, Springer — P1/P2 restated
   with π explicit. https://www.springerprofessional.de/numerical-and-experimental-investigation-of-the-hydrostatic-perf/11695652
3. US Patent 9,217,538 — cover-fraction formula (P2). https://patents.justia.com/patent/9217538
4. US Patent 8,960,065 — machine angle relation (P1). https://patents.justia.com/patent/8960065
5. CANCOM 2026, *Braiding of Composite Tubes using Pre-Impregnated
   Carbon Fibre/Thermoplastic Tapes* — Potluri unit cell, minimum
   diameter (P2, §4.1). https://cacsma.ca/wp-content/uploads/2026/07/CANCOM2026_paper_137-1.pdf
6. ANSI/SCTE 51 2018 (R2024), *Method for Determining Drop Cable
   Braid Coverage* — P3 with a fully worked example. https://wagtail-prod-storage.s3.amazonaws.com/documents/ANSI_SCTE_51_2018_R2024.pdf
7. A-A-59569D, *Braid, Wire … Tubular or Flat* (US DoD CID) — P3. https://weaponssupportapps.dla.mil/Downloads/MilSpec/Docs/A-A-59569/aa59569.pdf
8. MIL-DTL-13777L — P3 in military-cable form. https://quicksearch.dla.mil/Transient/B180DC7036D04F6A98780D4BE6D4BD17.pdf
9. Belden cable-design equations (via DigiKey) — P3/P4, mean-diameter
   definition. https://www.digikey.com/Site/Global/Layouts/DownloadPdf.ashx?pdfUrl=ECA84DAD2D7F4C94A8F2563BBDFB50D6
10. LIGO-T0900158-v1 — Alpha Wire P3 formulas applied and checked
    against a measured braid (P8). https://dcc-llo.ligo.org/public/0001/T0900158/001/T0900158.pdf
11. Textile School, *Braiding Carrier Speed & Braid Angle Calculator*
    — P1/P4. https://www.textileschool.com/calculators/braiding-angle/
12. Textile School, *Braid Extension, Diameter Change & the Neutral
    Angle* — P5 ratio forms. https://www.textileschool.com/calculators/braid-extension-geometry/
13. *Reconsidering Fascicles in Soft Pneumatic Actuator Packs*
    (arXiv:2302.01455) and Antonelli et al., *Numerical modelling and
    experimental validation of a McKibben pneumatic muscle actuator*
    — Chou & Hannaford model (P5). https://arxiv.org/pdf/2302.01455 ·
    https://iris.polito.it/bitstream/11583/2673347/3/Numerical%20modelling%20and%20experimental%20validataion%20of%20a%20McKibben%20pneumatic%20muscle%20actuator_to%20publish.pdf
14. ICCM-19 braid topology study — crimp measurement (P7). https://zenodo.org/records/15439036/files/NAW81578.pdf

*Method note: simulator values are from `python -m braid
examples/*.braid.json` plus direct calls to `braid.geometry`;
published values are from an independent scratch implementation of
P1–P5. No simulator code was modified.*
