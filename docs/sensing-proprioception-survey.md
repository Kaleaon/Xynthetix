# Sensing & Proprioception Survey — What the Literature Supports for a Braided Sensor Layer

**Date:** 2026-11-23
**Status:** Research survey v1.0 — companion to `sensor-layer-spec.md` and
`braided-mesh-integration.md`
**Scope:** Published tactile-sensing and proprioception technology, with
emphasis on what can be woven, knitted, tufted, or braided into a synthetic
body — and an honest gap analysis against our own sensor-layer spec.

## Key findings (up front)

1. **The spec's core architecture is the field's consensus, not a guess.**
   Every large-area robot skin that has actually shipped on a humanoid —
   iCub's capacitive skin, TUM's cellular HEX-O-SKIN line — independently
   converged on: local digitization at the patch, a serial bus out, and a
   hierarchical aggregator. Our "digitize near the skin" rule is exactly
   what iCub does with an AD7147 capacitance-to-digital converter per
   12-taxel module, and what Cheng's group does with a microcontroller per
   skin cell.
2. **Full-body tactile bandwidth is a solved problem only at modest rates.**
   Published whole-body systems deliver roughly 50 Hz frame rates over CAN
   (iCub) up to ~630 KB/s aggregate for 1,260 multimodal cells (Cheng et
   al.). Nobody publishes anything close to "8,000 channels at video rate,
   raw." Event-driven / send-on-change encoding is not an optimization —
   it is the only way the arithmetic closes, which validates the spec's
   event-driven rule and makes it load-bearing.
3. **Muscle self-sensing is real and published for both of our actuator
   families.** DEA displacement (and even force) can be reconstructed from
   the actuator's own voltage/current via capacitance estimation, with
   reported displacement error below 1% in one study; Peano-HASEL muscles
   in ETH Zürich's robotic leg provide capacitive self-sensing good enough
   for proprioception and obstacle detection in closed-loop hopping.
   A braided body does not need a separate proprioceptor per muscle — it
   needs the estimation electronics and models.
4. **The braid-native sensing results are stronger than our spec assumes,
   and the durability numbers are weaker.** Braiding itself is a published
   sensor-integration route (3D-braided triboelectric e-textiles;
   overbraided GMR sensors that survive machine washing). But published
   cycle lives for textile tactile sensors are typically 10⁴–10⁵
   interactions (ReSkin: >50,000), far below the 10⁶+ cycles a body needs —
   the spec's own open question is the right one, and nothing found here
   closes it.

---

## 1. Tactile sensing technologies

### 1.1 Capacitive

The workhorse of large-area robot skin. A deformable dielectric between
conductive plates changes capacitance under pressure; readout is a
capacitance-to-digital converter (CDC) at the patch.

