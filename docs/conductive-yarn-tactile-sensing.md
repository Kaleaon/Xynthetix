# Conductive Yarn Options for Tactile Sensing — Resistance, Wash/Flex Behaviour, Sourcing

**Date:** 2026-11-27
**Status:** Research survey v1.0 — companion to
`sensing-proprioception-survey.md`, `sensor-layer-spec.md`,
`braided-mesh-integration.md`, and `yarn-shortlist-first-sleeves.md`
**Scope:** Commercially buyable conductive yarns and published yarn-level
sensor data, judged against one job: tactile sensing in a braided synthetic
body. Every resistance figure below comes from a manufacturer listing, a
datasheet value reproduced in a peer-reviewed paper, or a measurement in
that paper. Where a number is derived from published values, the derivation
is shown and labelled as derived. Prices are single-unit retail listings
checked 2026-11-27 and are dated as such.

## Key findings (up front)

1. **Silver-coated nylon is the sensing yarn; stainless steel is the wiring
   yarn.** The only yarn-level electromechanical characterisation in the
   literature (Statex/Madeira silver-plated polyamide, Mersch et al. 2023)
   gives gauge factors of 5–22 and usable strain ranges of 4–12% — real
   sensor behaviour. Stainless thread is far more stable and washable, but
   the same literature finds steel yarns unsuitable as strain sensors
   because the base fibre barely stretches.
2. **The resistance spread across buyable yarns is roughly 30 Ω/m to
   250 kΩ/m — four orders of magnitude — so the yarn choice is really a
   readout choice.** Silver-coated nylon sits at 300–1,500 Ω/m; stainless
   thread at 33–92 Ω/m; PEDOT:PSS-coated yarns at ~10 kΩ/m (wet-spun
   composite) to ~250 kΩ/m (dip-coated sisal). A voltage-divider readout
   that works for one family is unusable for another.
3. **Silver's weakness is not flex — it is washing, specifically bleach.**
   After 30 delicate machine cycles, silver-plated nylon electrodes washed
   with bleach-containing powder detergent lost so much silver that their
   resistance exceeded 10 MΩ; the same electrodes in bleach-free liquid
   detergent stayed measurable but with significantly increased resistance
   (Gaubert et al. 2020). Sweat alone degrades silver-coated nylon too:
   six sweat/wash/dry cycles cut a knitted antenna's radiation efficiency
   from 32.7% to 24% (Zaman et al. 2020). A body that sweats (or is washed)
   cannot treat silver yarn as a fit-and-forget conductor.
4. **Drift, not sensitivity, is the problem with silver yarn sensors.**
   Gauge factors of 9–22 look excellent until you read the drift column:
   19–64% of the signal is non-recoverable after ten load cycles, and
   reproducible behaviour only starts above ~4% strain. Any tactile design
   using bare silver yarn as the sensing element needs per-taxel baseline
   tracking and a pre-strain or a working range that starts above 4%.
5. **Braiding is a published sensor route, and the newest braided sensors
   are extremely sensitive — but they are lab builds, not buyable yarns.**
   A 2025 three-dimensional braided strain sensor (polyurethane filaments
   dip-coated with carbon nanotubes and graphene) reports a gauge factor
   of 340 at 280% strain. That is the direction for high-sensitivity
   braided sensing; it is not a product yet.
6. **Two gaps dominate the buying decision.** No public Ω/m figure could be
   found for Bekaert Bekinox stainless yarns or for Shieldex 235/36, and no
   published flex-cycle lifetime exists for silver-plated yarns used as
   conductors (only 10-cycle sensor characterisations). Both are cheap
   experiments to run ourselves and are listed as G1–G2 in §11.

---

## 1. What the yarn has to do

A tactile skin built into a braided body asks a yarn to play up to three
roles, and the roles pull in opposite directions:

- **Conductor** — carry a signal or a small current from a taxel to the
  readout with negligible loss and negligible change under movement.
  Wants: low, stable resistance; no strain sensitivity at all.
- **Sensing element** — change resistance (or capacitance) predictably
  with stretch or pressure. Wants: high, repeatable, low-drift gauge
  factor; a working range that starts at zero strain.
- **Capacitive electrode** — form one plate of a capacitive taxel, where
  the yarn's own resistance matters only insofar as it must be low enough
  not to dominate the CDC measurement. Wants: low resistance, insulation
  from neighbouring conductors, and no strain sensitivity.

No single yarn is best at all three. The practical split, supported by
everything below, is: **stainless steel for wiring, silver-coated nylon
for sensing elements, insulated silver yarn (TPU-sheathed) for capacitive
electrodes** — with PEDOT:PSS-coated yarns as the high-resistance,
all-polymer alternative where metal is unwanted.

The sensor-layer spec (`sensor-layer-spec.md`) already fixes the electrical
architecture: 3.3 V logic rail, digitisation at the patch, event-driven
reporting. This document answers only the yarn question inside that
architecture: which yarn, at what resistance, with what failure modes.

## 2. Candidate yarns

### 2.1 Silver-coated nylon (polyamide 6.6) — Shieldex / Statex, Madeira

The most-studied conductive yarn family in e-textiles. Statex
Produktions- und Vertriebs GmbH sells it under the Shieldex brand; Madeira
Garnfabrik sells a refined embroidery version (HC 40). The base fibre is
high-tenacity polyamide 6.6 with a 99.9% pure silver coating; Shieldex
states its silver-plated yarns "can be twisted, knitted, embroidered,
woven and spun like uncoated yarns" and lists sensors, heating and
electrodes among the applications [1][2]. The catalogue runs from 44/10
dtex up to 235/36 in single, plied (×2, ×4, ×6) and high-conductive (HC)
variants, plus wrapped, stretch, and TPU-insulated constructions [1].

The hard numbers come from Mersch et al. (2023), who bought four
commercial yarns and measured them on a tensile tester with synchronous
four-wire resistance measurement (DIN EN ISO 2062) [8]:

