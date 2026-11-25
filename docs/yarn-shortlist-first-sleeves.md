# Yarn shortlist for first braided sleeves

**Date:** 2026-11-25 (Wed — braiding & woven tissue rotation)
**Status:** research note, sourced from manufacturer datasheets and
published fibre data. All numbers are typical values from the cited
sources, not product specifications; verify against the lot datasheet
before ordering.

## Why this shortlist exists

The first braided sleeves the programme makes will be learning pieces
(tube sleeves on a mandrel, then actuator sleeves), not flight hardware.
The yarn choice for those sleeves decides three things at once: how
much load a sleeve can carry, how the braid behaves on the machine
(friction, slippage, carrier tension), and how much a mistake costs.
This note compares the five fibre families named in the queue —
PET, nylon 6,6, UHMWPE, aramid — plus Vectran, which earned a place
during the research because it fixes the two failure modes that hurt
braided structures most (creep and flex fatigue). It ends with a
buying order: which yarn to braid first, and which to graduate to.

## Headline comparison

All values are fibre-level typical values. Braided-sleeve strength is
65–80% of the summed fibre strength (braiding geometry, friction and
splice losses — see the TMG Webbing grade guide, source 1).

| Property | PET (HT) | Nylon 6,6 (HT) | UHMWPE (Dyneema SK78) | Aramid (Kevlar 49) | Vectran HT (LCP) |
|---|---|---|---|---|---|
| Tenacity | 7–8 g/d (≈6.2–7.1 cN/dtex) | 6–7.3 g/d | 35.1 cN/dtex (39.8 g/d) | 23.6 g/d (208 cN/tex) | 23 cN/dtex (26 g/d) |
| Tensile strength | ~0.85–1.0 GPa | ~0.6–0.75 GPa | 3.2–3.4 GPa | 3.0 GPa | 3.2 GPa |
| Tensile modulus | 2–7.5 GPa (HMLS up to ~100 g/d) | 0.5–3 GPa | 109–132 GPa | 112 GPa | 75 GPa |
| Elongation at break | 13–18% | 20–40% | 3.5% | 2.4% | 3.8% |
| Density (g/cm³) | 1.38 | 1.14 | 0.97 | 1.44 | 1.40 |
| Melting / decomposition | melts 256 °C | melts ~255–265 °C | melts 147 °C | decomposes ~425–480 °C, no melt | melts 350 °C |
| Moisture regain | ~0.4% | 3–5% (up to 4.5%) | ~0% | 3.5% | <0.1% |
| Creep under sustained load | low | moderate | 0.006%/day at 30 °C, 300 MPa (SK78); SK75 is 0.02%/day | low | very low (manufacturer: no measurable creep to 50% of break; NASA testing found ~5× less than Kevlar) |
| Abrasion resistance | good (Martindale 25,000–60,000) | excellent (Martindale 40,000–100,000+) | excellent in rope service; low friction (μ ≈ 0.05 fibre–fibre, ~0.1 vs steel) | poor — fibrillates, cut-prone; needs a protective sheath | good; excellent flex fatigue |
| Flex / bending fatigue | good | good | excellent | poor — bending failure is compressive/shear-driven, strongly angle- and pretension-dependent | excellent |
| UV resistance | good | fair (yellows, retains 70–80% tenacity on long exposure) | excellent | poor | good |
| Friction (braiding behaviour) | moderate — grips, holds a braid | moderate — grips | very low — slips, knots slide, braid can walk | moderate, but fibrillation sheds material into the track | moderate |

Sources: PET tenacity/modulus and elongation from the high-tenacity
PET patent record and the GLYarn industrial-yarn guide (sources 6, 7);
nylon from the polyamide property summary and the Fiber-Line
selection guide (sources 8, 5); UHMWPE from the Avient/Dyneema
fact sheet and the SK75/SK78/SK99 grade guide (sources 1, 2);
aramid from the DuPont Kevlar technical guide (sources 3, 4);
Vectran from the Kuraray product brochure and datasheet (sources 9, 10);
abrasion/Martindale ranges from the GLYarn abrasion guide and the
workwear cut/abrasion review (sources 11, 12); UHMWPE friction
coefficients from the ultra-strong polyethylene design paper
(source 13); aramid bending fatigue from Cai et al. 2014 and the
Twaron rope damage study (sources 14, 15).

## Worked numbers: one yarn, one sleeve

Linear density is the honest way to compare yarns — a braid cares
about force per yarn and yarn diameter, not about brand names.
Diameter below assumes a solid round yarn at the stated density
(real multifilament yarns pack looser, so treat these as lower
bounds; measure the lot you buy).

