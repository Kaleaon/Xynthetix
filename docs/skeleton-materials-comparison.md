# Skeleton materials comparison

**Date:** 2026-11-24 (Tue — 3D body plan rotation)
**Status:** research note. Answers the first open question in
[body-plan-research-map.md](body-plan-research-map.md) §2.1: which
structural material wins per skeleton segment once repairability and
makerspace fabrication are scored alongside stiffness and weight.

**Scope:** load-bearing skeleton structure for human-scale synthetic
bodies — long-bone links (femur, humerus, tibia), pelvis/spine
frames, and joint housings. Skin, muscle, and tendon materials are
out of scope; they have their own workstreams. All property values
below are **typical values from vendor datasheets and published
reviews, not design minimums**. Where a datasheet gives a range, the
value used is stated. Prices are retail / small-quantity US list
prices seen in November 2026 and will move; treat them as order-of-
magnitude, not quotes.

## 1. The master table

| Material | E (GPa) | Density (g/cm³) | Yield / tensile strength (MPa) | E/ρ — specific stiffness (GPa per g/cm³) | σ_yield/ρ — specific strength (MPa per g/cm³) | Notes |
|---|---|---|---|---|---|---|
| 6061-T6 aluminium | 68.9 | 2.70 | 276 yield / 310 UTS | 25.5 | 102 | The default structural metal. Isotropic, machinable, weldable [1][2] |
| Steel, A36 class | ~200 | 7.85 | ~250 yield | 25.5 | 32 | Same specific stiffness as aluminium; wins on fatigue limit and cost, loses on mass per part [13][14] |
| Ti-6Al-4V (Grade 5) | 114 | 4.43 | 828–965 yield / 895–1035 UTS | 25.7 | 187–218 | Best specific strength of the metals; expensive, slow to machine [11] |
| CFRP, pultruded unidirectional (T700/epoxy) | 134 axial / 8.7 transverse | 1.52 | 2370 axial tensile (calc.) / 63 transverse | 88 axial / 5.7 transverse | 1560 axial / 41 transverse | Axial numbers are superb; transverse and shear are the weak axes [3] |
| CFRP, woven tube, high-modulus fibre | ~112 axial | ~1.55 | — | ~72 | — | A realistic off-the-shelf structural tube; still strongly directional [4] |
| PA12, SLS/MJF (neat) | 1.65–1.9 | 0.93–1.01 | 48–50 tensile | 1.7–1.9 | ~50 | Tough, printable in complex shapes; ~40× less stiff than aluminium per weight [5][6] |
| PA12, glass/mineral-filled SLS | 2.5–3.2 | 1.2–1.3 | 38–51 tensile | ~2.1–2.5 | ~30–40 | Stiffer, but elongation at break falls to 2–3% — brittle [7][10] |
| Onyx (chopped-CF nylon, Markforged) | 2.4 | 1.2 | 40 yield / 37 break | 2.0 | 33 | Good FFF engineering plastic; the base, not the reinforcement [8] |
| Onyx + continuous carbon fibre (plaque) | 60 tensile / 51 flexural | 1.2 | 800 tensile | 50 | 667 | Plaque-optimised values; real parts are lower and direction-dependent [8] |
| PLA (FDM, in-plane) | 3.0–4.0 | 1.24–1.25 | 50–60 tensile | 2.9 | ~44 | Stiffest cheap filament; brittle, creeps, softens at 55–60 °C [9] |
| PETG (FDM, in-plane) | 1.9–2.4 | 1.27 | 40–55 tensile | 1.7 | ~38 | Tougher than PLA, lower stiffness, Tg ~80 °C [9] |
| Human cortical bone (longitudinal) | ~18 | ~1.9 | ~72 yield / ~135 UTS tensile | ~9.5 | ~38 | The biological benchmark — every engineering option above beats it on specific stiffness except the neat polymers [12] |

Reading the table:

- **Specific stiffness (E/ρ) is what decides a bending-stiffness-
  designed link, and it barely varies between metals.** Aluminium
  6061-T6, A36 steel, and Ti-6Al-4V all sit at 25.5–25.7 GPa per
  g/cm³. This is the textbook result: for a stiffness-limited part
  at fixed shape, swapping metals does not save weight. The choice
  between metals is decided by strength, fatigue, cost, and
  fabrication — not by stiffness per kilogram [13][14].
