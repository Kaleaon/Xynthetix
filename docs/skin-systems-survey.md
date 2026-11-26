# Skin Systems Survey — What the Literature Supports for a Synthetic Body's Skin

**Date:** 2026-11-26 (Thu — skin / power / thermal rotation)
**Status:** Research survey v1.0 — companion to
`sensing-proprioception-survey.md`, `sensor-layer-spec.md`, and
`power-thermal-budget.md`
**Scope:** How a human-scale synthetic body gets a skin: cast silicone,
3D-printed elastomers, fur/hair attachment, and the trade-off between skin
thickness and tactile transparency. Sources were opened and read this
session (see §8 for what could *not* be verified).

## Key findings (up front)

1. **Cast platinum silicone is the default skin material, and the grades
   are already decided by the numbers.** Smooth-On Ecoflex 00-30
   (Shore 00-30, 900% elongation, 38 pli tear) and Dragon Skin 10–20
   (Shore 10–20A, 620–1,000% elongation, 102–120 pli tear) bracket the
   whole softness range a body needs, and both are skin-safe, room-temp
   cure, and sold in trial sizes. Nothing printed comes close on
   elongation or tear strength (§1–2).
2. **3D-printed elastomers are for moulds, fittings, and thin parts —
   not for the skin itself.** The best printable elastomers (Agilus30,
   Formlabs Silicone 40A) top out at 220–270% elongation and 5–7 kg/cm
   tear, against 620–1,000% and ~18–21 kg/cm for cast Dragon Skin.
   FDM TPU is far too hard (85–95A) for a skin. The one genuine
   exception: Formlabs Silicone 40A is a true printable silicone and
   the only printable elastomer found with a skin-contact rating
   (BioMed Flex 50A, >30 days).
3. **Thickness vs tactile transparency has anchors, not a curve.**
   GelSight fingertip elastomers run under 2.5 mm; LuxTac's flexible
   optical array is ~3.5 mm thick and still resolves 104 mN. No paper
   found plots sensitivity against silicone thickness parametrically —
   that experiment is ours to run (§4, gap G1). The published rule is
   qualitative: softer/thinner = more sensitive, harder/thicker = wider
   force range.
4. **Fur is a solved craft problem, not a research problem.** Fursuit
   practice — sewn faux fur over a foam base, with hair punching into
   silicone for faces — is mature, repairable, and cheap. The open
   question for us is not *how* to attach fur but how fur interacts
   with the tactile layer underneath it (§3, §7).
5. **Self-healing skin is real science and zero products.** Bao 2012
   heals conductivity in 15 s and mechanics in ~10 min at room
   temperature; Terryn 2017 and Menasce 2023 extend it to soft robots
   and 3D-printed silicones. Nothing is buyable as "self-healing robot
   skin" today. Plan for replaceable skin panels, not healing ones
   (§5).
6. **The open-source skin landscape is thin but real.** LuxTac
   (CC BY-NC-SA 4.0) and Digit 360 (CC BY-NC 4.0) are the two
   open-licensed tactile skins with published numbers; both are
   non-commercial licences, which constrains a company that intends to
   sell bodies (§6).

---

## 1. Silicone casting

### 1.1 The two product lines that matter

Platinum-cure (addition-cure) RTV silicone is the standard for
animatronic, prosthetic, and special-effects skin: room-temperature
cure, negligible shrinkage, skin-safe when cured, and a hardness range
that spans jelly to firm rubber. Two Smooth-On lines cover it:

**Ecoflex series** (Shore 00 scale — the soft end)
[product line](https://www.smooth-on.com/product-line/ecoflex/) ·
[Ecoflex 00-30](https://www.smooth-on.com/products/ecoflex-00-30/)

| Grade | Shore | Pot life | Cure | Tensile | Elongation | Die B tear |
|---|---|---|---|---|---|---|
| Ecoflex 00-10 | 00-10 | — | — | — | — | — |
| Ecoflex 00-20 | 00-20 | — | — | — | — | — |
| Ecoflex 00-30 | 00-30 | 45 min | 4 h | 200 psi | 900% | 38 pli |
| Ecoflex 00-50 | 00-50 | — | — | — | — | — |
| Ecoflex 5 | 5A | — | — | — | — | — |
| Ecoflex GEL | 000-35 | — | — | — | — | — |

Ecoflex 00-30 in full: Shore 00-30, 1A:1B by weight or volume, mixed
viscosity 3,000 cps, 100% modulus 10 psi, specific gravity 1.07 g/cc,
service range −65 to 450 °F, translucent. The technical bulletin
([PDF](https://www.smooth-on.com/tb/files/ECOFLEX_SERIES_TB.pdf))
states Ecoflex is "suitable for… prosthetic appliances, cushioning
for orthotics and special effects applications (especially in
animatronics where repetitive motion is required)" and that cured
Ecoflex is skin-safe, certified by an independent lab. Caveats from
the same sources: Ecoflex 00-10 cures with a tacky surface, and
Ecoflex 00-20 FAST trades pot life for speed (20 min pot, 1 h cure).

**Dragon Skin series** (Shore A scale — the durable end)
[product line](https://www.smooth-on.com/product-line/dragon-skin/)

| Grade | Shore | Pot life | Cure | Tensile | Elongation | Die B tear |
|---|---|---|---|---|---|---|
| Dragon Skin 10 FAST | 10A | 8 min | 75 min | 475 psi | 1,000% | 102 pli |
| Dragon Skin 20 | 20A | 25 min | 4 h | 550 psi | 620% | 120 pli |

[Dragon Skin 10 FAST](https://www.smooth-on.com/products/dragon-skin-10-fast/) ·
[Dragon Skin 20](https://www.smooth-on.com/products/dragon-skin-20/)
Dragon Skin 10 FAST also lists dielectric strength >350 V/mil —
relevant if the skin ever sits near HV DEA drive lines. The line
also includes FX-Pro, 15, 25 NV, and 30, with pot lives from 4 to
45 min and cures from 30 min to 16 h. Both lines are sold in 2 lb
trial, 1 gal (16 lb), 5 gal (80 lb), and 55 gal (880 lb) units.

**Reading the table:** Dragon Skin 20 is roughly 2.75× the tensile
strength and 3.2× the tear strength of Ecoflex 00-30 at ~6× the
100% modulus — that is the durability-vs-softness trade in one
comparison. Ecoflex is the "feels like skin" choice; Dragon Skin is
the "survives being a body" choice. A body will almost certainly
want both, zoned: soft Ecoflex-class silicone where touch matters
(face, hands, inner arms), Dragon Skin-class where abrasion and
handling dominate (palms, knees, feet, back).

### 1.2 Cure inhibition — the trap that ruins casts

Platinum silicones are inhibited by latex, tin-cure silicone, sulfur
clays, certain woods, and newly cast polyester/epoxy/urethane — the
silicone stays liquid against the contaminated surface. The product
pages' advice is to test a small patch first. For us this is a
process rule, not a footnote: any mould, release agent, or embedded
element (sensor, yarn, heater wire) that touches uncured platinum
silicone must be inhibition-tested before a full-body cast. Tin-cure
silicones do not have this failure mode but shrink more and are not
skin-safe in the same way — not a substitute.

### 1.3 Other manufacturers — unverified

- **Shin-Etsu:** product families confirmed (one- and two-component
  liquid rubbers for mouldmaking and for electric/electronic uses,
  rubber compounds, LIMS liquid injection moulding) at
  [shinetsusilicone-global.com](https://www.shinetsusilicone-global.com/products/)
  — no specific grade numbers retrieved.
- **Wacker Elastosil:** wacker.com is bot-blocked from this VM; no
  grades verified. Both are gap G2 (§8) — they matter because
  Smooth-On is a US hobby/pro supplier and industrial volumes will
  eventually need an industrial supplier.
- **Cost per kg:** not verified. Smooth-On lists no prices on product
  pages; the distributor page returned 403. Do not use any $/kg
  figure for silicone until a distributor price list is read
  (gap G3).

### 1.4 Skin thickness on humanoid hands/faces — no published number

No published figure for typical skin thickness on a humanoid hand or
face was found in this pass. The nearest hard numbers are the
tactile-sensor elastomers in §4 (GelSight <2.5 mm, LuxTac 3.5 mm).
Human skin itself is ~0.5–4 mm depending on site (dermis + epidermis),
but that is anatomy, not a robot-skin specification — a robot skin
also has to carry sensors, survive handling, and be castable, so the
number will be set by the §4 trade-off, not by copying anatomy.

---

## 2. 3D-printed elastomers

### 2.1 FDM thermoplastic polyurethane (TPU)

- **UltiMaker TPU 95A** —
  [product page](https://www.ultimaker.com/materials/tpu-95a):
  48 Shore D (≈95A), "easier and faster to print than other TPU
  filaments", aimed at parts that conform to existing surface
  geometry. No tensile/elongation figures on the page.
- **NinjaFlex (85A)** — NinjaTek's site is Cloudflare-blocked
  (HTTP 522, including the TDS PDF and Wayback copies); only the
  "85A" rating is confirmed, from the search-result title of
  [ninjatek.com/shop/ninjaflex](https://ninjatek.com/shop/ninjaflex/).
  Full TDS numbers unverified (gap G4).

**Verdict:** FDM TPU at 85–95A is far too hard for a skin (compare
Ecoflex 00-30 / Dragon Skin 10A) and carries layer lines. Its role
is fittings, gaskets, cable glands, and compliant joints — not skin.

### 2.2 PolyJet — Stratasys Agilus30

[Agilus30](https://www.stratasys.com/en/materials/materials-catalog/polyjet-materials/agilus30/):
Shore A 30–35, tensile 2.4–3.1 MPa, elongation 220–270%, tear
5–7 kg/cm, "superior tear-resistance, capable of withstanding
repeated flexing and bending." PolyJet-only printers (J7/J8/Objet
Connex), multi-material capable — so a rigid core and a soft shell
can print in one job.

**Verdict:** the smoothest printable elastomer surface available,
but elongation 220–270% vs 620–1,000% for cast Dragon Skin, and tear
5–7 kg/cm vs ~18–21 kg/cm (120 pli ≈ 21 kg/cm). Good for fingertip
pads, gaskets, and prototype skins; not a body skin.

### 2.3 DLP/SLA resins — Formlabs

[Formlabs materials](https://formlabs.com/materials/):

| Resin | Shore | Notes |
|---|---|---|
| Flexible 50A | 50A | Translucent |
| Flexible 80A Resin V2 | 80A | "2× higher tear strength, 2× higher elongation at break, 4× higher rebound" vs v1; tack-free matte black |
| **Silicone 40A Resin** | 40A | "The first accessible 100% silicone 3D printing material" (Pure Silicone Technology); 230% elongation at break; 12 kN/m tear strength |
| BioMed Flex 50A | 50A | Rated for long-term skin contact (>30 days) and short-term mucosal contact |

**Verdict:** Silicone 40A is the closest printed analogue to cast
silicone — a real silicone, printable — but at 230% elongation and
12 kN/m tear it is still well below cast Dragon Skin on both axes,
and 40A is harder than the softest cast grades. BioMed Flex 50A is
the only explicitly skin-contact-rated printable elastomer found,
which matters if any printed part touches a human for extended
periods. Loctite 3D IND405 and Resione flexible resins were not
verified (Henkel page 404'd; gap G4).

### 2.4 Printed vs cast — the comparison

No head-to-head published comparison of printed vs cast elastomer
skins was found. The qualitative picture from the sources above:

| Property | Cast silicone (Dragon Skin 20) | Best printed (Agilus30 / Silicone 40A) |
|---|---|---|
| Elongation | 620% | 220–270% |
| Tear | 120 pli (~21 kg/cm) | 5–7 kg/cm / 12 kN/m |
| Hardness floor | Shore 00-10 | ~30–40A |
| Surface | Optically clear, smooth (GelSight uses cast silicone/TPE) | Smooth (PolyJet/SLA) but layer/step artefacts on FDM |
| Scale | Mould-limited; whole-body casts possible | Build-volume-limited; panels only |

**Design rule:** cast the skin; print the moulds, the fittings, and
the thin rigid/soft interface parts. Revisit if a printable silicone
reaches ~600% elongation with cast-class tear.

---

## 3. Fur and hair attachment

Fur is a surface system on top of the skin, and the craft is mature.
What follows is trade practice from the sources that could be
opened; where no primary tutorial was reachable, that is flagged.

### 3.1 Methods

- **Sewn faux fur over a foam base (fursuit method).** The
  established pipeline, documented at
  [matrices.net](https://matrices.net/tutorials.htm): a carved foam
  head/base, patterned faux fur sewn over it (free-form patterning,
  hidden zippers, fur shaved to length). Wikipedia's
  [Fursuit](https://en.wikipedia.org/api/rest_v1/page/summary/Fursuit)
  summary confirms faux-fur construction and duct-tape-dummy
  fitting. This is the most repairable method: re-sew or re-glue
  panels, re-shave to length.
- **Flocking.** Depositing many small fibre particles ("flock") onto
  an adhesive-coated surface; thin fibres give a soft velvety
  surface, thicker fibres a bristle-like surface
  ([Flocking (texture)](https://en.wikipedia.org/wiki/Flocking_(texture))).
  Standard for velvet-like short pile. Least repairable — a damaged
  area means re-flocking the whole area — and durability is limited
  by the adhesive bond and fibre shedding (no quantitative durability
  data found).
- **Hair punching.** Standard SFX practice: a hooked punching needle
  pushes small bundles of hair through cured silicone so the loop
  anchors on the back, often sealed with a thin silicone wash.
  Durable but slow to install and hard to patch invisibly.
  **Verification gap:** no reachable primary tutorial page in this
  pass — Stan Winston School is a JS-gated SPA, Monster
  Makers/Kryolan pages were blocked or unfindable. Do not cite a
  specific tutorial URL until one is opened (gap G5).
- **Glued / wefted fur.** Wefts (hair sewn onto a strip) glued or
  sewn onto the skin — widely used in wigs and mascot work. No
  primary source opened for silicone-specific weft gluing (gap G5).

### 3.2 What fur does to the sensing problem

This is the open question, and it is ours, not the literature's:
fur sits *between* the world and the tactile layer. A dense fur pile
spreads a point contact over a wider area and attenuates peak
pressure — the same direction as thicker silicone (§4), but with a
pile that also moves, mats, and sheds. Consequences for the sensor
spec (`sensor-layer-spec.md`):

- Taxel pitch and force thresholds calibrated under bare silicone
  will read differently under fur; calibration must be done
  **through the fur**, not before it is attached.
- Fur is also a thermal insulator — the warm-body budget
  (`power-thermal-budget.md`) assumes bare or lightly covered skin;
  a furred body loses less heat at the surface and needs less heater
  power, but the skin temperature *under* the fur will read
  differently from the surface temperature a hand feels.
- Serviceability argues for fur as a **separate, removable layer**
  (zippered/velcroed panels, fursuit-style) over a replaceable
  silicone skin, rather than hair punched permanently into the skin.
  The ReSkin lesson from the sensing survey — dumb skin, smart
  substrate, recalibrate on swap — applies twice over once fur is
  in the stack.

---

## 4. Thickness vs tactile transparency

### 4.1 Published anchors

- **GelSight** — Yuan, Dong & Adelson, "GelSight: High-Resolution
  Robot Tactile Sensors for Estimating Geometry and Force",
  *Sensors* 2017, 17, 2762
  ([PDF](https://mdpi-res.com/d_attachment/sensors/sensors-17-02762/article_deploy/sensors-17-02762.pdf),
  open access, CC BY). Fingertip sensor elastomer is a clear
  silicone, neo-Hookean coefficient μ = 0.145 MPa, hardness ≈
  Shore 00-45; sensor elastomer sheets are "much thinner (under
  2.5 mm)" and domed; typical elastomer Shore A 5–20; minimum
  perceivable force mostly <0.05 N (limit of the ATI Nano-17 used
  for calibration). The trade-off is stated explicitly: softer
  elastomer = sensitive to small contact force; harder elastomer
  needed for heavy-load measuring range. The reflective coating is
  a thin silicone + pigment layer (bronze/aluminium flake), kept
  thin to preserve fine detail. Commercial product:
  [gelsight.com](https://gelsight.com/) (GelSight Mini).
- **LuxTac** — Prince et al., arXiv:2611.23575
  ([abstract](https://arxiv.org/abs/2611.23575),
  [project](https://luxtac.github.io)): flexible optical taxel
  array, **~3.5 mm thick**, built from off-the-shelf parts; each
  taxel is an RGBC light sensor under a translucent white silicone
  layer capped by an opaque black film; normal-force response
  linear (R² = 0.999) from **104 mN to ≥5.8 N**, 2.0%
  repeatability, 5.9% hysteresis; a shear cartridge resolves
  per-taxel 3-axis force (R² 0.92–0.96). Open-source,
  **CC BY-NC-SA 4.0**.
- **iCub skin** — arXiv:1609.09720
  ([abstract](https://arxiv.org/abs/1609.09720)): the iCub forearm
  skin is a capacitive taxel array, calibrated by vacuum-bag
  uniform pressure, pressure↔capacitance characterised per taxel,
  net normal force by integrating over skin geometry. (The iCub
  hardware repo page 404s — repo appears moved/renamed; licence
  unverified.)
- **BioTac** — SynTouch's site blocked (403) this session; arXiv
  papers confirm it as the reference fluid-filled fingertip sensor,
  e.g. arXiv:2101.05452 "Interpreting and Predicting Tactile
  Signals for the SynTouch BioTac". No skin-thickness number
  verified (gap G6).

### 4.2 What is missing

**No paper was found that plots sensitivity vs silicone thickness
parametrically** (e.g. 1/2/4 mm over the same sensor). That is the
main gap (G1): the GelSight <2.5 mm and LuxTac 3.5 mm figures are
concrete anchors, and the GelSight hardness trade-off is the closest
published statement of the rule, but the curve itself is
unpublished. It is also the cheapest experiment in this whole
programme: one capacitive taxel, silicone sheets of 1/2/3/5 mm at
two hardnesses, a force gauge, and a plot. It belongs on the
experiment list before any full-body skin thickness is specified.

### 4.3 Working thickness budget (estimates, from the anchors)

Using the reference body from `power-thermal-budget.md`
(75 kg / 1.75 m, surface area ≈ 1.9 m²) and Ecoflex 00-30 density
(1.07 g/cc):

| Skin | Mass (estimate) | Notes |
|---|---|---|
| 2 mm silicone over 1.9 m² | ≈ **4.1 kg** | 1.9 × 0.002 × 1070 |
| 3 mm silicone over 1.9 m² | ≈ **6.1 kg** | Same arithmetic |
| 5 mm silicone over 1.9 m² | ≈ **10.2 kg** | GelSight/LuxTac anchors say this is already too thick for fine touch |

A 2–3 mm skin costs 4–6 kg of the weight budget before fur,
sensors, or heaters — it is not a rounding error, and it is another
reason the thickness-vs-sensitivity curve (§4.2) has to be measured
rather than assumed. Zoning helps: thin (1–2 mm) soft skin where
touch resolution matters, thicker tougher skin where it does not.

---

## 5. Self-healing and repairable surfaces

All published self-healing elastomers are lab-scale. Nothing is
buyable as "self-healing robot skin" today.

- **Bao et al. 2012, *Nature Nanotechnology***
  ([nature.com](https://www.nature.com/articles/nnano.2012.192)):
  supramolecular polymer + nickel nanostructured microparticles;
  conductivity up to 40 S/cm; on rupture, conductivity repeatably
  restored to ~90% after **15 s** healing, mechanical properties
  fully restored after **~10 min** at ambient conditions;
  pressure- and flexion-sensitive. Lab demo, not a product.
- **Terryn et al. 2017, *Science Robotics***
  (DOI 10.1126/scirobotics.aan4268, verified via Crossref — authors
  Terryn, Brancart, Lefeber, Van Assche, Vanderborght, 16 Aug 2017):
  "Soft robots manufactured out of self-healing polymers have the
  ability to repair macroscopic damage." Full text unreachable from
  this VM (science.org Cloudflare-blocked; VUB repository host
  connection failed), so healing conditions/times are **not**
  verified here (gap G7). Diels-Alder chemistry, heat-triggered, is
  the mechanism named in the literature — treat as unverified until
  the PDF is read.
- **Menasce et al. 2023**, arXiv:2311.05633
  ([abstract](https://arxiv.org/abs/2311.05633)): 3D-printed
  architectured silicones with **autonomic self-healing at room
  temperature** (dioxaborolane vitrimer chemistry) combined with
  covalent networks for creep resistance; demonstrated as a
  patient-specific vascular phantom. Closest to a printable
  self-healing robot skin; still research-stage, no commercial
  product.
- Also surfaced (abstracts read): arXiv:1706.00501, "Tough
  self-healing elastomers by molecular enforced integration of
  covalent and reversible networks" (2017).

**Design rule:** plan for **replaceable skin panels** (the ReSkin
model from the sensing survey — dumb skin, smart substrate,
recalibrate on swap), not healing skin. Track self-healing as a
research watch item; revisit if a commercial self-healing silicone
appears.

---

## 6. Open-source robot skin / tactile projects

| Project | What it is | Licence / access |
|---|---|---|
| **LuxTac** — [luxtac.github.io](https://luxtac.github.io), arXiv:2611.23575 | Flexible optical taxel array, 3.5 mm, shear-sensing, off-the-shelf parts | **CC BY-NC-SA 4.0** (non-commercial, share-alike) |
| **Digit 360** — [digit.ml](https://digit.ml), [github.com/facebookresearch/digit360](https://github.com/facebookresearch/digit360) | Meta FAIR finger-shaped tactile sensor; ~8.3M taxels, hemispherical compliant embodiment; 7 µm spatial detail, 1 mN force; assembled units free to researchers via proposal | Repo LICENSE is **CC BY-NC 4.0**. Note: the original `facebookresearch/digit` repo now 404s — superseded by digit360 |
| **RobotSweater** — arXiv:2303.02858 | Machine-knitted pressure-sensitive tactile skin from off-the-shelf yarns; closed-loop human lead-through demonstrated | Paper only; repo/licence not verified — check before reuse |
| **BubbleTouch** — arXiv:1809.09153 | Open-source quasi-static simulator for robotic tactile skins (contact-force traces for tactile object recognition) | Described as open source in the abstract; repo URL/licence not verified |
| **e-NABLE** — [enablingthefuture.org](http://enablingthefuture.org) | Global volunteer community, open-source 3D-printed prosthetic upper-limb designs; ~40,000 volunteers, 10,000–15,000 recipients | Open-source designs; per-design licences vary — verify per file |
| **OpenBionics (open-source initiative)** — [github.com/OpenBionics](https://github.com/OpenBionics) | "An open-source initiative for… affordable, light-weight, modular robot and prosthetic hands" (<$100, <200 g, underactuated) | Open-source initiative; per-repo licences not checked. Distinct from commercial openbionics.com (Hero Arm, clinical product) |
| **iCub skin** — arXiv:1609.09720 | Capacitive whole-body tactile skin on the iCub humanoid | Hardware repo currently unreachable (404); licence unverified |
| **GelSight** — [gelsight.com](https://gelsight.com) | Commercial; foundational paper is open-access (Sensors 2017, CC BY) but the sensor is a product, not open hardware | Paper CC BY; hardware proprietary |

**Also surfaced, not fully verified:** arXiv:2611.05936 "LumiTac"
(compact six-axis optical tactile sensor, 2026) and
arXiv:2608.02080 "Toward Geometry-Scalable Whole-Body Touch for
Humanoids: A 3D-Printed Conformal EIT Skin" (2026) — both from
arXiv search results only; abstracts not opened. Worth a follow-up
pass.

**Licence warning:** the two best open tactile skins (LuxTac,
Digit 360) are both **non-commercial** licences. A company that
intends to sell bodies cannot ship either as-is. They are reference
designs and benchmarks, not components — the same care the
programme already takes with licences elsewhere applies here.

---

## 7. Xynthetix implications

1. **Skin stack, first version:** cast silicone over the tactile
   layer, zoned — Ecoflex 00-30-class (soft) at face, hands, inner
   arms; Dragon Skin 10–20-class (durable) at palms, knees, feet,
   back. Target 2–3 mm, 4–6 kg for the reference body, pending the
   §4.2 measurement.
2. **First experiment (cheap, decisive):** one capacitive taxel,
   silicone sheets 1/2/3/5 mm at two hardnesses (00-30 and 10A),
   force gauge, plot sensitivity vs thickness. This closes gap G1
   and sets the thickness spec for every later skin decision.
3. **Printed elastomers stay in the mould shop:** print moulds,
   fittings, gaskets, fingertip pads; cast the skin. Formlabs
   Silicone 40A is the watch item for printed skin parts.
4. **Fur is a removable layer, not part of the skin:** zippered /
   velcroed fursuit-style panels over replaceable silicone; calibrate
   the tactile layer through the fur; budget the fur's thermal
   insulation in the warm-body numbers.
5. **Repairability is the durability strategy:** replaceable panels
   + recalibration on swap (ReSkin model), not self-healing
   materials — nothing buyable exists yet.
6. **Cure-inhibition testing is a process gate:** every mould,
   release agent, and embedded element gets a patch test before a
   full cast. This is the cheapest way to avoid ruining a
   body-scale pour.

## 8. Gaps and unverified items

- **G1.** No parametric sensitivity-vs-thickness study found — the
  core experiment is unrun; see §4.2.
- **G2.** Wacker Elastosil and Shin-Etsu specific grades/numbers
  unverified (Wacker bot-blocked; Shin-Etsu only categories
  retrieved).
- **G3.** Silicone cost per kg unverified — no prices on
  manufacturer pages; distributor blocked.
- **G4.** NinjaFlex full TDS unverified (NinjaTek Cloudflare-blocked);
  Loctite IND405 / Resione flexible resins not verified.
- **G5.** Hair punching / weft gluing: no reachable primary tutorial
  this session; method described from trade practice only.
- **G6.** BioTac skin thickness and SynTouch specs unverified (site
  blocked 403).
- **G7.** Terryn 2017 healing conditions/times not verified
  (paywalled/blocked); Diels-Alder mechanism treated as unverified.
- **G8.** RobotSweater / BubbleTouch / iCub hardware repo licences
  not verified — check before any reuse.
- **G9.** Humanoid hand/face skin thickness: no published figure
  found; GelSight <2.5 mm and LuxTac 3.5 mm are the anchors.
- **G10.** LumiTac (arXiv:2611.05936) and the 3D-printed conformal
  EIT skin (arXiv:2608.02080) surfaced but not read — follow-up pass.

## Sources

24 sources opened and read this session (product pages, datasheets,
papers, project pages), plus 3 arXiv abstracts. All URLs above are
the sources; items flagged as gaps in §8 are the ones that could not
be opened or verified. Note: this session's browser tools were
unavailable from the parent agent (E2BIG environment error), so
sources were fetched by the research subagent via curl; two
follow-up arXiv items in §6/G10 were surfaced from search results
only and are flagged as such.