| Yarn | Construction | Linear density | Base resistance |
|---|---|---|---|
| Shieldex S117 | 117/17 dtex, 2-ply, plain silver | 280 dtex | **1,500 Ω/m** |
| Shieldex HCB | 117/17 dtex, 2-ply, extra silver layer + silicone-oil protective coating (B) | 295 dtex | **300 Ω/m** |
| Shieldex TPU | 117/17 dtex, 2-ply HCB + thermoplastic polyurethane insulating sheath (92% of yarn weight, 250 µm thick) | 3,000 dtex | **300 Ω/m** |
| Madeira HC 40 | refined HCB-type, embroidery-grade finish | 290 dtex | **300 Ω/m** |

Two things to notice. First, the extra silver layer in the HC variants
buys a 5× resistance reduction (1,500 → 300 Ω/m) for a 5% mass penalty —
the plain S117 is a poor buy for any new design. Second, the TPU sheath
costs a 10× mass penalty (3,000 dtex) for the same 300 Ω/m: it is an
insulated cable, not a yarn, and Mersch et al. note it "severely limits
the processability in, for example, knitting or embroidery" [8].

Amann & Söhne's competing silver yarn, Silver-tech + 150 (PA 6.6,
220 dtex), is quoted at **<300 Ω/m** in the knitted-sensor study that
used it (Warncke et al. 2023) [9] — consistent with the HCB figure, and
a useful second source for the ~300 Ω/m class.

**No public Ω/m figure was found for Shieldex 235/36** (the heavier yarn
in the same catalogue) or for the 78/20 and 44/10 grades; the Shieldex
shop, which would carry datasheets and prices, returned HTTP 403 to
every fetch during this research. Gap G1.

### 2.2 Stainless steel fibre thread — Adafruit, SparkFun, Bekaert Bekinox

Stainless thread is spun from 316L stainless steel fibres (Adafruit) or
stainless fibres generally (SparkFun, Bekaert). It is the stable,
washable, non-oxidising option — Adafruit's listing states it "will not
oxidize like silver does" and is "safe to wash", while warning it feels
stiff, "a little like waxed thread" [3][4].

| Product | Construction | Resistance (listed) | Resistance (Ω/m) | Price, 2026-11-27 |
|---|---|---|---|---|
| Adafruit 640 | 316L stainless, 2-ply, 0.2 mm | 16 Ω/ft (1.3 Ω/in) | **52.5** | $6.95 / 23 m ($0.30/m) |
| Adafruit 641 | 316L stainless, 3-ply, 0.25 mm | 10 Ω/ft (0.83 Ω/in) | **32.8** | $9.95 / 18 m ($0.55/m) |
| SparkFun DEV-11791 | stainless fibres, no nylon core | 28 Ω/ft | **91.9** | $82.75 / 60 g spool, ~360 yd (~329 m, $0.25/m) |
| Adafruit 603 | 316L stainless, thick yarn / thin thread, 30 ft | not published | — | $4.50 / 9.14 m ($0.49/m) |
| Adafruit 1088 | loose 316L fibre, 20 µm, 10 g | not published (fibre, not yarn) | — | $2.95 / 10 g |

Sources: Adafruit product pages [3][4][5][6]; SparkFun product page [7].
Conversions: Ω/m = Ω/ft × 3.28084. Adafruit rates the 2-ply for loads
under ~50 mA and the 3-ply under ~100 mA [3][4].

Bekaert's Bekinox is the industrial end of this family: stainless steel
fibres and yarns, 100% stainless or blended with cotton and polyester,
sold for e-textiles with claims of high corrosion resistance, long
flex-life, and garments that "can be washed numerous times without
losing their specific characteristics" [19][20]. **No Ω/m, linear density,
or price is published on Bekaert's public pages or in its smart-textiles
product sheet** — the sheet is marketing-level only. Bekinox is therefore
unverifiable as a purchase until a datasheet is requested from Bekaert
directly. Gap G1 again.

SparkFun adds a handling note that matters for braiding: its stainless
thread is "somewhat 'hairy'" and the hairs "could potentially short
across small distances" in machine sewing; hand-sewing users are advised
to wax it [7]. A hairy conductor inside a braided sleeve is a short
waiting to happen — see §7.

Adafruit 1088 (loose 20 µm stainless fibre) is worth a line because it
demonstrates the contact mechanism in its purest form: Adafruit notes
the fibre "becomes less resistive the more you squeeze the fibers
together" and suggests it for squeeze/pressure sensors and felt touch
buttons [6]. That is a piezoresistive contact sensor with no polymer and
no coating to degrade — crude, but nearly indestructible.

### 2.3 Carbon yarns and carbon-loaded coatings

Carbon appears in this space in three distinct forms, which must not be
confused:

- **Carbon fibre tow** (structural carbon, e.g. 1K–12K tow). Very strong,
  very stiff, electrically conductive, but brittle in bending and
  essentially un-braidable as a bare tow at small radii. No buyable
  carbon yarn with a published Ω/m datasheet was found in this pass
  (Gap G4). Tibtech, which sells carbon heating yarns, warns that carbon
  yarn resistivity *decreases* with temperature — the opposite of metals —
  so a damaged or thinned spot gets more conductive as it heats, which
  "may induce an acceleration of the damage through eventual hot spots",
  while metallic yarns self-regulate slightly because their resistivity
  rises with temperature [17].
- **CNT/graphene-coated braided sensors** (lab builds). The strongest
  recent result is Zhang et al. (2025): a three-dimensional braided
  strain sensor built on polyurethane filaments, dip-coated with carbon
  nanotubes (long-range conduction) and graphene nanoplatelets (fast
  resistance change by interlayer sliding), reporting a gauge factor of
  **340 at 280% strain** and a peak sensitivity of **1,152 at 180%
  strain**, with braiding angle and yarn arrays used to tune geometry
  [12]. This is the proof that braiding itself can be the sensor
  architecture — but it is a fabrication paper, not a product: no yarn
  is sold, no wash data, no cycle life.
- **CNT-sheathed pressure yarns** (lab builds). Qi et al. (2020) wove a
  textile pressure sensor from a core-sheath nanofibre yarn — a
  nickel-coated cotton yarn core with a CNT-embedded polyurethane
  nanofibre sheath — reporting sensitivity **16.52 N⁻¹**, a sensing range
  of **0.003–5 N**, and response time **~0.03 s** [14]. Again a lab build,
  but it shows the sensitivity a yarn-structure pressure sensor can
  reach, two orders of magnitude below the force range of a fingertip
  press.