- **Carbon fibre is the only material that breaks the metal band,**
  and only along the fibres: 88 GPa per g/cm³ unidirectional,
  ~72 for a woven structural tube. Transverse to the fibres it is
  worse than printed nylon (5.7). A carbon skeleton is a layup
  design problem, not a material swap [3][4].
- **Printed polymers are 10–15× worse than metals on specific
  stiffness.** They can still work as structure, but only by using
  much larger sections (stiffness scales with diameter cubed) or by
  accepting much heavier parts. See the worked example in §3.
- **Bone itself is not the bar to clear.** Cortical bone at ~9.5
  GPa per g/cm³ is out-stiffened per weight by aluminium, titanium,
  steel, and carbon alike. The skeleton problem is joints,
  attachment, and fatigue — not matching bone's material [12].

## 2. The three properties that actually decide

### 2.1 Stiffness per weight — carbon wins, metals tie, polymers lose

Covered in §1. The practical consequence: a carbon-tube femur is
roughly a third the mass of a metal one at equal bending stiffness
(§3). A printed-polymer femur at human proportions cannot reach
the same stiffness at all without becoming a 50–60 mm solid rod.

### 2.2 Fatigue and creep — the service-life split

- **Steel is the only material here with a true endurance limit.**
  Below roughly 40–50% of its ultimate tensile strength, a steel
  part can in principle cycle indefinitely; its S–N curve flattens
  around 10⁶–10⁷ cycles [13].
- **Aluminium has no endurance limit.** 6061-T6 is rated at a
  fatigue strength of ~96.5 MPa at 5×10⁸ cycles (R. R. Moore test)
  — a finite-life number, not a safe-forever threshold. Aluminium
  structures are designed to a service life, and every load cycle
  consumes some of it [1][2][13].
- **CFRP is excellent in fibre-dominated fatigue but weak at
  joints and in the matrix.** Fibre-direction laminates show very
  little degradation under cyclic tension; the matrix, bonded
  joints, and bolted holes are where damage starts. A NASA damage-
  tolerance comparison found a carbon/epoxy face sheet's fatigue
  life ~17× an undamaged 7075-T6 aluminium sheet at the same
  fraction of ultimate load — but also a sharp static-strength drop
  after even a 2.6 J impact [14][15]. Impact damage in CFRP is
  often invisible (delamination under an intact surface), which is
  why aerospace practice includes tap-testing and inspection.
- **Printed polymers creep.** PLA is viscoelastic: measurable
  flexural creep occurs over long periods even well below its glass
  transition temperature (~55–60 °C), and one 1,000-hour test at
  23 °C and 25 MPa constant stress measured 0.41–1.35% strain
  depending on brand, against ~0.18% for ABS and ~0.11% for nylon
  6/6 under identical conditions [16][17]. Annealing at 60 °C
  reportedly cuts PLA creep deformation by ~75%, but the base
  behaviour stands: **do not put a sustained structural load on
  unreinforced PLA and expect it to hold geometry for months**
  [16][17]. Nylon (PA12) is the better creep performer of the
  printable set, but it absorbs moisture (0.52% at 23 °C/50% RH,
  up to 1.33% at 96% RH for EOS PA 2200), which changes dimensions
  and properties with humidity [6].
- **Temperature ceilings matter for a warm body.** The body plan
  calls for a 35–37 °C skin (see
  [power-thermal-budget.md](power-thermal-budget.md)). PLA's glass
  transition at 55–60 °C leaves little margin above a warm body in
  a warm room; PETG (~80 °C) and PA12 (heat deflection 86 °C at
  1.82 MPa, 140–147 °C at 0.45 MPa) are safer, and Onyx's heat
  deflection is 145 °C [5][8][9]. Aluminium, steel, titanium, and
  CFRP (epoxy Tg typically 120–180 °C, resin-dependent) are
  unaffected at body temperatures.

### 2.3 Anisotropy — the hidden tax on printed and composite parts