- **iCub skin (IIT)** — the reference deployment. Triangular flexible-PCB
  modules carry 12 capacitive taxels each (10 pressure + 2 for temperature
  compensation in the insole derivative), digitized by an AD7147 CDC that
  can read all 12 taxels independently at 50 Hz, or an average at ~500 Hz,
  sending 16-bit values over I²C. Spatial resolution is ~4 taxels/cm²
  (≈5 mm pitch in the original skin paper). Modules chain over serial
  links; microcontroller boards aggregate patches and forward over CAN at
  50 Hz.
  [iCub hand integration](https://archive.iar.kit.edu/workshops/icra2010/pdf/8.pdf) ·
  [sensorised insole, same technology](https://www.mdpi.com/1424-8220/20/3/747)
- **Commercial arrays (PPS TactArray class)** — capacitive Kapton-encapsulated
  mats with elements as small as 2 mm, full-scale ranges up to 500 psi in
  industrial variants, ~0.3 mm thick. Useful benchmark for what commercial
  capacitive arrays achieve on flat/rigid surfaces; conformability to a
  soft, curved, moving body is a different and harder problem.
  [EE Times on PPS ITS](https://www.eetimes.com/ultra-thin-tactile-sensor-fits-into-tight-spaces/)
- **Textile capacitive** — conductive knit fabric electrodes with a silicone
  dielectric make fully soft capacitive sensors (see §2 and §3.2); the same
  transduction works for pressure and for strain.

**Braid relevance:** capacitive yarns are already in the integration doc's
sensing-yarn list. The literature supports capacitive as the *base layer*
choice (the spec's recommendation), with the caveat that the proven
deployments use flex-PCB taxels, not yarn taxels — yarn-form capacitive
sensing is demonstrated in textiles (§2) but not yet at iCub scale/density
on a robot.

### 1.2 Piezoresistive

Resistance drops under load. Cheapest, simplest readout (a divider or
op-amp), worst drift/hysteresis of the mainstream options.

- **FlexiForce A201 (Tekscan)** — the canonical discrete FSR: 0.203 mm
  thick, 9.53 mm diameter sensing area, standard ranges 4.4 N / 111 N /
  445 N, hysteresis <4.5% FS, drift <5% per logarithmic time decade, rated
  ≥3 million actuations at 22 N. Note the durability figure: a *discrete
  film* FSR is rated in millions of cycles — orders of magnitude beyond
  published textile-array lifetimes (§2), which is a materials-integration
  gap, not a transduction gap.
  [Tekscan A201](https://www.tekscan.com/products-solutions/force-sensors/flexiforce-a201-sensor)
- **STAG (MIT, Nature 2019)** — the canonical *array*: a piezoresistive
  film probed by a network of conductive-thread electrodes sewn onto a
  knitted glove, 548 sensors over the whole hand, normal forces 30 mN–0.5 N,
  full-hand frames at ~7.3 Hz, ~US$10 of materials. Proves that a textile
  row–column piezoresistive array plus learned models can identify objects
  and estimate weight — and also shows the frame-rate cost of passively
  probing a large passive matrix.
  [STAG project](http://stag.csail.mit.edu/) ·
  [Nature 2019 abstract](https://pubmed.ncbi.nlm.nih.gov/31142856/)

**Braid relevance:** piezoresistive yarns/films are the easiest to co-braid
(coaxial stainless/nanocomposite fibers are machine-knittable per the
integration doc), and STAG shows the readout pattern (passive row–column
probing) works in thread form. Budget for drift compensation in software;
the integration doc's ~1.6%/hour drift figure is consistent with FSR-class
behaviour, and FlexiForce's own datasheet drift spec confirms drift is
intrinsic to the transduction, not a defect of one product.

### 1.3 Optical (vision-based)

A camera images a deforming elastomer; spatial resolution is set by the
camera, not by taxel fabrication.

- **GelSight** — photometric stereo over a reflective elastomer membrane
  reconstructs contact geometry at 1–2 µm spatial resolution in metrology
  builds, 30–100 µm in compact robot-finger versions; marker motion gives
  force/shear/slip. Nothing else in this survey comes within two orders of
  magnitude on spatial resolution.
  [GelSight review, Sensors 2017](https://mdpi.com/1424-8220/17/12/2762/xml)
- **DIGIT** — miniaturized, low-cost, open-source GelSight-class sensor
  designed for multi-finger hands; modular, with replaceable elastomer.
  [DIGIT, arXiv:2005.14679](https://arxiv.org/pdf/2005.14679)

**Braid relevance:** none directly — optical sensors need a rigid optical
cavity, a camera, and illumination per site. They cannot be woven. Their
role in a braided body is exactly what the spec already says: discrete
hotspot modules (fingertips) embedded *in* the braid, not made *of* it.
The bandwidth cost is also real: a camera per fingertip is a video stream
per fingertip, which the body bus (§4) must treat as a separate class of
traffic.

### 1.4 Magnetic / Hall-effect

Two distinct sub-families:

- **Magnet-in-elastomer + magnetometer (ReSkin, Meta AI / CMU)** — a 2–3 mm
  elastomer with embedded magnetic microparticles, read by nearby
  magnetometers; ML models recover 3-axis force and contact location.
  Published specs: 1 mm spatial resolution at 90% accuracy, temporal
  resolution up to 400 Hz, >50,000 interactions lifetime, <$6 per sensor at
  100 units. The sensing skin contains *no electronics* — it is passive,
  peel-off replaceable, and self-supervised auto-calibration transfers
  between replacement skins. That replaceability model is the closest
  published analogue to our tufted-layer serviceability argument.
  [ReSkin](https://ai.meta.com/blog/reskin-a-versatile-replaceable-low-cost-skin-for-ai-research-on-tactile-perception/)
- **Magnetoresistive elements in the yarn itself** — flexible GMR thin-film
  sensors placed in the core of a textile braid ("overbraided"): detectivity
  down to 380 nT, machine-washable, functional underwater. Demonstrated for
  touchless interaction (a magnet in a ring/glove), not force sensing — but
  it is the strongest published proof that a *braid* can carry a functional
  sensor element in its core with conventional textile machinery.
  [Commun. Eng. 2025, PMC full text](https://pmc.ncbi.nlm.nih.gov/articles/PMC11861257/)

**Braid relevance:** high. A magnetic-particle elastomer can in principle be
tufted/coated onto a braid and read by magnetometers in the digitizer
pockets; GMR-in-braid is literally our manufacturing process carrying
someone else's sensor. Watch item: magnetic skins sense *field change*,
so nearby motors and DEA drive electronics are an interference source the
literature (wearables-focused) does not stress-test.

### 1.5 Barometric

Sealed MEMS barometers under an elastomer skin transduce contact pressure
into air-pressure change.

- **TakkTile (Harvard Biorobotics)** — consumer MEMS barometer chips
  (~$1 class) under vacuum-sealed rubber: ~1 g touch sensitivity, survives
  25 lb (11.3 kg) direct load and hammer strikes, built with standard PCB
  processes, digital I²C output per chip, strips of 5 sensors at 8 mm
  spacing in the starter kit.
  [Harvard SEAS](https://seas.harvard.edu/news/2013/04/robot-hands-gain-gentler-touch) ·
  [RobAid summary](https://www.robaid.com/tech/takktile-sensor-inexpensive-tactile-sensing-with-mems-barometers.htm)

**Braid relevance:** barometric taxels are rigid chips — they belong in
digitizer pockets or fingertip pads, not in yarn. But the transduction is
attractive for a braided body for one specific reason: the sensor is
*sealed and environmentally isolated by construction*, which sidesteps the
spec's open question about fluid sealing/sweat. Temperature cross-sensitivity
(the chip includes a temperature sensor for compensation) must be budgeted.

### 1.6 Also in the field: triboelectric & piezoelectric

- **Triboelectric (TENG)** — dynamic-only, self-powered. A 3D five-directional
  braided TENG e-textile (silver-plated nylon + PDMS-coated yarns) is
  machine-washable, compression-resilient, and pressure-sensitive, and
  doubles as an energy harvester (90 V open-circuit, 26 W/m³ peak under
  3 Hz / 20 N loading). As a *braided* sensor it is directly on-process for
  us; as a *static pressure* sensor it is not — TENGs report change, not
  held load.
  [Nat. Commun. 2020](https://www.nature.com/articles/s41467-020-16642-6)
- **PVDF piezoelectric yarn** — dynamic only (vibration/slip), consistent
  with the integration doc. No new contradicting evidence found.

---

## 2. Textile-integrated sensing

What has actually been demonstrated in fabric form:

| System | Form | Transduction | Scale demonstrated | Notes |
|---|---|---|---|---|
| STAG (2019) | Knitted glove + sewn conductive thread | Piezoresistive film, row–column probing | 548 sensors / hand, ~7.3 Hz frames | ~$10 materials; learned models do the heavy lifting |
| Silicone–textile composite (Harvard, 2017) | Conductive knit electrodes + silicone dielectric, laser-cut from a batch mat | Capacitive (pressure & strain variants) | Glove-scale; strain GF 1.23, high linearity, low hysteresis | Batch-fabricated as a *mat*, then cut to shape — a manufacturing model a braid shop can copy |
| 3DB-TENG (2020) | 3D five-directional braid | Triboelectric | Garment/shoe demos | Washable; dynamic sensing + harvesting |
| Overbraided GMR (2025) | Sensor film in braid core | Giant magnetoresistive | Armband / strap demos | Machine-washable; touchless, not force |
| PileUp (2025) | Tufted conductive pile | Resistive + capacitive | Rug, sleeve, wall art | Pile height/density are sensing parameters; bending/strain/moisture + pressure |
| ReSkin (2021) | Cast elastomer sheet (not woven) | Magnetic | Hand/arm/glove patches | Passive skin, replaceable, auto-calibrating |

Sources: STAG, Atalay et al., Dong et al., Lugoda et al., PileUp, ReSkin —
all cited in §1/§3.
[PileUp, arXiv:2511.21000](https://arxiv.org/abs/2511.21000) ·
[Atalay et al., silicone–textile capacitive sensors](https://biodesign.seas.harvard.edu/sites/g/files/omnuum11441/files/biodesignlab/files/2017_atalay_adv_mat_tech_-_batch_fabrication_of_customizable_silicone-textile_composite_capacitive_strain_sensors_for_human_motion_tracking.pdf)

**Patterns across the textile literature:**

- **Nobody has published a woven/knitted tactile skin at whole-body scale
  with per-taxel digital readout.** Textile demos are garment- or
  glove-scale with centralized readout; whole-body digital skins (iCub,
  Cheng) are flex-PCB, not textile. The braided sensor layer sits in a
  genuine gap between two literatures — which is the opportunity and the
  risk.
- **ML super-resolution / learned calibration is standard practice**, not a
  trick: STAG's object ID, ReSkin's self-supervised auto-calibration, and
  DEA self-sensing (§3.3) all treat the sensor as a signal source for a
  learned estimator. This supports the integration doc's super-resolution
  claim and the spec's runtime-calibration stance.
- **Conductive-yarn durability is the recurring failure mode.** The
  integration doc's warning about silver-coated conductors cracking under
  flex is consistent with the field's move toward intrinsically conductive
  elements (GMR films, liquid metal, PEDOT-class polymers) and passive
  skins (ReSkin) that keep conductors out of the flexing layer entirely.

---

## 3. Proprioception

A synthetic body needs joint angle, muscle length/force, and tendon tension
continuously. Four published routes, in order of maturity:

### 3.1 Joint encoders (the baseline)

Rotary encoders at the joint remain the ground truth every soft-sensing
paper calibrates against. They are rigid, point sensors — they cannot be
woven — but for a braided body with a skeletal core they are cheap,
absolute, and drift-free at the joints that have a defined axis. The
sensing review literature treats encoder-class proprioception as the
reference against which soft proprioceptors are judged.
[Review: The Next Evolution of Artificial Sense of Touch, arXiv:2310.16641](https://arxiv.org/html/2310.16641v2)

**Design rule:** encoders at skeletal joints wherever an axis exists;
soft proprioception (§3.2–3.4) for muscle state, continuum segments, and
redundancy — not as an encoder replacement.

### 3.2 Stretch / strain sensors

- **Liquid metal (EGaIn) microchannels** — resistance of a liquid-metal
  trace in an elastomer channel changes with strain; the conductor cannot
  fatigue-crack because it is liquid. Published devices: wave-shaped LM
  sensor with gauge factor 2.07, 150% strain range, 1.9% hysteresis, 0.4%
  detection limit, 120 ms response, closed-loop proprioception on a soft
  crawling robot; EGaIn microfluidic sensors reaching GF ≈ 4.95 at up to
  550% strain in optimized channel geometries. Park et al.'s elastomer
  sleeve embedded conductive liquid channels for strain/bend sensing
  alongside pneumatic muscles — an early integrated muscle+sense unit.
  [LM strain sensor, Sens. Actuators A 2024](https://www.sciencedirect.com/science/article/abs/pii/S0924424724003091) ·
  [Park et al., IROS 2012](http://www.cs.cmu.edu/afs/cs/user/ylpark/www/publications/Park_IROS12.pdf)
- **Capacitive stretch (textile)** — conductive-knit electrodes + silicone
  dielectric: gauge factor ~1 (theoretically bounded near 1 for parallel-
  plate geometry), but high linearity, low hysteresis, and 50 ms-class
  response in interdigital textile variants; demonstrated tracking finger
  and knee joints. Lower sensitivity than resistive/LM, better behaved.
  [Atalay et al. 2017](https://biodesign.seas.harvard.edu/sites/g/files/omnuum11441/files/biodesignlab/files/2017_atalay_adv_mat_tech_-_batch_fabrication_of_customizable_silicone-textile_composite_capacitive_strain_sensors_for_human_motion_tracking.pdf)

**Braid relevance:** LM channels are a *lay-in* element (axial inlay during
braiding, per the integration doc's layer cake), not a yarn; capacitive
stretch patches can be tufted/applied over joint zones. Both measure
*surface* strain — converting that to joint angle needs a model per joint,
which is a calibration problem, not a sensing problem.

### 3.3 Muscle self-sensing (DEA / HASEL capacitance)

The actuator is its own proprioceptor: a DEA or HASEL is a compliant
capacitor whose capacitance changes with deformation.

- **DEA** — superimposing a high-frequency probing signal on the actuation
  voltage and extracting capacitance from the sensing current yields online
  displacement estimation; Ye & Chen report <1% displacement error with
  ANN-based fitting, and Wang et al. validate capacitance self-sensing in
  closed-loop PI control of a tubular DEA with no external sensor.
  Rizzello et al. go further: simultaneous displacement *and force*
  reconstruction from voltage/current only, via recursive-least-squares
  capacitance estimation — i.e., interaction control with no separate
  force sensor.
  [Ye & Chen, Smart Mater. Struct. 2017](https://par.nsf.gov/servlets/purl/10056616) ·
  [Wang et al., Smart Mater. Struct. 2020](https://iopscience.iop.org/export?type=article&doi=10.1088/1361-665X/ab914b&exportFormat=iopexport_ris&exportType=abs&navsubmit=Export+abstract) ·
  [Rizzello et al., IEEE RA-L 2018 (record)](https://publikationen.sulb.uni-saarland.de/handle/20.500.11880/28184?locale=en)
- **HASEL** — Peano-HASEL muscles in ETH Zürich's electrohydraulic leg
  (Nature Communications 2024) provide capacitive self-sensing used for
  proprioception and obstacle detection during agile hopping (>5 Hz gait
  motions), with no dedicated external proprioceptors on the muscles.
  [PELE project page](https://srl-ethz.github.io/Electrohydraulic-Musculoskeletal-Robotic-Leg/)

**Caveat for our architecture:** self-sensing lives on the *high-voltage*
side. The sensor-layer spec's hard rule — sensing on the 3.3 V rail,
electrically separated from HV muscle — still holds for the *skin*; muscle
self-sensing is a muscle-subsystem function whose *estimates* (not raw HV
signals) cross into the sensory bus as data. The spec should say this
explicitly (see §5, gap G3).

### 3.4 Tendon force sensing

- **FBG-in-tendon (the Golgi-tendon-organ route)** — a fiber Bragg grating
  embedded in the actuating tendon itself measures tendon tension via
  wavelength shift. Yi et al. (RA-L 2023) built an underactuated gripper
  whose single-mode fiber tendon both actuates and senses grasp force;
  a 2025 follow-up puts three FBGs per finger — one for tendon tension,
  two at the fingertip for contact force and temperature. FBGs multiplex
  naturally: multiple gratings at different wavelengths share one fiber,
  and the Stanford work notes strain resolution on the order of 0.1 µstrain
  with full EMI immunity — valuable next to HV DEA drive lines.
  [Yi et al., RA-L 2023](http://bearlab.skku.edu/assets/pub/RAL_FBG.pdf) ·
  [Yi et al., IEEE T-RO 2025](https://www.osti.gov/pages/servlets/purl/17010324) ·
  [Park et al., ICRA 2008](http://bdml.stanford.edu/twiki/pub/RisePrivate/OpticalFiberICRA08/PhotonicRobot_ICRA08.pdf)
- **Motor-side inference** — the spec's "piezoresistive at joint capsules +
  motor current" line: motor current gives tendon tension only through the
  capstan/friction model the integration doc budgets so carefully. It is a
  useful cross-check, not a measurement. FBG-in-tendon is the published
  upgrade path and is braid-compatible in a way load cells are not (the
  fiber *is* a yarn-gauge element that routes with the tendon).

---

## 4. Readout electronics & system architecture

### 4.1 What published full-body systems actually do

| System | front-end | local aggregation | body bus | published rate |
|---|---|---|---|---|
| iCub skin | AD7147 CDC per 12-taxel flex-PCB module | Microcontroller tactile boards (≤16 modules each), temp/offset compensation on-board | CAN | 50 Hz full-patch frames; CDC can do 12 taxels @ 50 Hz or averaged @ ~500 Hz |
| Cheng / TUM cellular skin (HEX-O-SKIN lineage) | One multimodal cell = its own board: proximity (4 IR, <1 cm), 6 temperature sensors, 3-axis accelerometer, (later gens) force | Cell microcontroller; cells self-organize into a network, route for each other, self-locate | Cell network | 1,260 cells integrated; ~630 KB/s aggregate data rate (vs ~125 KB/s for iCub's skin) per the 2023 review |
| STAG | Passive piezoresistive matrix, conductive-thread row–column | Central probing electronics | — (tethered) | ~7.3 Hz full-hand frames (548 sensors) |
| ReSkin patch | Magnetometers on a flex PCB under a passive skin | Local board + ML model | — (patch-scale) | Up to 400 Hz per patch |

Sources:
[iCub](https://archive.iar.kit.edu/workshops/icra2010/pdf/8.pdf) ·
[TUM skin news release (cell contents)](https://webarchiv.typo3.tum.de/static/TUM/robotics/uploads/media/110629_robotskin.pdf) ·
[Mittendorfer et al., IROS 2013 (HEX-O-SKIN on HRP-2)](https://staff.aist.go.jp/e.yoshida/papers/MittendorferIROS2013.pdf) ·
[arXiv:2310.16641 (data-rate comparison)](https://arxiv.org/html/2310.16641v2) ·
[STAG](http://stag.csail.mit.edu/) ·
[ReSkin](https://ai.meta.com/blog/reskin-a-versatile-replaceable-low-cost-skin-for-ai-research-on-tactile-perception/)

### 4.2 Multiplexing patterns that recur

1. **Row–column passive probing** (STAG, PPS arrays): O(n+m) wires for an
   n×m matrix; frame rate falls as the matrix grows; sneak-path/ghosting
   management is the tax. Right for cheap, dense, slow zones.
2. **Per-patch CDC/ADC + I²C/SPI** (iCub): a standard CDC (AD7147) per
   ~12 taxels; short analog runs, digital onward. This is the spec's
   architecture, with published part numbers and rates.
3. **Cellular self-organizing network** (Cheng): every cell is a node that
   forwards for neighbours and auto-determines its position — the only
   published approach that treats *wiring topology itself* as survivable
   and self-describing. For a body whose skin is serviced by re-tufting
   (§5), auto-location is not a luxury: a replaced patch must announce
   where it is.
4. **Wavelength multiplexing** (FBG): many strain points on one fiber,
   one interrogator per limb segment; zero electrical noise pickup.
5. **Event-driven encoding** — the spec's send-on-change rule has a
   neuromorphic cousin in the literature: Cheng's group encodes multimodal
   hand sensing into spike trains modelled on mechanoreceptor/
   proprioceptor/thermoreceptor responses for spiking-network processing
   (97.14% object recognition across poses on a sensorized soft hand).
   Whether or not we adopt SNNs, the principle — transmit *events and
   features*, not raw frames — is what makes whole-body rates in §4.1
   achievable.
   [Wang et al., arXiv:2509.02275](https://arxiv.org/pdf/2509.02275)

### 4.3 Bandwidth sanity check (our numbers vs theirs)

The integration doc targets >8,000 taxels/m² at >50 FPS. At 16 bits/taxel
that is ~2.6 Mbit/s per m² *raw* — versus ~630 KB/s for the largest
published whole-body skin (1,260 cells, all modalities). Conclusion:
the target is reachable only with the spec's event-driven encoding plus
per-patch feature extraction (contact centroid, force sum, slip flag),
not with raw streaming. The documents should state the target as an
*event-rate* budget, not a frame-rate budget (gap G2, §5).

---

## 5. The braided sensor layer vs. the literature

Comparison against `sensor-layer-spec.md` (SS) and
`braided-mesh-integration.md` (BMI).

### 5.1 Agreements — spec positions the literature backs

| Spec position | Literature support |
|---|---|
| Digitize near the skin; digital on the bus (SS rule 1–2, BMI §2.2) | iCub (CDC per module, CAN backbone); Cheng (per-cell MCU) — universal in deployed systems |
| Capacitive or printed-polymer taxels as base layer (SS) | Capacitive is the only modality with whole-body humanoid deployments; textile capacitive (Atalay) is glove-proven |
| Optical/GelSight only at hotspots (SS) | GelSight/DIGIT are discrete camera modules by construction; cannot scale to area coverage |
| Event-driven encoding (SS rule 2) | Required by the bandwidth arithmetic of every published system (§4.3); spike/event encodings published by Cheng's group |
| Runtime calibration, not factory calibration (BMI §6–7) | FSR drift on datasheets; STAG/ReSkin/DEA self-sensing all rely on learned, adaptive estimators |
| ML super-resolution beyond taxel pitch (BMI §2.2) | STAG (learned grasp signatures), ReSkin (learned force/location from sparse magnetometers) |
| Tufted layer serviceability as the killer advantage (BMI §5) | ReSkin's peel-and-replace passive skin + auto-calibration is the published existence proof that replaceability + recalibration works as a system concept |
| Silver-coated conductor flex failure warning (BMI §2.3) | Field-wide shift to intrinsic conductors / passive skins / liquid metal (§2) |
| FBG as a sensing yarn (BMI §2.1, ~14.5 pm/N) | FBG-in-tendon is now published at gripper scale with tension + fingertip force + temperature on one fiber (§3.4) |

### 5.2 Gaps — where the spec outruns or under-specifies the literature

- **G1. Durability targets are unmet by every textile system found.**
  ReSkin: >50,000 interactions. Textile arrays generally: 10⁴–10⁵ cycles.
  Discrete FSR film: ≥3M actuations. The spec's open question (PEDOT:PSS
  at 10⁶+) remains open *for all textile modalities*, not just PEDOT:PSS.
  Implication: design the tufted layer for *scheduled replacement* (the
  ReSkin model) rather than lifetime durability, and say so in the spec.
- **G2. The ">8,000 taxels/m² at >50 FPS" figure (BMI §2.2) is not
  achievable as raw streaming** and no cited system demonstrates it as
  such; restate as event/feature throughput (see §4.3). Also, iCub's
  ~4 taxels/cm² (= 40,000/m²) shows *density* is not the binding
  constraint — *bandwidth and power per taxel* are.
- **G3. Muscle self-sensing is missing from the sensor-layer spec.**
  SS maps "deep pressure / proprioception" to piezoresistive + motor
  current. The DEA/HASEL capacitance literature (§3.3) is stronger,
  published, and native to our actuators. It belongs in the spec as a
  muscle-subsystem input to the somatic channel, with the HV-isolation
  rule clarified (estimates cross, raw HV does not).
- **G4. Tendon force sensing is under-specified.** BMI covers tendon
  friction/creep in detail but no tendon *tension sensing*. FBG-in-tendon
  (§3.4) is published, braid-routable, EMI-immune, and multiplexes on one
  fiber — it should be a named option in both documents.
- **G5. The PPS "RoboTact" figures in SS (3.2 mm elements, 100 Hz, I2C)
  could not be verified** against PPS publications found in this survey
  (published PPS arrays document 2 mm elements in research systems and
  industrial mats with different electronics). Treat those numbers as
  unverified until checked against a current PPS datasheet; the iCub
  numbers in this survey are the safer citation for the same design point.
- **G6. Shear sensing is thinner in the literature than SS implies.**
  SS wants a stroked-vs-pressed distinction. Published shear routes are:
  GelSight marker fields (hotspots only), ReSkin 3-axis magnetic (patch
  scale), and capacitive taxel quads (design pattern, limited published
  validation at scale). PileUp's pile deformation under shear is a
  plausible tufted route but is characterized for HCI, not robot skin.
  Flag shear as a research track, not a solved line item.
- **G7. No published system addresses fluid sealing of a *sweating* body**
  (SS open question). Closest data points: overbraided GMR works
  underwater and is machine-washable; barometric taxels are sealed by
  construction; ReSkin's passive skin has no in-skin electronics to
  protect. A composite answer exists (passive/washable sensing layer +
  sealed digitizer pockets) but nobody has published it as a body system.
- **G8. Thermal sensing: SS's dual-mode PEDOT:PSS sponge is a single-study
  result.** The mundane route — thermistors/RTDs, plus the temperature
  sensors already inside TakkTile-class barometers and Cheng's cells
  (6 per cell) — is what deployed systems actually use. Keep the dual-mode
  device as research track (SS already does) and spec thermistors as the
  baseline.

### 5.3 What a braided sensor layer can realistically reuse, today

1. **Readout architecture, wholesale:** iCub's module pattern (CDC per
   ~12 taxels, I²C locally, CAN/Ethernet-class backbone, compensation at
   the aggregator) maps 1:1 onto BMI's digitizer pockets and axial bus
   inlays. This is the lowest-risk reuse in the programme.
2. **Tufted pile as taxels:** PileUp validates tufted conductive pile as a
   pressure/bend/strain transducer with pile height and density as design
   parameters — BMI §5's core claim, now with a peer-reviewed-adjacent
   (TEI '26) citation.
3. **Braid-carried sensor elements:** overbraided GMR proves a braid can
   carry a functional thin-film sensor in its core on conventional
   machinery; 3DB-TENG proves a fully braided structure can itself be the
   sensor (dynamic channel).
4. **Passive, replaceable skins:** ReSkin's model — dumb skin, smart
   substrate, auto-calibration on swap — is directly transferable to
   tufted patches and resolves G1 by re
...[truncated 6852 chars]