### 2.4 PEDOT:PSS-coated yarns — the all-polymer option

PEDOT:PSS (poly(3,4-ethylenedioxythiophene):poly(styrenesulfonate)) is
the conductive polymer of choice for coating yarns. Two published yarns
bracket the range:

- **Wet-spun SWCNT/PEDOT:PSS/sodium-alginate composite yarn** (2025):
  ~290 µm diameter, tensile strength 151 MPa, breaking strain 12.7%,
  Young's modulus 0.26 GPa, electrical conductivity **15.3 S/cm**
  [13]. Derived resistance per metre: cross-section
  π(145 µm)² ≈ 6.6×10⁻⁸ m²; σ = 1,530 S/m; R/m = 1/(σ·A) ≈
  **≈10 kΩ/m** (derived, not measured). A lab material, but the only
  PEDOT yarn with both conductivity and mechanics published together.
- **Dip-coated sisal/PEDOT:PSS sensor yarn** (2021): a PVA-impregnated
  sisal core (2.6 mm diameter) with 2–5 dip-coated PEDOT:PSS layers.
  Conductivity rises from **0.177 S/m (2 layers) to 0.752 S/m
  (4 layers)** past a pseudo-percolation threshold, with gauge factors
  of **0.42 (0–2.5% strain) and 3.98 (4.5–7% strain)** at four layers
  [15]. Derived resistance per metre at four layers: A ≈ 5.3×10⁻⁶ m²;
  R/m = 1/(0.752 × 5.3×10⁻⁶) ≈ **≈250 kΩ/m** (derived). Usable as a
  strain sensor, but at a quarter of a megaohm per metre it needs a
  high-impedance readout and is very sensitive to moisture — the authors
  note PEDOT:PSS is "well known to have more sensitivity to moisture
  hydration" [15].
- **Knitted PU/PEDOT:PSS fibre textiles** (Seyedin et al. 2015): the
  earliest scaled wet-spinning demonstration; knitted textiles with
  gauge factor rising with the number of conductive fibres co-knitted,
  stable cyclic response at strains up to **160%**, demonstrated in a
  knee sleeve with a wireless transmitter [16]. No Ω/m published in the
  abstract; the value here is the durability signal — an all-polymer
  sensor surviving 160% cyclic strain, far beyond silver nylon's 12%.

PEDOT yarns are the right answer where metal is unwanted (MRI-adjacent
work, all-polymer skins, very high strain), and the wrong answer where
low resistance or moisture stability matters.

### 2.5 Copper-core yarns

Copper is the best conductor of the group and the least documented as a
yarn. Shieldex's own homepage lists copper among the metals it
metallises textiles with (silver, copper, nickel, tin) [21], and Tibtech
sells copper-based heating and conductive yarns [17][18] — but **no
copper yarn with a published Ω/m, linear density, or price was found in
this pass**. Copper's known failure mode (rapid oxidation and
verdigris in sweat and air, worse than silver's tarnish) makes it a
poor default for a skin that is handled and sweated on, and there is no
published wash-cycle study of a copper yarn to check that against.
Copper stays a gap (G5) until a datasheet is in hand; do not design
around it.

---

## 3. Comparison table

Resistance per metre, strain behaviour, wash behaviour, and braidability
in one place. "—" means not published / not found, not zero.

| Yarn | R/m | Strain sensing (gauge factor) | Drift / hysteresis | Wash behaviour | Braidability |
|---|---|---|---|---|---|
| Shieldex S117 (Ag/PA, 280 dtex) | 1,500 Ω/m | 4.5 @4% → 16.1 @12% | drift 42–64% | bleach kills it (see §5) | knits/braids like uncoated yarn [1] |
| Shieldex HCB (Ag/PA, 295 dtex) | 300 Ω/m | 5.2 @4% → 15.3 @12% | drift 25–39% | bleach kills it (see §5) | as S117; silicone-oil coat |
| Madeira HC 40 (Ag/PA, 290 dtex) | 300 Ω/m | 8.7 @4% → 22.3 @12% | drift 19–29% | bleach kills it (see §5) | embroidery-grade finish [8] |
| Shieldex TPU (Ag/PA + TPU sheath, 3,000 dtex) | 300 Ω/m | 6.4 @4% → 11.7 @12% | drift 27–32% | sheath protects; untested | poor — sheath "severely limits" knitting/embroidery [8] |
| Amann Silver-tech + 150 (Ag/PA, 220 dtex) | <300 Ω/m | knitted sensor GF 2.4 (system-level) | system drift 50%, hysteresis 12.5% [9] | as silver-coated nylon | knitted in study [9] |
| Adafruit 640 (316L, 2-ply) | 52.5 Ω/m | not a strain sensor (steel barely stretches) | low (vendor: stable) | vendor: safe to wash, no oxidation [4] | stiff, waxed feel; machine-sewable |
| Adafruit 641 (316L, 3-ply) | 32.8 Ω/m | as 640 | low | as 640 [3] | as 640 |
| SparkFun DEV-11791 (stainless) | 91.9 Ω/m | as 640 | low | stainless; vendor silent on cycles | hairy — shorting risk in close work [7] |
| Bekaert Bekinox (stainless) | — (not published) | — | vendor: long flex-life [19] | vendor: "washed numerous times" (no count) [19] | sold for embroidery/weaving/knitting [19] |
| SWCNT/PEDOT:PSS/SA composite yarn | ~10 kΩ/m (derived) | not reported as strain sensor | — | — | lab material only |
| Sisal/PEDOT:PSS, 4 layers | ~250 kΩ/m (derived) | 0.42 @0–2.5%; 3.98 @4.5–7% | stable cyclic response reported [15] | moisture-sensitive [15] | lab material only |
| 3D-braided CNT/GNP sensor (lab) | — | 340 @280%; peak 1,152 @180% [12] | — | — | **is** a braid |
| Ni-coated cotton / CNT-PU pressure yarn (lab) | — | 16.52 N⁻¹, 0.003–5 N, ~0.03 s [14] | — | — | woven in study |

## 4. Resistance under stretch and flex

### 4.1 Silver-coated nylon: high gauge factor, high drift