- **FDM parts are roughly half as strong between layers as in the
  plane.** Published maker datasheets put PLA interlayer adhesion
  at ~17 MPa against 50–59 MPa in-plane, and PETG at ~18 MPa
  against 46–50 MPa [18]. A printed skeleton part must be oriented
  so its load paths run in-plane, or it must be treated as a
  17–18 MPa material in the weak direction. SLS/MJF PA12 is much
  closer to isotropic (HP MJF PA12: 50 MPa tensile in both XY and
  Z) — one of the real reasons to pay for powder-bed printing for
  structural parts [6].
- **CFRP is anisotropic by construction.** Pultruded unidirectional
  tube: 134 GPa axial, 8.7 GPa transverse, shear modulus 5.5 GPa,
  transverse tensile strength ~63 MPa [3]. Any bolt hole, clamp,
  or side load engages the weak axes. Real structural tubes use
  off-axis plies (the Rock West high-modulus woven tube is ~112 GPa
  axial with a woven outer layer specifically to survive machining
  and drilling [4]) — and every off-axis ply costs axial stiffness.
- **Metals are isotropic for practical purposes.** This is why
  metal parts are cheap to model and trustworthy in simulation:
  one E, one yield, every direction [14].

## 3. Worked example: a femur link at equal bending stiffness

Take a 450 mm long link (a femur) with a 30 mm outside diameter,
and demand the bending stiffness of a 6061-T6 tube of 30 mm OD ×
2 mm wall. That reference tube has I ≈ 17,330 mm⁴ and
EI ≈ 1,194 N·m². Its Euler buckling load at 450 mm is
π²EI/L² ≈ 58 kN — far above body-weight loads, so bending
stiffness, not buckling, governs this case. (Method: thin-walled
tube I ≈ πD³t/8 at fixed OD, wall thickness adjusted per material;
where the required wall exceeds a quarter of the diameter, a solid
rod of the needed diameter is used instead. Mass = ρ·A·L.
Computed with the §1 values.)

| Material | Form at equal EI | Mass (450 mm) |
|---|---|---|
| 6061-T6 aluminium | tube, 1.63 mm wall | 187 g |
| Steel | tube, 0.56 mm wall | 187 g |
| Ti-6Al-4V | tube, 0.99 mm wall | 186 g |
| CFRP, pultruded uni | tube, 0.84 mm wall | 54 g |
| PA12 (SLS) | solid rod, 61.5 mm dia. | 1,337 g |
| Onyx | solid rod, 56.4 mm dia. | 1,350 g |
| PLA | solid rod, 51.0 mm dia. | 1,139 g |

What this says:

1. **The three metals are identical to within a gram.** Pick
   between them on strength, fatigue, cost, and fabrication, never
   on stiffness per weight.
2. **Carbon is 3.4× lighter than metal here** — 54 g vs ~187 g.
   That is the whole case for carbon spars in a body that must
   carry its own weight plus actuators and batteries.
3. **Printed polymer cannot be the femur at human proportions.**
   A 51–62 mm solid rod is not a femur — it is a club — and it
   still weighs 6–7× the aluminium tube. Printed polymer belongs
   in joint housings, fairings, tendon guides, and brackets, not
   in primary long-bone load paths, unless it is a skin over a
   metal or carbon core.
4. **Thin walls have practical floors the arithmetic ignores.**
   A 0.56 mm steel wall at 30 mm diameter will dent, ovalise
   under a clamp, and buckle locally long before it reaches its
   theoretical bending load; a 0.84 mm carbon wall needs
   off-axis plies for crush and torsion, which raises its mass
   above the 54 g ideal. The numbers rank the materials; they do
   not size the part. Real sizing needs a local-buckling and
   joint check on top.

## 4. Cost at the femur scale

Material cost per femur-length link (450 mm), from the sources
cited — retail/small-quantity, November 2026, before cutting,
machining, bonding, or fasteners:

| Material | Cost basis | Cost per 450 mm femur |
|---|---|---|
| 6061-T6 aluminium tube | 1″ OD × ⅛″ wall round tube, ~$1.42/ft estimated net (Material Price Book, 23 Nov 2026); small-quantity retail typically $2–$8/ft | ~$2–$12 |
| CFRP pultruded uni tube | Rock West 0.393″ OD × 78″ tube at $32.59–$41.99 | ~$8–$10 |
| PLA filament | Budget PLA ~$20 per 2 kg spool | ~$11–$23 of filament for a 1.14 kg solid rod (before print failures) |
| Onyx (Markforged) | $190 per 800 cc spool ≈ $0.24/cc | ~$270 of Onyx for a 1,125 cc solid rod — and that excludes the printer |
| PA12 SLS | Service-bureau pricing, per-part and per-volume; no stable per-cc figure found | Unverified — do not budget from a guess; get a bureau quote per part |