| Yarn (linear density) | Break force | Solid-round diameter |
|---|---|---|
| Dyneema SK78, 1760 dtex | 35.1 cN/dtex × 1760 dtex ≈ **618 N** | 0.48 mm |
| Vectran HT, 1670 dtex (1500 den) | 23 cN/dtex × 1670 dtex ≈ **384 N** | 0.39 mm |
| Kevlar 49, 1270 dtex (1140 den) | 208 cN/tex × 127 tex ≈ **264 N** (matches DuPont's 264 N table value) | 0.38 mm |
| Nylon 6,6 HT, 1670 dtex | ≈6.2 cN/dtex × 1670 dtex ≈ **104 N** | 0.43 mm |
| PET HT, 1670 dtex | ≈6.5 cN/dtex × 1670 dtex ≈ **109 N** | 0.39 mm |

A 16-carrier maypole sleeve with one 1760 dtex SK78 yarn per carrier
carries 16 × 618 N ≈ 9,900 N of fibre strength on paper; at the
65–80% braid derating that is **≈6,400–7,900 N axial** before the
braid angle is even accounted for (angle reduces the axial component
further — see `docs/braid-geometry-validation.md`). The same sleeve
in PET HT carries ≈1,100–1,400 N. The gap is a factor of six, and it
is the whole reason the shortlist matters: PET is a learning yarn,
UHMWPE is a load yarn, and they are not interchangeable.

Note on the simulator: braid geometry relations should be evaluated
at mandrel diameter + yarn thickness (the `D + 2d` convention flagged
in `docs/braid-geometry-validation.md`). The diameters above are the
`d` to use — e.g. a 30 mm mandrel braided with 1760 dtex SK78 should
be evaluated at 30.96 mm, not 30 mm.

## Per-yarn notes

### PET (high-tenacity polyester) — braid first, learn on this

PET is the cheapest yarn on the list, the most forgiving on the
machine, and the easiest to buy in small lots. High-tenacity grades
(≥7 g/d, terminal modulus ≥20 g/d) are the industrial standard for
tire cord, seat belts and conveyor belting, so supply is deep and
grades are well documented. Elongation of 13–18% gives a braid some
give before anything snaps, and moderate friction means the braid
stays where the machine puts it. Downsides for the programme: the
lowest strength-to-weight of the five (a PET sleeve is a teaching
sleeve, not a tendon), and 0.4% moisture regain is low but not zero.
**Verdict: first sleeves, process development, and any sleeve that
will be cut open and inspected. Buy 1100–1670 dtex high-tenacity
multifilament.**

### Nylon 6,6 (high-tenacity) — the compliant sleeve

Nylon's selling point is not strength — it is stretch and recovery.
Elongation at break of 20–40% and excellent elastic recovery make it
the only yarn here that can act as a compliant element: a sleeve
that stretches and comes back, an elastic return layer, a soft
tissue analogue. It also has the best abrasion resistance of the
commodity fibres. The costs: 3–5% moisture regain (wet nylon is a
different yarn — strength and dimensions shift, and it must be
dried before precision work), the lowest modulus here (a nylon
sleeve creeps into its shape under load and stays there), and fair
UV resistance. **Verdict: second yarn to buy; use where compliance
is the point, never where dimensional stability is.**

### UHMWPE (Dyneema SK78 / Spectra S-900) — the load yarn

The strongest fibre per weight on the list: 3.2–3.4 GPa at
0.97 g/cm³ — it floats, and it is roughly 15× the specific strength
of steel. SK78 (not SK75) is the grade to specify: identical
tenacity and modulus to SK75, but creep of 0.006%/day vs 0.02%/day
at 30 °C and 300 MPa, thanks to side-chain molecular anchors.
SK99 is stronger still (42.5 cN/dtex, 155 GPa) at a 15–30% price
premium per step, but SK78 is the high-cycle standard and the right
default. Spectra S-900 is Honeywell's equivalent (1200 denier:
79 lb / 351 N break, 73 GPa modulus, 3.9% elongation).

The traps are all in handling, not in the datasheet:

- **Friction is ~0.05 fibre-on-fibre, ~0.1 against steel.** Knots
  slip — a square knot behaves as a sliding knot in UHMWPE — and
  braid crossings can walk under cyclic load. Carrier tension and
  take-up must be set with this in mind, and terminations need
  splices or extra loops, not knots.
- **Creep is real under sustained load**, even at SK78's improved
  rate: a tendon held at working load for weeks will lengthen.
  Pre-stretch before use; do not design a holding tendon on
  SK75.
- **Melting point 147 °C** is the lowest on the list. A warm body
  (35–37 °C skin) is fine; a hot actuator, a soldering iron, or a
  heated build plate is not. Keep UHMWPE away from heat sources
  in the build.