Mersch et al.'s four-yarn characterisation is the only yarn-level dataset
with gauge factor, drift, and modulus together, so it carries this
section [8]. Ten load/unload cycles per strain level, 4–12% strain in
2% steps, 0.83%/s:

| Yarn | GF @4% | GF @6% | GF @8% | GF @10% | GF @12% | Drift @8% |
|---|---|---|---|---|---|---|
| S117 | 4.45 | 8.93 | 12.3 | 14.5 | 16.1 | 42.4% |
| HCB | 5.2 | 8.8 | 11.6 | 13.7 | 15.3 | 25.2% |
| HC 40 | 8.7 | 14.7 | 18.6 | 21.0 | 22.3 | 20.6% |
| TPU | 6.4 | 8.2 | 9.7 | 10.8 | 11.7 | 27.3% |

Three structural facts explain the numbers, and all three matter for
design:

1. **Gauge factor rises with strain** because deformation starts as
   structural (fibres straightening and sliding, changing fibre-to-fibre
   contact) and only later becomes material (the polyamide and its
   silver coating actually stretching). Contact-dominated resistance
   change is frictional and partly non-recoverable — which is why drift
   is worst at low strain [8].
2. **Reproducible behaviour only starts at ~4% strain.** Below that the
   signal is dominated by settling and, for bare S117, by spurious
   resistance peaks at the relaxed end of each cycle [8]. A tactile
   sensor that must resolve a light touch from zero strain cannot use
   bare silver yarn directly; it needs pre-strain, a working range
   floored at ~5%, or a different transduction mechanism (capacitive,
   §6).
3. **Coatings help, but modestly.** The extra silver layer plus
   silicone-oil coat (HCB) removes the zero-strain peaks and roughly
   halves drift versus bare S117; the embroidery-grade HC 40 is the best
   of the four on both gauge factor and drift [8]. The TPU sheath
   homogenises the response (flattest gauge-factor curve, most stable
   drift) at the cost of 10× mass and lost processability.

At system level, Warncke et al.'s knitted piezoresistive sensors (Amann
Silver-tech + 150 plated with elastic yarn) achieved GF **2.4**, drift
**50%**, hysteresis **12.5%**, nonlinearity **0.3%** — and the authors
state explicitly that steel-based yarns were *less* suitable for strain
sensors than silver-plated polyamide because of their low stretchability
[9]. The yarn-level gauge factor does not survive integration into a
knit: the structure dominates. Budget for system GF ≈ 2–3, not 15–22,
when the yarn is knitted or braided rather than pulled straight.

### 4.2 Stainless steel: stable, and therefore not a sensor

No published gauge-factor data was found for stainless thread, which is
itself informative: the material's selling point is stability. Steel
fibres stretch ~1% before yielding, so a stainless yarn's resistance
barely moves under the strains a skin sees — exactly what a conductor
wants and exactly what a strain sensor does not. Treat stainless as a
wire, and do not expect it to sense.

### 4.3 Flex-cycle lifetime: the missing number

Mersch et al. ran **10 cycles per strain level**. Warncke et al. ran
multi-cycle knitted tests but report drift/hysteresis, not a cycle life.
The sensing survey (`sensing-proprioception-survey.md`) already flagged
that published textile tactile lifetimes run 10⁴–10⁵ cycles versus the
10⁶+ a body needs. **No study found in this pass measures the resistance
of a silver-plated yarn as a conductor over thousands of flex cycles.**
That is the single most important unmeasured quantity for our programme:
a conductor that drifts 20–60% in ten cycles may or may not settle, and
we do not know which. Gap G2, and the cheapest decisive experiment in
§11.

## 5. Washing and sweat

### 5.1 Machine washing destroys silver — if bleach is involved