The cost story is the opposite of the mass story: **aluminium is
cheapest, carbon is only ~3–5× aluminium at this size, and printed
polymer is the most expensive way to make a bad femur** — because
the polymer femur needs ~1.1–1.35 kg of material to do a 187 g
metal tube's job, and engineering filament is priced by the
kilogram. Onyx's $190/800 cc spool and continuous carbon fibre at
~$450/150 cc (~$3.00/cc) also mean the Markforged route is gated
by machine access (Mark Two class printers are five-figure
purchases) before material cost even matters [19][20][21][22].

## 5. Repairability and joints

A skeleton that cannot be repaired in the field is a skeleton that
ends the body's service life at the first hard fall. Scored
separately from stiffness:

| Material | Field repair | Joint practice | Failure character |
|---|---|---|---|
| 6061-T6 aluminium | Weldable (TIG); weld zone loses T6 temper and needs re-ageing or a strength knockdown; bolted and machined easily | Tapped holes, bearings, and inserts all native | Yields and dents before fracture — visible damage, graceful degradation |
| Steel | Weldable; heavy but forgiving; cheap to replace | Best bearing and thread behaviour of the set | Yields; true fatigue limit (see §2.2) |
| Ti-6Al-4V | Weldable only with inert-gas discipline; slow to machine; expensive to replace | Excellent where strength per weight at a joint matters | Strong but notch-sensitive; galling at threads without treatment |
| CFRP tube | Not field-repairable in practice — a damaged tube is replaced; bonded joints are permanent | Needs metal inserts or bonded collars for bolts; never tap a composite; bearing loads engage the weak transverse axis | Elastic to failure, then sudden; impact delamination can be invisible — inspect after any knock [14][15] |
| PA12 SLS/MJF | Reprint the part in hours (if a printer/service is at hand); solvent-bonding and adhesives workable | Printed threads are poor; use heat-set inserts or through-bolts | Tough, ductile; fails by gradual deformation |
| Onyx / Onyx + continuous CF | Reprint; continuous-fibre parts reprint at the same machine | Same insert practice as PA12; fibre must be routed around holes, not through them | Matrix-dominated failure modes where unreinforced |
| PLA / PETG FDM | Reprint in hours on a desktop machine — the fastest repair loop of all | Heat-set inserts; printed threads only for light loads | PLA snaps without warning; PETG bends first. PLA creeps under sustained load (§2.2) |

Design rules that follow:

- **Put metal where bearings, threads, and impact live.** Joint
  pivots, motor mounts, and hard points should be aluminium (or
  steel where fatigue dominates) with printed polymer as housings
  and fairings around them — never the other way round.
- **Carbon spars need metal ends.** A carbon tube's job is the
  span between joints; the joint itself is a bonded or clamped
  aluminium collar. Design the collar first, the tube second.
- **Modular boundaries should follow wear boundaries.** The
  research map's standing rule: a part that wears or breaks should
  come off with fasteners, not a saw. That argues for bolted
  aluminium joint blocks + replaceable carbon spars + reprintable
  polymer covers as the default skeleton architecture.

## 6. What real robots chose

- **Poppy (Inria, 2012– ):** 84 cm, ~3.5 kg, 25 Dynamixel
  servos. Structure is laser-sintered polyamide (PA12 class) in
  latticed parts — the lattice is the design answer to §1: when
  the material is soft, use geometry (large, hollow, ribbed
  sections) to buy stiffness back. Total printed-parts cost was
  ~€1,200 of an ~€7,500 build. Poppy proves a small, light robot
  can be all-printed; it does not prove the same architecture
  scales to 100 kg [23][24][25].