- **Cutting and sewing are hard** for the same reason the fibre is
  strong: it is slippery and tough. Expect to need hot-cutting or
  dedicated shears.

**Verdict: the load-bearing sleeve and tendon yarn. Specify SK78
(or Spectra S-900), 1760 dtex, pre-stretched. Budget for the
handling learning curve — the first UHMWPE sleeve will fight the
machine.**

### Aramid (Kevlar 49 / Twaron) — heat and cut, with a warning

Kevlar 49 is the stiffest aramid here (112 GPa) with 3.0 GPa
strength, no melting point (decomposes 425–480 °C), and excellent
cut resistance — the right yarn for a sleeve that must survive
heat or a sharp edge. But it is the worst braiding yarn on the
list for a moving body: bending fatigue is poor (aramid's
compressive and shear strength are poor; bending failure is driven
by compressive/shear damage, and fatigue life depends strongly on
bend angle and pretension), and the fibres fibrillate — they split
into microfibrils, shed material into the braid track, and lose
strength at every crossing. Abrasion resistance in rope service is
rated poor; aramid ropes are normally given a protective outer
sheath. It also absorbs 3.5% moisture and degrades in UV.
**Verdict: buy only for a specific heat/cut requirement, and
sheath it. Never the default sleeve yarn, never a flexing tendon.**

### Vectran (LCP) — the dimensional-stability yarn

Vectran HT (3.2 GPa, 75 GPa, 3.8% elongation, 1.40 g/cm³) is the
quiet standout: very low creep, excellent flex/fold fatigue,
<0.1% moisture regain, <0.2% shrinkage in boiling water or 180 °C
air, and a 350 °C melting point. It is the only yarn here that
holds its dimensions under load, heat, and humidity all at once —
which is exactly what a tendon or a sensor-carrying braid needs.
Trade-offs: modulus (75 GPa) is below UHMWPE and aramid, strength
per weight is below SK78, and it is a speciality yarn — fewer
suppliers, higher price, and less small-lot availability than PET
or nylon. Note also that the manufacturer's "no measurable creep
to 50% of break" claim is contradicted by NASA testing, which
measured creep about five times less than Kevlar — still excellent,
but not zero.
**Verdict: the tendon and precision-braid yarn once the machine
works. Worth the price where a sleeve must not grow, shrink, or
drift.**

## Buying order (Phase 1)

1. **PET HT, 1100–1670 dtex** — first sleeves, machine shakedown,
   geometry checks against the simulator. Cheap, forgiving, honest.
2. **Nylon 6,6 HT, 840–1670 dtex** — compliant sleeves and elastic
   layers, once the machine runs.
3. **Dyneema SK78, 1760 dtex** — first load-bearing sleeve and
   tendon trials. Pre-stretched; plan terminations as splices.
4. **Vectran HT, 1670 dtex** — precision tendons and any braid that
   carries sensors or must hold dimension.
5. **Kevlar 49, 1140 denier** — only on a named heat/cut
   requirement, sheathed, and never as a flexing element.

## What to measure on the first lots

Before any sleeve is trusted, measure the lot in hand: break force
of five single yarns (ASTM D2256-style, or the braider's own
tension rig), yarn diameter under a microscope or caliper, and
friction behaviour in a simple capstan test. Record the lot, the
supplier, and the measured values in the sleeve's build note.
Datasheet values are typical values; braided-sleeve strength is
what the lot actually does, derated 65–80% for the braid.

## Open questions

- **Small-lot sourcing and price**: PET and nylon are commodity
  yarns available by the spool from textile suppliers; SK78,
  Vectran, and Kevlar 49 are speciality yarns sold through
  distributors (e.g. Fiber-Line, Goodfellow) — prices were not
  verified for this note and should be quoted per lot before
  budgeting.
- **Yarn-on-yarn friction in a braid**: published friction
  coefficients are single-fibre or rope-level values; the
  effective friction inside a 16-carrier braid at working
  tension is unmeasured. A capstan / braid-pull test on the
  first PET and SK78 sleeves would close this.
- **Aramid flex-fatigue limit in braid geometry**: no published
  cycle-life number exists for Kevlar 49 in a maypole braid at
  body-scale bend radii. If aramid is ever needed in a flexing
  part, that test has to be run, not assumed.

## Sources

1. TMG Webbing — "SK75 vs SK78 vs SK99: Which UHMWPE Fiber Grade
   Should You Specify?" (datasheet consolidation, DSM/Avient,
   Honeywell Spectra) —
   https://tmgwebbing.com/blog/uhmwpe-fiber-grades-sk75-sk78-sk99-guide.html