Gaubert et al. (2020) is the definitive study: silver-plated nylon
electrodes (three suppliers' yarns, knitted) machine-washed on a
delicate 30 °C cycle, 400 rpm spin, with 1.8 kg of everyday clothes,
for up to 30 cycles, in four detergent regimes — powder with bleach,
bleach-free liquid, tap water only, and sodium percarbonate (bleach)
alone [10]. Results:

- **Bleach is the killer, not the machine.** Powder detergent's bleaching
  agents oxidise the silver layer, making it vulnerable to the
  mechanical rubbing that then tears it off, wash after wash. With
  percarbonate alone, resistance exceeded the 10 MΩ meter range after
  **20 washes, for every yarn**. With powder detergent, only one of
  three yarns was still measurable after 30 washes.
- **Liquid, bleach-free detergent is survivable but not free.** All
  samples stayed measurable after 30 washes, but sheet resistance rose
  significantly (worst for one of the three yarns, which also degraded
  in tap water alone).
- **Silver is physically lost, not just oxidised.** XPS of a
  powder-washed electrode after 30 cycles: surface silver 18.0% →
  9.0%; percarbonate-washed: 1.1% remaining, 7% of the reference. Some
  silver chloride forms (chlorine 0.5% → 2.2%), but the dominant
  mechanism is the silver layer being rubbed off.
- **A visible proxy exists:** darkening of more than ~10% in lightness
  (L*) predicts resistance above 10 MΩ. A darkened silver yarn is a dead
  yarn; colour is a usable field check.

Practical rules for our programme: **never bleach; wash only in
bleach-free liquid detergent; design silver conductors as replaceable
consumables, not permanent infrastructure; and treat any silver yarn
that has darkened visibly as failed.** Note the study's electrodes were
knitted fabric, not braided sleeves — a braided sleeve buries the yarn
under crossings and may protect it somewhat, or may abrade it worse.
Unverified either way (Gap G3).

### 5.2 Sweat

Zaman et al. (2020) immersed knitted silver-coated nylon transmission
lines in artificial sweat (EN 1811: NaCl 5.0 g/L, lactic acid 1.0 g/L,
urea 1.0 g/L, pH 6.5) for seven days, with a wash-and-dry cycle every
24 h [11]. Sheet resistance rose with every cycle — the authors
attribute it to the silver coating delaminating from the nylon under
sweat, washing, and drying. A bellyband antenna built from the same
fabric lost radiation efficiency from **32.7% to 24%** over six cycles,
a 10% read-range loss. Sweat is a slower bleach: same direction, same
mechanism, no detergent required. A body that sweats needs its silver
either coated (HCB's silicone-oil layer helps; the TPU sheath helps
more) or replaced by stainless for any conductor that must last.

### 5.3 Vendor wash claims, and how much to trust them

- Bekaert (Bekinox): "washed numerous times without losing their
  specific characteristics" [19]. No cycle count, no detergent, no
  resistance data. A claim, not evidence.
- Adafruit (stainless thread): "safe to wash", "will not oxidize like
  silver does" [3][4]. Consistent with stainless metallurgy and with
  the absence of a coating to lose, but still a vendor claim without
  cycle data.
- Shieldex: no wash-cycle data on the public pages read. The
  silicone-oil B coating on HCB exists specifically "to reduce external
  influences" [8] — a tacit admission that the bare coating needs
  protection.

## 6. Sensing mechanisms — which yarn for which transduction

### 6.1 Piezoresistive (resistance changes with strain/pressure)

The mechanism behind every silver-yarn and PEDOT-yarn strain sensor
above: stretch changes fibre-to-fibre contact and then coating strain,
so resistance rises with strain (GF 2–22 for silver, 0.4–4 for PEDOT
sisal, up to 1,152 for the lab CNT/GNP braid). Best for: joint-angle and
stretch sensing over a known range, where a 4–12% working window is
acceptable and baseline drift can be tracked out in software. Worst
for: absolute pressure measurement, light touch from rest, and anything
needing calibration stability over weeks — drift of 20–60% per ten
cycles rules that out without continuous re-baselining.

### 6.2 Capacitive (yarn as electrode)

A capacitive taxel needs the yarn only to be conductive enough that its
resistance does not swamp the capacitance measurement, and insulated
enough not to short to its neighbour. The textile capacitive review
(Mei et al. 2022) divides devices into sandwich, yarn-structure, and
in-plane forms, and finds yarn-structure devices the most wearable and
comfortable — but their performance "needs further improvement" versus
sandwich structures [22]. Shieldex itself lists capacitive sensors
among the applications for its yarns [2], and Mersch et al. note the
TPU-insulated yarn is usable "as an electrode in capacitive-type strain
sensors" precisely because the sheath insulates it [8]. A 2026 study
using sparse soft capacitive tactile sensors on a robotic hand reached
95.4% size-invariant shape recognition across 12 objects, showing the
approach works for robot hands with few sensors and low wiring [23].

Worked example: a 1 cm² taxel with a 1 mm silicone dielectric
(εr ≈ 3) has C = ε₀·εr·A/d ≈ 8.85×10⁻¹² × 3 × 10⁻⁴ / 10⁻³ ≈
**2.7 pF**. That is squarely in the range of the AD7147 CDC our sensor
spec already uses, and a yarn electrode at 300 Ω/m contributes
negligible series resistance at these capacitances. Capacitive sensing
is also the mechanism that sidesteps silver's drift problem entirely:
the yarn is not the sensor, the dielectric gap is.

### 6.3 Contact / squeeze (resistance falls with pressure)

Two conductors pressed together make more contact area, so resistance
falls. Adafruit's loose stainless fibre demonstrates it directly
("becomes less resistive the more you squeeze the fibers together")
[6], and Qi et al.'s core-sheath yarn uses the same physics at
nanofibre scale to reach 0.003 N detection [14]. Best for: binary touch
and grip-force thresholds, where a simple comparator beats a calibrated
analogue chain. The failure mode is the obvious one: anything that
holds the conductors apart (a stiff braid, a thick skin layer) kills
sensitivity, and anything that holds them together (a kink, a snag)
reads as a permanent press.

## 7. Braidability — what the braiding programme needs to know

Our braiding programme (`yarn-shortlist-first-sleeves.md`,
`braid-spec.md`, `braided-mesh-integration.md`) braids structural
yarns on a maypole machine. Conductive yarns enter that programme in
two ways: as carriers in the braid itself, or as sensing elements laid
into/onto a braided sleeve. What this research says about each:

- **Silver-coated nylon braids like ordinary nylon.** Shieldex states
  its yarns process like uncoated yarns [1], and the 3D-braided sensor
  literature braids conductive-coated filaments directly [12]. The
  risk is not processability but **abrasion of the silver coating at
  carrier crossings and horn-gear contact**: the same rubbing that
  strips silver in a washing machine (Gaubert et al. [10]) happens
  continuously inside a braid under cyclic load. No published
  braid-abrasion data for silver yarn exists (Gap G3). The HCB's
  silicone-oil protective coat is the cheapest mitigation; the TPU
  sheath is the strongest, at 10× mass.
- **Stainless thread is a poor braiding yarn.** It is stiff, springy,
  and hairy: SparkFun warns the hairs can short across small distances
  [7], and Adafruit calls it stiff and waxed-feeling [3]. In a braid,
  hairs become inter-carrier shorts, and stiffness fights the tight
  radii at the braid point. Use stainless as straight laid-in wiring
  (or as a served/covered yarn), not as a braiding carrier — and if it
  must be a carrier, wax it or cover it, and keep conductor spacing
  generous.
- **TPU-insulated silver yarn is an insulated cable in yarn form.**
  3,000 dtex, 250 µm sheath, 92% of its mass is insulation [8]. It will
  not short to its neighbours, which is exactly what a capacitive
  electrode or a power conductor inside a braid wants — but it will
  fight every tight bend, and Mersch et al. warn it "severely limits"
  knitting and embroidery [8]. Reserve it for electrode runs, not for
  the braid body.
- **Friction matters and is unmeasured for conductive yarns.** The
  sleeve shortlist (`yarn-shortlist-first-sleeves.md`) leans on
  fibre–fibre friction (notably UHMWPE's μ ≈ 0.05 making braids walk).
  No friction coefficient was found for any silver-coated or stainless
  yarn. Silver-on-silver and steel-on-steel friction at crossings will
  decide whether a conductive braid holds its angle or walks — measure
  it before committing a braid design (Gap G6).
- **A conductive braid is a parallel circuit.** Worked example (§8.3):
  a 1 m sleeve braided from 16 carriers of HCB at 45° has each carrier
  running ~1.41 m; if all carriers are conductive and bonded at both
  ends, the sleeve end-to-end is ~26 Ω. That is a feature (low
  resistance, redundancy — one broken carrier barely matters) and a
  hazard (a single short anywhere couples the whole sleeve). Design
  conductive braids with the assumption that carriers touch.

## 8. Worked numbers

All derivations use the figures cited above; "derived" marks arithmetic
done here, not a published measurement.

### 8.1 Lead resistance and readout sizing

A 20 cm run of HCB (300 Ω/m) is 60 Ω; the same run of S117 (1,500 Ω/m)
is 300 Ω; of Adafruit 641 (32.8 Ω/m) is 6.6 Ω. Against a 10 kΩ
pull-up in a 3.3 V divider, even the S117 lead shifts the divider by
3% — acceptable. Against a 100 Ω reference resistor, the S117 lead
dominates the measurement. **Rule: keep divider reference resistors at
least 10× the worst-case lead resistance, or use four-wire (Kelvin)
sensing for any silver-yarn measurement**, as both Mersch et al. and
Warncke et al. did in the lab [8][9].

At a 1 mA sense current, a 60 Ω HCB lead drops 60 mV and dissipates
60 µW — negligible self-heating. At 5 V across a 10 cm HCB length
(30 Ω), dissipation is 0.83 W: enough to feel warm and to cook a
silicone skin locally. Never put rail voltage across a short yarn
length; sense with current-limited, low-voltage excitation.

### 8.2 PEDOT yarn resistance from published conductivity

- SWCNT/PEDOT:PSS/SA composite yarn [13]: σ = 15.3 S/cm = 1,530 S/m;
  d ≈ 290 µm → A ≈ 6.6×10⁻⁸ m² → **R/m ≈ 10 kΩ/m** (derived).
- Sisal/PEDOT:PSS, 4 layers [15]: σ = 0.752 S/m; d = 2.6 mm →
  A ≈ 5.3×10⁻⁶ m² → **R/m ≈ 250 kΩ/m** (derived).

A 10 cm length of the composite yarn is ~1 kΩ — directly readable by a
3.3 V divider with a 10 kΩ reference. The same length of sisal yarn is
~25 kΩ — readable, but the divider current is ~130 µA and leakage,
moisture, and ADC input impedance all start to matter. Both are
usable; neither is a drop-in replacement for a 300 Ω/m silver yarn.

### 8.3 A conductive braided sleeve as a parallel circuit

Take a 1 m sleeve, 16 carriers, 45° braid angle, HCB yarn (300 Ω/m).
Yarn path per carrier = 1 / cos(45°) ≈ 1.41 m → 423 Ω per carrier.
Sixteen carriers bonded in parallel at both ends: 423 / 16 ≈ **26 Ω
end-to-end** (derived, assuming perfect end bonds and no inter-carrier
contact; real braids have inter-carrier contact, which only lowers it
further). A sleeve is therefore a very low-resistance conductor by
construction — and a single broken carrier changes the total by ~6%,
invisible to any coarse readout. Redundancy is free; fault detection is
not.

### 8.4 Capacitive taxel order of magnitude

1 cm² electrodes, 1 mm silicone dielectric (εr ≈ 3): C ≈ 2.7 pF
(§6.2). A 50% compression of the dielectric roughly doubles it to
~5.4 pF. The AD7147 CDC in our sensor spec resolves femtofarads, so a
yarn-electrode capacitive taxel is comfortably measurable — the yarn
choice barely matters for capacitive sensing, which is the point:
**for capacitive taxels, buy the cheapest durable conductor (stainless)
or the best-insulated one (TPU silver), not the most sensitive one.**

## 9. Sourcing and buying order

Prices below are single-unit retail, checked 2026-11-27. Industrial
yarns (Shieldex/Statex, Madeira, Amann, Bekaert) are sold by quote or
through distributors, not by the metre online — expect minimum orders
and lead times, and request datasheets before ordering.

| Item | Source | Price / quantity (2026-11-27) | Notes |
|---|---|---|---|
| Adafruit 640, 316L 2-ply, 23 m | adafruit.com/product/640 | $6.95 ($0.30/m) | first buy: wiring |
| Adafruit 641, 316L 3-ply, 18 m | adafruit.com/product/641 | $9.95 ($0.55/m) | lower R, stiffer |
| Adafruit 603, 316L thick yarn, 30 ft | adafruit.com/product/603 | $4.50 ($0.49/m) | no Ω/m published; gloves/touch |
| Adafruit 1088, 316L fibre 20 µm, 10 g | adafruit.com/product/1088 | $2.95 | squeeze/contact experiments |
| SparkFun DEV-11791, stainless, 60 g, ~360 yd | sparkfun.com/products/11791 | $82.75 ($0.25/m) | bulk wiring; hairy, wax it |
| Shieldex 117/17 HCB, 235/36 HCB, HC 40 | shieldex.de / Statex; Madeira | quote only | request datasheet + wash data |
| Amann Silver-tech + 150 | Amann & Söhne | quote only | <300 Ω/m, knitting-proven [9] |
| Bekaert Bekinox | bekaert.com | quote only | no public Ω/m — request datasheet |
| Syscom Advanced Materials | syscom-advanced-materials.com | — | site unreachable during research; retry |
| VTechnical (Liberator) | vtechnical.com | — | JS-only site, no specs retrievable |
| Swicofil SwicoSilver | swicofil.com | — | silver yarn line listed, no public datasheet found |

**Buying order (first sleeves and first sensors):**

1. **Adafruit 640 + 641 (one bobbin each, ~$17).** Stainless wiring for
   every taxel run. Known resistance, known price, washable, no
   oxidation. This is the default conductor.
2. **Adafruit 1088 fibre ($2.95).** The cheapest possible contact /
   squeeze sensor experiment: felt a touch button, measure resistance
   versus squeeze. Validates the contact mechanism before any silver is
   bought.
3. **Shieldex HCB 117/17 (quote, small quantity).** The sensing yarn:
   300 Ω/m, best drift of the plain silver family, silicone-oil coat.
   Buy only after requesting the datasheet (235/36 Ω/m too) and the
   wash-cycle data Statex holds. Do not buy bare S117 (1,500 Ω/m) — the
   HC variant is strictly better for 5% more mass.
4. **Madeira HC 40 (quote, small quantity).** The best-measured silver
   yarn (GF up to 22.3, drift 19–29%) and the embroidery-grade finish
   matters if taxels are embroidered rather than braided. Buy alongside
   (3) and A/B them in the same test rig.
5. **Shieldex TPU-insulated yarn (quote).** Only for capacitive
   electrode runs where insulation is load-bearing. Last, because of
   mass and processability.
6. **PEDOT:PSS-coated yarn — do not buy; make.** No buyable PEDOT yarn
   with a datasheet was found. The published route is dip-coating a
   core yarn (sisal/PVA in the literature; a nylon or PU core would
   suit us better) — a bench experiment, not a purchase.
7. **Bekinox — hold until Bekaert supplies a datasheet.** The vendor
   claims are attractive (washable, corrosion-proof, blends), but
   without Ω/m and linear density it cannot be designed in.

## 10. Recommendations

| Decision | Recommendation |
|---|---|
| Default conductor (taxel wiring, bus runs) | Stainless 316L thread, Adafruit 640/641 or SparkFun bulk. 33–92 Ω/m, washable, no oxidation, no drift to track. |
| Strain / stretch sensing element | Silver-coated nylon, HCB or HC 40 (300 Ω/m). Budget system GF ≈ 2–3 after integration, not the 15–22 yarn-level figure. Pre-strain or floor the working range at ~5%. |
| Capacitive taxel electrodes | TPU-insulated silver yarn where insulation matters; stainless thread everywhere else. Yarn resistance is nearly irrelevant here (§8.4). |
| Binary touch / grip thresholds | Contact mechanism: loose stainless fibre (Adafruit 1088) or crossed silver yarns; a comparator, not a calibrated ADC chain. |
| High-sensitivity braided sensing | Follow Zhang et al.'s CNT/GNP 3D-braid route [12] as a research build, not a purchase. GF 340 @ 280% is the benchmark to beat. |
| High-strain (>50%) sensing | PEDOT:PSS-coated yarns (lab-made); silver nylon breaks its useful range at ~12%. |
| Washing policy for any silver in the body | Bleach-free liquid detergent only; treat silver as a replaceable consumable; darkening >10% means replace. |
| What not to buy yet | Bare Shieldex S117 (superseded by HCB); copper-core yarn (no datasheet, oxidation risk); Bekinox (no datasheet). |

## 11. Gaps — what this research could not verify

- **G1 — Missing datasheet resistances.** No public Ω/m for Bekaert
  Bekinox (any grade), Shieldex 235/36 / 78/20 / 44/10, VTechnical
  Liberator, Syscom silver yarns, or Swicofil SwicoSilver. The
  Shieldex shop returned HTTP 403; Syscom's site was unreachable;
  VTechnical's site is JavaScript-only; Kitronik and LessEMF returned
  HTTP 403. All four vendors need a direct datasheet request.
- **G2 — No flex-cycle lifetime for silver yarn as a conductor.** The
  literature characterises silver yarn as a *sensor* over 10 cycles.
  Nothing measures its resistance as a *conductor* over 10³–10⁶ flex
  cycles. Cheapest decisive experiment: motorised flex rig, HCB vs
  stainless, four-wire logging, 10⁴ cycles.
- **G3 — No braid-abrasion data for conductive yarns.** Washing-machine
  abrasion (Gaubert et al.) is the nearest proxy, but a braid's
  carrier crossings are a different abrasion regime. Needs a braided
  sleeve cycled under load with resistance logged.
- **G4 — No buyable carbon yarn with a datasheet.** Carbon tow exists
  but is a structural product, not a sensing yarn; no Ω/m was found for
  a carbon yarn sold for e-textiles.
- **G5 — Copper-core yarns undocumented.** Copper appears in
  Shieldex's metallisation list and in Tibtech's catalogue, but no
  copper yarn datasheet, wash study, or price was found.
- **G6 — No friction data for conductive yarns.** Fibre–fibre friction
  at braid crossings is unmeasured for silver-coated and stainless
  yarns; it decides whether a conductive braid holds its angle.
- **G7 — No long-term drift data.** Ten-cycle drift (19–64%) is
  published; nothing covers weeks of static hold, temperature cycling,
  or the interaction of sweat with strain sensing.
- **G8 — Prices are retail and single-unit.** Industrial pricing for
  Shieldex, Madeira, Amann, and Bekaert (per-metre at 100 m+ quantities)
  is unknown until quoted.

## Sources

All sources were opened and read during this research (2026-11-27).
Where a site blocked fetching (noted in G1), the source is cited only
for what its reachable pages actually state, or listed as unverified.

1. Shieldex — Fibers & Yarns (product catalogue: 117/17, 235/36 HCB,
   78/20, 44/10, TPU yarns; "can be twisted, knitted, embroidered,
   woven and spun like uncoated yarns").
   https://www.shieldex.de/en/products_categories/fibers-yarns/
2. Shieldex — Sensors, Heating & Lighting (capacitive, pressure and
   temperature sensors from Shieldex yarns/textiles).
   https://www.shieldex.de/en/applications/sensors-heating-lighting/
3. Adafruit — Stainless Medium Conductive Thread, 3 ply, 18 m (Product
   641): 316L stainless, 10 Ω/ft, $9.95, "will not oxidize like silver
   does", safe to wash. https://www.adafruit.com/product/641
4. Adafruit — Stainless Thin Conductive Thread, 2 ply, 23 m (Product
   640): 316L stainless, 16 Ω/ft, $6.95.
   https://www.adafruit.com/product/640
5. Adafruit — Stainless Thin Conductive Yarn / Thick Conductive Thread,
   30 ft (Product 603): 316L, $4.50, no resistance published.
   https://www.adafruit.com/product/603
6. Adafruit — Conductive Fiber, Stainless Steel 20 µm, 10 g (Product
   1088): $2.95; "becomes less resistive the more you squeeze the
   fibers together". https://www.adafruit.com/product/1088
7. SparkFun — Conductive Thread, 60 g, Stainless Steel (DEV-11791):
   28 Ω/ft, $82.75, ~360 yards; "somewhat 'hairy'", wax for hand
   sewing. https://www.sparkfun.com/products/11791
8. Mersch, J. et al. (2023). Electromechanical Properties of
   Silver-Plated Yarns and Their Relation to Yarn Construction
   Parameters. *Polymers* 15(21):4210. doi:10.3390/polym15214210 —
   S117/HCB/TPU/HC40 resistances (1,500/300/300/300 Ω/m), gauge
   factors, drift, TPU sheath mass/thickness, processability.
   https://pmc.ncbi.nlm.nih.gov/articles/PMC10647411/
9. Warncke, M. N. et al. (2023). Advancing Smart Textiles: Structural
   Evolution of Knitted Piezoresistive Strain Sensors for Enabling
   Precise Motion Capture. *Polymers* 15(19):3936.
   doi:10.3390/polym15193936 — Amann Silver-tech + 150 (<300 Ω/m,
   220 dtex), system GF 2.4, drift 50%, hysteresis 12.5%; steel yarns
   less suitable than silver-plated polyamide.
   https://pmc.ncbi.nlm.nih.gov/articles/PMC10574850/
10. Gaubert, V. et al. (2020). Investigating the Impact of Washing
    Cycles on Silver-Plated Textile Electrodes: A Complete Study.
    *Sensors* 20(6):1739. doi:10.3390/s20061739 — 30 delicate cycles,
    bleach vs liquid detergent, >10 MΩ after 20 percarbonate washes,
    surface silver 18% → 1.1%, darkening proxy.
    https://pmc.ncbi.nlm.nih.gov/articles/PMC7146542/
11. Zaman, S. U. et al. (2020). On the Effect of Sweat on Sheet
    Resistance of Knitted Conductive Yarns in Wearable Antenna Design.
    *IEEE Antennas and Wireless Propagation Letters* 19(4).
    doi:10.1109/LAWP.2020.2971189 — 7-day artificial sweat, efficiency
    32.7% → 24% over six cycles, 10% read-range loss.
    https://pmc.ncbi.nlm.nih.gov/articles/PMC8547707/
12. Zhang, M. et al. (2025). Three-Dimensional Braided Wearable Flexible
    Strain Sensors: Fabrication and Performance. *ACS Applied Materials
    & Interfaces* 17(47):65032–65047. doi:10.1021/acsami.5c16157 —
    3D-braided CNT/GNP sensor, GF 340 @ 280% strain, peak 1,152 @ 180%.
    https://pubmed.ncbi.nlm.nih.gov/41234026/
13. SWCNT/PEDOT:PSS/SA Composite Yarns with High Mechanical Strength and
    Flexibility via Wet Spinning for Thermoelectric Applications.
    *Sensors* 25(19):6202 (2025). doi:10.3390/s25196202 — conductivity
    15.3 S/cm, ~290 µm, 151 MPa, 12.7% break strain.
    https://pmc.ncbi.nlm.nih.gov/articles/PMC12526872/
14. Qi, K. et al. (2020). Core-sheath nanofiber yarn for textile pressure
    sensor with high pressure sensitivity and spatial tactile acuity.
    *Journal of Colloid and Interface Science* 561:93–103.
    doi:10.1016/j.jcis.2019.11.059 — Ni-coated cotton core, CNT-PU
    sheath; 16.52 N⁻¹, 0.003–5 N, ~0.03 s.
    https://pubmed.ncbi.nlm.nih.gov/31812870/
15. Piezo-Resistive Properties of Bio-Based Sensor Yarn Made with Sisal
    Fibre. *Sensors* 21(12):4083 (2021). doi:10.3390/s21124083 —
    PEDOT:PSS-coated sisal, conductivity 0.177 → 0.752 S/m (2 → 4
    layers), GF 0.42 / 3.98, moisture sensitivity.
    https://pmc.ncbi.nlm.nih.gov/articles/PMC8232028/
16. Seyedin, S. et al. (2015). Knitted Strain Sensor Textiles of Highly
    Conductive All-Polymeric Fibers. *ACS Applied Materials &
    Interfaces* 7(38):21150–21158. doi:10.1021/acsami.5b04892 —
    PU/PEDOT:PSS wet-spun fibres, knitted, repeatable to 160% strain,
    knee-sleeve demo. https://pubmed.ncbi.nlm.nih.gov/26334190/
17. Tibtech — Electric Conductivity (technical advice): carbon yarn
    resistivity falls with temperature (hot-spot risk) vs metals rising;
    ultra-fine multifilament yarns withstand bending/fatigue/washing.
    https://www.tibtech.com/electric-conductivity
18. Tibtech — Conductive Fabrics (Tibgrid heating fabrics, yarn
    functionalisation for smart textiles).
    https://www.tibtech.com/conductives
19. Bekaert — Conductive fibers and yarns for smart textiles (Bekinox
    stainless steel fibres/yarns; corrosion resistant; "washed
    numerous times"; no Ω/m published).
    https://www.bekaert.com/en/products/basic-materials/textile/e-textiles-/conductive-fibers-and-yarns-for-smart-textiles
20. Bekaert — Smart textiles product sheet (PDF): Bekinox stainless
    yarns/cables, washable, blends discretely into textiles; no
    electrical figures.
    https://www.bekaert.com/content/dam/corporate/en/products/basic-materials/textile/pdf/PS_Smart%20textiles.pdf
21. Shieldex — homepage: 40 years of metallised textiles in silver,
    copper, nickel and tin; silver 99.9% pure on polyamide.
    https://www.shieldex.de/en/
22. Mei, X. et al. (2022). Textile-Based Flexible Capacitive Pressure
    Sensors: A Review. *Nanomaterials* 12(9):1495.
    doi:10.3390/nano12091495 — sandwich / yarn / in-plane structures;
    yarn-structure devices most wearable, performance needs improvement.
    https://pmc.ncbi.nlm.nih.gov/articles/PMC9103991/
23. Object Shape Recognition Using Sparse Soft Capacitive Tactile Sensors
    for Robotic Hands. *Sensors* 26(17):5583 (2026).
    doi:10.3390/s26175583 — 95.4% size-invariant recognition across 12
    objects with sparse capacitive taxels.
    https://pubmed.ncbi.nlm.nih.gov/42740203/
24. Swicofil — homepage / yarn specialities: SwicoSilver silver yarn
    line listed; no public datasheet or resistance figure found.
    https://www.swicofil.com/