- **InMoov (Gaël Langevin, 2012– ):** life-size (~1.8 m),
  fully 3D-printed, PLA recommended, every part fitting a
  12×12×12 cm bed. Around 4 kg of filament for the printed parts,
  ~30 hobby servos. The legs are not motorised — it is a torso,
  arms, and head on a stand, not a walking body. It proves
  desktop PLA can build a life-size *shape*; it does not prove
  PLA can carry a walking body [26][27].
- **Kengoro (University of Tokyo JSK Lab, 2016):** 1.7 m,
  56 kg, 108 motors, 114 DOF. Skeleton is laser-sintered
  aluminium with deliberately varied porosity — the pores carry
  water that seeps out and evaporates, cooling the motors
  (artificial perspiration, ~3× better than air cooling; 11
  minutes of continuous push-ups). The lesson for us is not the
  sweating; it is that **the skeleton can be a multifunctional
  part** — structure plus cooling channels plus tendon routing —
  when the fabrication process (metal powder-bed) allows it
  [28][29]. It is also the most expensive route on this page.
- **Berkeley Humanoid Lite / ToddlerBot (2025):** the current
  open-source walking references. Berkeley Humanoid Lite is
  0.8 m, 16 kg, 22 actuated DOF, with a published parts cost of
  $4,312 and PLA structural parts; ToddlerBot is 0.56 m, 3.4 kg,
  30 active DOF. Both are small enough that printed polymer
  structure works — the scaling question (§3 of the research
  map) is exactly where their architecture stops working
  [27].

## 7. Recommendation for Xynthetix

For Phase 0–2 builds (testbeds, forearms, sub-scale bodies):

1. **Default skeleton: aluminium joint blocks + carbon tube
   spars + printed PA12/Onyx covers.** Aluminium where things
   bolt, bear, or get hit; carbon where a long span must be
   light; printed polymer where the shape is complex and the
   load is low. This is the cheapest architecture that is also
   repairable and honest about each material's weak axis.
2. **Steel only where fatigue rules** — e.g. a joint pin or a
   part that will see millions of cycles at a known stress.
   Never for a stiffness-designed link (no weight saved).
3. **Titanium only for a specific joint that cannot be made
   light enough in aluminium** — it buys strength, not
   stiffness, and it buys it at a machining cost.
4. **No unreinforced printed polymer in a primary load path at
   human scale.** PLA for jigs, mockups, and fit checks; PA12
   for housings and guides; Onyx + continuous fibre only where
   a Markforged-class machine is actually available.
5. **Run the experiment the research map proposes:** print or
   machine one forearm-length segment in three candidate
   materials at equal bending stiffness; publish mass, cost,
   fabrication time, and cycles-to-visible-damage under a
   repeated side-load rig. The §3 numbers predict the ranking;
   the rig measures the caveats (local buckling, joint
   behaviour, creep) that the arithmetic cannot.

## 8. Open questions carried forward

- Skeleton mass fraction for a 100 kg body: the research map
  leaves this open. Poppy's printed structure is a large share of
  a 3.5 kg robot; Kengoro's aluminium skeleton is part of a
  56 kg machine with 108 motors. Neither gives a clean fraction
  for our scale — the worked budget template in the map is the
  tool for this, once actuator masses are fixed.
- Carbon tube joint design: bonded vs clamped collars, and
  measured pull-out / torsion capacity of each, is unresearched
  here. It is the next joint-design item, not this one.
- Long-term CFRP behaviour in a warm, humid, skin-covered body
  (moisture uptake in epoxy, galvanic contact with aluminium
  inserts) is unquantified for our use case.

## Sources

1. ASM Material Data Sheet — Aluminium 6061-T6; 6061-T651.
   http://asm.matweb.com/search/SpecificMaterial.asp?bassnum=MA6061T6
2. Metline — 6061-T6 Aluminium: Temper, Data & Forms.
   https://www.thealuminiumfactory.com/guides/6061-t6-aluminium/
3. Rock West Composites — Tube, Round, Pultruded Uni,
   0.118″ × 0.197″ × 72″ (Toray T700S; EX 19.4 Msi, density
   0.055 lb/in³).
   https://www.rockwestcomposites.com/t-rnd-197-l72.html
4. Rock West Composites — Tube, Plain Weave, High Modulus,
   0.250″ × 0.331″ × 60″ (Toray M40J; composite EX ~16.2 Msi).
   https://www.rockwestcomposites.com/45162-hm.html