2. Avient/Dyneema — Dyneema comprehensive fact sheet (SK75/SK78/
   SK65/SK62 tensile strength, modulus, elongation, abrasion,
   fatigue) —
   https://www.vanwalt.com/pdf/fact-sheets/Dyneema-Comprehensive-factsheet-UHMWPE.pdf
3. DuPont — Kevlar Aramid Fiber Technical Guide, Table II-1
   (Kevlar 29/49 yarn properties: 264 N break, 112 GPa modulus,
   2.4% elongation at 1140 denier) —
   https://docslib.org/download/5121755/kevlar%C2%AE-aramid-fiber-technical-guide-table-of-contents
4. DuPont Kevlar 49 datasheet via MatWeb/lookpolymers (3000 MPa,
   112 GPa, 2.4%, density 1.44) —
   https://lookpolymers.com/pdf/DuPont-Kevlar-49-Aramid-Fiber.pdf
5. Fiber-Line — High Performance Synthetic Fibers product selection
   guide (tenacity/modulus/elongation/density across Kevlar,
   Vectran, Zylon, UHMWPE, PET, nylon) —
   https://www.plasticomp.com/sites/default/files/2021-07/fiber-line-global-product-selection-guide.pdf
6. US Patent 5,403,659 — dimensionally stable high-tenacity PET
   yarn (tenacity ≥7 g/d, terminal modulus ≥20 g/d) —
   https://patents.justia.com/patent/5403659
7. GLYarn — "What is the Acceptable Tenacity for Industrial
   Polyester Filament Yarn?" (PET tenacity 3 to >10 cN/dtex,
   modulus 2–7.5 GPa) —
   https://www.glyarn.com/what-is-the-acceptable-tenacity-for-industrial-polyester-filament-yarn/
8. TextileBlog — "Polyamide Fibre: Properties, Production and Uses"
   (nylon 6,6: density 1.14–1.15, tensile strength 4–9 g/den,
   modulus 0.5–3 GPa, elongation 20–40%, moisture regain 3–5%) —
   https://www.textileblog.com/polyamide-fibre-properties-production-and-uses/
9. Kuraray — Vectran product brochure (HT: 3.2 GPa, 75 GPa,
   3.8% elongation, density 1.40, <0.1% moisture, melts 350 °C,
   excellent flex fatigue, very low creep) —
   https://www.kuraray.com/content/dam/kuraray/europe/de/products/vectran/brochures/vectran_product_brochure.pdf
10. Kuraray Vectran HT 1500/300 LCP fiber datasheet via
    lookpolymers (3200 MPa, 75 GPa, 3.3–3.7% elongation) —
    https://www.lookpolymers.com/pdf/Kuraray-Vectran-HT-1500300-LCP-Fiber.pdf
11. GLYarn — "What Are Abrasion-Resistant Yarns?" (Martindale
    ranges: nylon 6,6 40,000–100,000+; HT polyester 25,000–60,000;
    aramid 100,000–500,000+) —
    https://www.glyarn.com/what-are-abrasion-resistant-yarns/
12. Smart Armours — "Cut and Abrasion Resistance of Workwear"
    (fibre comparison table: Kevlar abrasion moderate, HMPE
    low-moderate, nylon high, PET good) —
    https://smartarmours.com/cut-and-abrasion-resistance-of-workwear/
13. Minerva — "Design with Ultra Strong Polyethylene Fibers"
    (UHMWPE friction μ ≈ 0.05 fibre–fibre, ~0.1 vs steel; knot
    slippage; creep; low transverse compression strength) —
    https://www.minervasyte.us/blogs-design-with-ultra-strong-polyethylene-fibers.html
14. Cai et al. — "Study on the Bending Fatigue Behavior of Single
    Aramid Fibers", J. Fiber Bioeng. Inform. 7:1 (2014) 13–22
    (aramid bending fatigue; compressive/shear failure) —
    https://www.mdpi.com/2617-8699/7/1/13/pdf
15. Univ. of Twente — "Assessing internal mechanical damage in
    aramid ropes using ATR-FTIR spectroscopy" (2025) (cyclic
    bending fatigue → fibrillation and peeling at strand
    interfaces) —
    https://research.utwente.nl/en/publications/assessing-internal-mechanical-damage-in-aramid-ropes-using-atr-ft/
16. Honeywell — Spectra S-900 1200 denier datasheet (79 lb break,
    73 GPa modulus, 3.9% elongation, density 0.97) —
    https://honeywell-65-prod.adobecqms.net/us/en/products/spectra-fibers/industrial-grade-fiber/s-900/spectra-1200-denier-s-900
17. TextileSphere — "Vectran High-performance Fibre" (NASA creep
    testing: ~5× less than Kevlar, contradicting the no-creep
    claim) —
    https://www.textilesphere.com/2021/05/vectran-high-performance-fibre.html?m=1