5. Materialise — PA 12 (SLS) datasheet (density 0.95 g/cm³,
   tensile modulus 1,650 MPa, tensile strength 48 MPa).
   https://www.materialise.com/en/industrial/3d-printing-materials/pa12-sls
6. Forge Labs — Nylon PA12 / HP High Reusability PA12 MJF
   datasheets (EOS PA 2200: 50 MPa, 1,700 MPa; HP MJF: 50 MPa,
   1,900 MPa both directions; water absorption 0.52–1.33%).
   https://forgelabs.com/3d-printing/materials/nylon-pa12
   and https://forgelabs.com/3d-printing/materials/hp-mjf-pa12
7. Protolabs — PA12 Mineral-Filled (PA620-MF) datasheet
   (E 3,100 MPa XY, tensile 38 MPa, elongation 3%).
   https://www.protolabs.com/services/3d-printing/plastic/nylon/pa12-mineral-filled/
8. Markforged — Composites material datasheet, rev 5.0
   (Onyx: E 2.4 GPa, 40 MPa yield, density 1.2; continuous
   carbon fibre: E 60 GPa, 800 MPa tensile).
   https://static.markforged.com/downloads/composites-data-sheet.pdf
9. PMC — Mechanical properties of 3D-printed PLA/PETG
   (PLA: E 3,600 MPa, 60 MPa; PETG: E 2,200 MPa, 55 MPa;
   Tg 60 °C / 80 °C).
   https://pmc.ncbi.nlm.nih.gov/articles/PMC10880662/table/tb1/
10. Sculpteo — PA12 (SLS/MJF) material data (incl. glass-filled
    PA12: E 3,200 MPa, 51 MPa tensile, 9% elongation).
    https://www.sculpteo.com/en/materials/pa12/
11. Aerospace Metals — Titanium Ti-6Al-4V (Grade 5), STA bar
    data sheet (density 4.43 g/cm³, E 114 GPa, yield 965 MPa,
    fatigue 700 MPa at 10⁷ cycles).
    https://www.aerospacemetals.com/wp-content/uploads/2023/07/Titanium-Ti-6Al-4V-Grade-5-STA-Bar-Data-Sheet.pdf
12. Morgan et al. — Bone Mechanical Properties in Healthy and
    Diseased States, *Annual Review of Biomedical Engineering*
    2018 (human femoral cortical bone: E ~17.9 GPa longitudinal,
    tensile yield ~72 MPa, compressive ultimate ~205 MPa).
    https://pmc.ncbi.nlm.nih.gov/articles/PMC6053074/
13. Element6 Composites — Carbon Fiber vs. Aluminum vs. Steel
    vs. Fiberglass (steel endurance limit ~40–50% UTS;
    aluminium has no endurance limit; CFRP fibre-direction
    fatigue behaviour).
    https://element6composites.com/carbon-fiber-vs-aluminum-vs-steel-vs-fiberglass/
14. DifferenceBetweenZ — Aluminum vs Carbon Fiber (aluminium
    isotropic and predictable; CFRP anisotropic; aluminium
    yields before fracture, CFRP fails suddenly).
    https://differencebetweenz.com/difference-between-aluminum-and-carbon-fiber/
15. NASA NTRS — A damage tolerance comparison of 7075-T6
    aluminium alloy and IM7/977-2 carbon/epoxy (composite
    specific strength ~2× aluminium undamaged; sharp drop after
    2.6 J impact; damaged composite fatigue life ~17×
    undamaged aluminium).
    https://ntrs.nasa.gov/citations/19920027567
16. LayerCraftLog — Will PLA Filament Prints Deform Under
    Sustained Load? (1,000 h creep at 23 °C / 25 MPa: PLA
    0.41–1.35% strain by brand; ABS ~0.18%; nylon 6/6 ~0.11%;
    annealing at 60 °C cuts PLA creep ~75%). Hobby-lab test,
    not peer-reviewed — treat as indicative.
    https://www.layercraftlog.com/filaments/will-pla-filament-prints-deform-under-sustained-load
17. arXiv — Effect of physical aging on the flexural creep in
    3D printed thermoplastic (non-negligible PLA creep over
    long periods even well below Tg).
    https://ar5iv.labs.arxiv.org/html/2302.11240
18. Nebulas-X — Properties of 3D printing and CNC materials
    (PLA interlayer adhesion ~17 MPa vs 50–59 MPa in-plane;
    PETG ~18 vs 46–50 MPa).
    https://nebulas-x.com/choose/material-properties/
19. Material Price Book — Aluminium 6061-T6 round tube prices,
    estimated net as of 23 Nov 2026 (¾″ OD × ⅛″ wall ~$4.03/ft;
    1″ OD × ⅛″ wall ~$1.42/ft).
    https://www.materialpricebook.com/prices/aluminum/6061/round-tube/0.75x0.125
20. OnlineMetals — 6061-T6 drawn round tube listings
    (1″ OD × 0.125″ wall drawn tube listed at $34.02 per piece,
    quantity pricing to 4+).
    https://www.onlinemetals.com/en/buy/aluminum-round-tube-6061-t6-drawn?page=3&pagesize=25&q=:size&sort=size
21. Hawkridge Systems — How Much Does a 3D Printer Cost?
    2026 price guide (Onyx ~$190/800 cc spool; continuous
    carbon fibre ~$450/150 cc spool; Onyx Pro from $8,990).
    https://hawkridgesys.com/blog/3d-printer-cost
22. Mecanica Solutions — Economics of 3D Printing (Markforged:
    Onyx $190/800 cc = $0.24/cc; carbon fibre $150/50 cc =
    $3.00/cc).
    https://preprod.mecanicasolutions.com/wp-content/uploads/2021/10/MF_Economics-of-3D-Printing.pdf
23. Humanoid.Pub — Poppy Humanoid specs (84 cm, ~3 kg, 25 DOF,
    open-source, SLS polyamide structure).
    https://www.humanoid.pub/en/robots/poppy-humanoid
24. Lapeyre et al. — Poppy Humanoid platform paper (84 cm,
    3.5 kg; printed parts ~€1,200 of ~€7,500 build; latticed
    SLS polyamide structure).
    https://www.researchgate.net/figure/Human-proportion-used-for-the-design-of-Poppy-9_fig1_261352960
25. Poppy Project — Open-Source Fabrication of 3D Printed
    Humanoid Robot for Science, Education and Art, Digital
    Intelligence 2014.
    https://lacuna.tiptreesystems.com/pdf/art_d15088bfdb66fbeb7a4d489a255a583c
26. Humanoid.Press — InMoov, open-source 3D-printed life-size
    humanoid (PLA, 12×12×12 cm bed, ~1.8 m).
    https://humanoid.press/database/humanoid-press-database-inmoov/
27. Offbrand Human — Open-source humanoid robots you can
    actually build, with real parts costs (Berkeley Humanoid
    Lite: 0.8 m, 16 kg, $4,312 parts, PLA structure; ToddlerBot:
    0.56 m, 3.4 kg; InMoov: ~4 kg filament, legs not motorised).
    https://www.offbrandhuman.com/blog/open-source-humanoid-robots-you-can-build
28. IEEE Spectrum — This Robot Can Do More Push-Ups Because It
    Sweats (Kengoro: 1.7 m, 56 kg, 108 motors; laser-sintered
    porous aluminium skeleton; perspiration cooling ~3× air
    cooling; 11 minutes of push-ups).
    https://spectrum.ieee.org/this-robot-can-do-more-pushups-because-it-sweats
29. Wevolver — Kengoro specs (114 DOF, 100 W brushless motors,
    muscle fidelity 49.1%).
    https://www.wevolver.com/specs/kengoro
30. JJ Mobility — Frame Materials Compared: Carbon Steel vs
    Aluminium vs Carbon Fiber (A36 steel ~250 MPa yield at
    7.85 g/cm³; aluminium no fatigue limit; CFRP impact
    delamination risk).
    https://www.jj-mobility.com/en/news/frame-materials-steel-aluminum-carbon-fiber
31. Body plan research map (this repo) — subsystem decomposition
    and the open question this note answers.
    [body-plan-research-map.md](body-plan-research-map.md)

*Typical values, not design minimums. Verify against the mill
certificate or datasheet of the exact grade and form before
designing to any number on this page.*
