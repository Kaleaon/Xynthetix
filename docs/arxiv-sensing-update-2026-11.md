# arXiv Sensing Update — November 2026

**Date:** 2026-11-28
**Scope:** What changed in the sensing literature since the
`sensing-proprioception-survey.md` pass, with emphasis on 2024–2026
arXiv preprints. Companion to `sensor-layer-spec.md` (SS),
`sensing-proprioception-survey.md` (SPS, gaps G1–G8), and
`conductive-yarn-tactile-sensing.md` (CY).
**Method:** arXiv searched directly by topic; every paper below was
opened at least to its abstract, and every number quoted is as
reported in that abstract. Abstract numbers are author-reported and
not independently verified — treat them as claims to check in the
full text before designing against them.

## Gap scoreboard (SPS §5.2, after this sweep)

| Gap | Status after Nov 2026 sweep |
|---|---|
| G1 Textile durability 10⁴–10⁵ cycles | **Not closed.** Best new textile result is 15,000 stable cycles (twisted-yarn capacitive, §2) — inside the same band. Vision-tactile hotspots fare better: a durable fingertip beats GelSight Mini / DIGIT durability by >100× under accelerated tests (§4). |
| G2 ">8,000 taxels/m² at >50 FPS" not achievable as raw streaming | **Substantially answered at array level.** Event-driven scanning (99% sparsity), compressive single-channel readout, and event+frame hybrids all published with hard numbers (§1). The spec's event-rate restatement is now well supported. |
| G3 Muscle self-sensing missing from SS | **Literature gap closed; spec gap remains.** DEA self-sensing has a full 2026 review; HASEL self-sensing now works to 20 Hz and in a sensorless hand (§3). SS still doesn't name it — spec update recommended. |
| G4 Tendon force sensing under-specified | **Narrowed, with a new alternative.** A self-sensing tendon loop measures input/output tension proximally with no distal sensor at all (§3); FBG point sensors keep improving but no body-scale multiplexed tendon result appeared. |
| G5 PPS RoboTact figures (3.2 mm, 100 Hz, I2C) unverified | **Still unverified.** Nothing in this sweep confirms them. |
| G6 Shear sensing thin | **Partially narrowed.** Magnetic lattice skins and tactile-proprioceptive fusion add routes (§4), but no tufted/shear-at-scale result. |
| G7 Fluid sealing of a sweating body unaddressed | **Still open.** No paper found addresses it. |
| G8 Dual-mode PEDOT:PSS thermal is single-study | **Still single-study.** Mundane routes gained support instead: textile capacitive sensors with minimal thermal drift 25–90 °C (§2), FBG temperature compensation (§3). |

## 1. Electronic skin & readout architecture

### Event-driven e-skin with SNN classification
- **arXiv:2603.10537** — *An Event-Driven E-Skin System with Dynamic
  Binary Scanning and real time SNN Classification* (2026-03-11)
  https://arxiv.org/abs/2603.10537
- 16×16 piezoresistive array; event-based binary scan search gives
  12.8× fewer scans, 38.2× data compression, 99% data sparsity;
  FPGA Conv-SNN classifies handwritten digits at 92.11% using 65% of
  a CNN's compute and 15.6% of its weight storage.
- **So what:** the strongest published support yet for SS rule 2
  (event-driven encoding). Directly narrows **G2** — the bandwidth
  problem is being solved by *not scanning*, exactly as the spec
  assumed, now with compression numbers attached.

### Single-Pixel Tactile Skin (compressive sampling)
- **arXiv:2511.16898** — *Single-Pixel Tactile Skin via Compressive
  Sampling* (2025-11-21) https://arxiv.org/abs/2511.16898
- Every taxel carries a miniature microcontroller and contributes a
  dynamically weighted analog signal to one global sum: the whole
  array reconstructs from a **single output channel**. Object
  classification at an effective 3,500 FPS; an 8 ms projectile impact
  resolved into 23 frames; contact localisation from as little as 7%
  of total data, then progressive refinement. Daisy-chainable wiring.
- **So what:** attacks the other half of **G2** — wiring, not just
  bandwidth. A braid-routed skin cares about conductor count more
  than almost anything; "a few input lines and one output" is the
  most braid-compatible readout architecture in this sweep. Candidate
  alternative to per-patch CDC + bus for low-density zones.

### Mixtac — event+frame hybrid vision tactile
- **arXiv:2605.18550** — *Mixtac: A Novel Bio-Inspired Hybrid Tactile
  Sensor with Synergistic Event-Frame Perception* (2026-05-18)
  https://arxiv.org/abs/2605.18550
- Event cameras drift during static force estimation; frames are
  slow. Mixtac fuses both: events for high-frequency tracking, frames
  to correct event drift, via a Frame Guided Event Recurrent Network.
  Normal-force MAE 0.04 N; bridges the 0–500 Hz sampling gap of
  vision-based tactile.
- **So what:** the drift problem SPS flagged for learned/event
  systems has an architectural answer — pair a fast drifting channel
  with a slow absolute one. The same pattern applies to our tufted
  layer (fast piezoresistive + slow capacitive absolute reference).

### DexSkin — calibratable conformable skin
- **arXiv:2509.18830** — *DexSkin: High-Coverage Conformable Robotic
  Skin for Learning Contact-Rich Manipulation* (2025-09-23)
  https://arxiv.org/abs/2509.18830
- Soft capacitive skin covering almost entire gripper finger
  surfaces; demonstrated on in-hand reorientation and elastic-band
  wrapping; critically, **calibrated so models transfer across sensor
  instances**, and used for online RL on a real robot.
- **So what:** cross-instance calibration is the published proof
  behind the SPS §5.3 "replaceable skin + recalibration" model
  (the G1 workaround). If skins are consumables, calibration transfer
  is the enabling technology — DexSkin shows it working.

### EIT-pneumatic hybrid skin
- **arXiv:2605.28468** — *EIT-Pneumatic Hybrid Robotic Skin for
  Practical and Accurate Force Map Reconstruction* (2026-05-27)
  https://arxiv.org/abs/2605.28468
- Fully 3D-printed + spray-coated skin; EIT reconstruction anchored
  by per-pad pneumatic calibration cuts sensitivity non-uniformity
  (coefficient of variation 0.31 → 0.14 vs EIT-only); chest-mounted
  on a humanoid, reliable under multiple simultaneous contacts.
- **So what:** EIT remains the cheapest large-area route, and its
  known weakness (non-uniform sensitivity) now has a published fix
  that is itself a calibration technique. Relevant to low-density
  torso zones where taxel arrays are overkill.

### Full-body modular e-skin gesture recognition
- **arXiv:2506.18256** — *Robot Tactile Gesture Recognition Based on
  Full-body Modular E-skin* (2025-06-23)
  https://arxiv.org/abs/2506.18256
- Irregular modular patches assembled over a robot body, thousands
  of sensing points (pressure + pose), classified by an equivariant
  graph neural network into poke / grab / stroke / double-pat
  gestures mapped to robot actions.
- **So what:** the stroke-vs-poke distinction SS wants for the
  relational channel (and SPS **G6** flags as thin) is demonstrated
  at whole-body scale — as a *learned, patch-level* classification,
  not per-taxel shear hardware. Supports treating shear/gesture as a
  software layer over pressure + pose, at least for interaction
  gestures.

## 2. Textile, knitted & yarn-level sensors

### Twisted-yarn textile capacitive sensors
- **arXiv:2608.14406** — *Effect of Twisted-Yarn Architecture on
  Pressure and Proximity Sensing Characteristics of Textile
  Capacitive Sensors for Robotic Skin* (2026-08-14)
  https://arxiv.org/abs/2608.14406
- Silver-coated yarns (the CY doc's sensing-yarn class) with PDMS
  coating, in 1/2/4-layer twisted configurations. Four-layer:
  sensitivity 0.1331 MPa⁻¹ at 100 kHz, low hysteresis, **minimal
  thermal drift from 25 to 90 °C, stable operation over 15,000
  cycles**; proximity range 60/50/40 mm for 1/2/4 layers (more layers
  = more sensitivity, less proximity range). 4×4 array demonstrated;
  robotic-arm touch+proximity reaction latency 403 ms end-to-end.
- **So what:** three wins in one paper — (a) yarn *architecture* is a
  tunable design parameter, which is exactly the lever a braiding
  programme controls; (b) pressure **and proximity** in one textile
  element speaks to multimodal skins; (c) thermal-drift data across
  25–90 °C supports the mundane thermal route over the single-study
  dual-mode device (**G8**). But 15,000 cycles leaves **G1** exactly
  where it was.

### Knit structure vs joint-angle error
- **arXiv:2610.07416** — *Knit-Structure Effects on Electromechanical
  Metrics and Their Correlation with Joint-Angle Estimation Error in
  Knitted Strain Sensors* (2026-10-05)
  https://arxiv.org/abs/2610.07416
- Seven knit structures × two stitch sizes, cyclic tension + joint
  bending rig. Gauge factor and baseline resistance are set by knit
  structure and predict joint-angle error; working range, hysteresis,
  and cyclic stability vary only modestly across designs.
- **So what:** a screening rule for proprioceptive textiles — pick
  structure by gauge factor / baseline resistance from a bench
  tensile test, don't over-optimise the other metrics. Useful when
  the queue's proprioception work reaches yarn selection.

### Full-body NFC knitted sensor networks
- **arXiv:2503.13240** — *Full-body NFC: body-scale near-field sensor
  networks with machine-knittable meandered e-textiles* (2025-03-17)
  https://arxiv.org/abs/2503.13240
- Digitally knitted twin-meander coils give battery-free NFC sensor
  tags over ~70–80% of body area, mW-class power, hundreds of kbps,
  tags occupying <0.3% of coverage area, robust under severe body
  movement.
- **So what:** a wireless alternative for the zones where a wired
  bus is worst (across joints, on replaceable patches). Battery-free
  tags on a knitted carrier is architecturally close to a braided
  carrier with sensor inlays — worth a design note if patch
  replacement (the G1 model) wants connector-free patches.

### Low-cost strain/touch fibre — and repair
- **arXiv:2606.13352** — *Low cost, easily manufactured, highly
  flexible strain and touch sensitive fiber for robotics
  applications* (2026-06-11) https://arxiv.org/abs/2606.13352
- Conductive thread ($0.07/ft) inside silicone tubing ($0.94/ft),
  20 cm made in 2 minutes with a $2 tool. Works as resistive strain
  sensor (grasp triggering, pose estimation) and, knitted, as
  capacitive touch / near-field sensor. **Includes a demonstrated
  method for repairing a cut fibre.**
- **So what:** the price point makes fibre sensing disposable, and
  the repair method matters more than the specs: a braided body will
  cut fibres. Field-repairable sensing fibre is a property none of
  the high-performance options in SPS advertise.

### e-Textile shape sensing for continuum robots
- **arXiv:2404.12627** — *A Soft e-Textile Sensor for Enhanced Deep
  Learning-based Shape Sensing of Soft Continuum Robots*
  (2024-04-19) https://arxiv.org/abs/2404.12627
- Resistive e-textile layers + CNN decode curvature/shape of a soft
  continuum robot, reported to match or exceed rigid sensor
  approaches without adding bulk or rigidity.
- **So what:** textile proprioception for continuously deforming
  structures (spine, tail) rather than discrete joints — the regime
  where encoders don't exist and our body plan has the least
  published support.

## 3. Proprioception & self-sensing actuators

### DEA self-sensing review (2026)
- **arXiv:2604.17199** — *Modeling, Control and Self-sensing of
  Dielectric Elastomer Soft Actuators: A Review* (2026-04-19)
  https://arxiv.org/abs/2604.17199
- Reviews physics-based and data-driven self-sensing methods that
  reconstruct DEA displacement with no additional sensors, alongside
  the modelling/control literature for creep, hysteresis, and
  viscoelasticity.
- **So what:** **G3** is now a spec problem, not a literature
  problem. A 2026 review exists to cite; SS should name DEA
  capacitance self-sensing as a muscle-subsystem input, as SPS
  recommended. First item on the top-5 list below.

### F-HASEL — high-frequency capacitive self-sensing
- **arXiv:2404.04071** — *High-Frequency Capacitive Sensing for
  Electrohydraulic Soft Actuators* (2024-04-05)
  https://arxiv.org/abs/2404.04071
- A dedicated extra electrode pair on a Peano-HASEL gives
  displacement estimation during actuation **up to 20 Hz** (previous
  HASEL self-sensing was effectively ≤1 Hz), using miniaturised
  low-cost circuitry and a miniature HV supply; multi-actuator
  estimation demonstrated tracking a VR user's joint rotations.
- **So what:** removes the bandwidth objection to HASEL
  self-sensing. If HASELs end up in hands/forearms (per the muscle
  landscape doc's hybrid recommendation), their proprioception is
  free and fast enough for control, not just monitoring.

### Sensorless electrohydraulic musculoskeletal hand
- **arXiv:2603.24357** — *A Sensorless, Inherently Compliant
  Anthropomorphic Musculoskeletal Hand Driven by Electrohydraulic
  Actuators* (2026-03-25) https://arxiv.org/abs/2603.24357
- Peano-HASEL actuators relocated to the forearm, 1:2 pulley tendon
  routing, and **grasp detection + closed-loop contact-aware control
  from operating current alone** — no force transducers, no encoders.
  Demonstrated on standard grasp taxonomies and non-destructive
  grasping of a paper balloon.
- **So what:** the closest published system to our hand concept —
  remote soft actuators, tendon routing, self-sensing as the *only*
  sensing. It validates the architecture and sets the bar: any
  Xynthetix hand design should explain what its extra sensors buy
  over this baseline.

### SSTL — self-sensing tendon loop
- **arXiv:2605.16870** — *SSTL: Self-Sensing Tendon Loop for
  Hysteresis Modeling and Compensation in Tendon-Sheath Mechanisms*
  (2026-05-16) https://arxiv.org/abs/2605.16870
- A double-pass loop tendon shares the actuation tendon's routing;
  both its input and output tensions are measured **proximally**, so
  no distal or fibre-optic sensor is needed. A learned mapping
  estimates the actuation tendon's configuration-dependent
  hysteresis; feedforward compensation cuts tension-tracking RMSE by
  **88.1%** vs uncompensated, reaching 97.8% of direct
  identification performance.
- **So what:** directly narrows **G4** with a route that competes
  with FBG-in-tendon: one sacrificial loop tendon per routing path
  gives the friction/hysteresis state of the whole path. For a
  tendon-driven body with dozens of routings, proximal-only sensing
  is a major wiring win. The two routes are complementary — SSTL for
  hysteresis state, FBG where true distal force is needed.

### FBG contact force sensor with temperature compensation
- **arXiv:2502.03914** — *A Flexible FBG-Based Contact Force Sensor
  for Robotic Gripping Systems* (2025-02-06)
  https://arxiv.org/abs/2502.03914
- Dual-FBG array in a 3D-printed TPU casing: range 4.69 N,
  sensitivity ~1169 pm/N, RMSE 0.12 N, max hysteresis 4.83%;
  temperature compensation holds force RMSE to **0.01 N over an
  11 °C change**. Closed-loop force control improved grip stability
  in pick-and-place.
- **So what:** FBG remains a point-sensor technology (gripper
  scale), but the temperature-compensation result matters for a body
  held at 35–37 °C with gradients — any FBG tendon installation
  needs exactly this. Supports keeping FBG in the spec for fingertip
  and tendon-exit points, not as the body-wide answer (**G4**).

### SMA self-sensing proprioception & contact
- **arXiv:2409.17111** — *Self-Sensing for Proprioception and
  Contact Detection in Soft Robots Using Shape Memory Alloy
  Artificial Muscles* (2024-09-25)
  https://arxiv.org/abs/2409.17111
- Pose and binary contact/no-contact predicted from SMA electrical
  resistance + in-situ temperature with a polynomial regression —
  no dedicated force sensors, in a fully soft limb.
- **So what:** completes the pattern across actuator families: DEA,
  HASEL, and now SMA all self-sense. Whichever muscles the body
  ships with, proprioception-by-actuator is published for it —
  reinforcing the **G3** spec update.

## 4. Multimodal skins & vision-based tactile

### Durable vision-based tactile fingertip
- **arXiv:2608.24242** — *A Durable Vision-Based Tactile Fingertip
  for Robotic Manipulation* (2026-08-25)
  https://arxiv.org/abs/2608.24242
- Silicone gel behind a textured TPU protective film, in a
  **replaceable sensing cartridge**. Accelerated tests: protective
  film rupture after ~2–3 h of drum sanding vs **24–30 seconds** for
  GelSight Mini and DIGIT; under 39.2 N repetitive probing at
  45 cycles/min, all nine units still functional when tests stopped
  at 5–8 days, vs 25–35 minutes to initial rupture for the
  commercial sensors. Degradation is gradual and barely interferes
  with imaging.
- **So what:** for the hotspot modules SS already specifies
  (fingertips), **G1** is effectively answered — by armour +
  cartridge replacement, the same replaceability doctrine SPS
  derived for textiles. >100× durability improvement is the number
  to beat for any in-house optical module.

### Magnetic lattice skin with super-resolution
- **arXiv:2605.28352** — *Magnet-Based Soft Robotic Skin Using a
  3D-Printed Multi-Lattice Structure and CNN-Based Tactile
  Super-Resolution* (2026-05-27) https://arxiv.org/abs/2605.28352
- Embedded magnets in a tunable 3D-printed lattice over Hall arrays;
  each sensor's receptive field is large and overlapping, minimising
  blind spots; a CNN estimates contact location and normal force in
  real time; SLS printing supports conformal, complex shapes.
- **So what:** the ReSkin lineage (SPS §2) growing a structural
  design parameter — lattice geometry tunes compliance and
  transduction together. A printed lattice under a braided skin is
  a plausible composite: braid carries, lattice transduces.

### Tactile-proprioceptive fusion for whole-body interaction
- **arXiv:2605.28412** — *Tactile-Proprioceptive Sensor Fusion for
  Contact Wrench Estimation in Whole-Body Physical Human-Robot
  Interaction* (2026-05-27) https://arxiv.org/abs/2605.28412
- Pneumatic skin pads act as contact indicators (bypassing the
  friction-residue ambiguity of motor-current-only estimation),
  fused with motor-current proprioception to reconstruct multi-axis
  contact forces; a temporal convolutional network handles friction
  hysteresis at stick-slip transitions. Validated in kinesthetic
  teaching on a skin-integrated arm.
- **So what:** whole-body contact *force* (not just detection) from
  cheap pads + currents we already have. For a body meant to be
  touched and guided, this is the estimation layer between taxels
  and behaviour — and another argument that proprioception and
  tactile should be one fused channel, as SS's receptor mapping
  implies.

## 5. Calibration, drift & learned tactile processing

### Tactile-JEPA — self-supervised tactile pretraining
- **arXiv:2609.24385** — *Tactile-JEPA: Topology-Aware
  Self-Supervised Representation Learning for Distributed Tactile
  Sensors* (2026-09-21) https://arxiv.org/abs/2609.24385
- Pretraining that predicts masked taxels' embeddings using the
  sensor connectivity graph, with dual-scale (local + global)
  masking. Across three datasets (magnetic and piezoresistive,
  multiple embodiments): force estimation error −6.3%, in-hand
  orientation error −20.8% vs prior state of the art; code public.
- **So what:** distributed skins have been the poor cousin of
  vision-tactile in learned processing; this is the encoder
  pretraining method built for exactly our sensor class
  (sparse, irregular taxel layouts — i.e. braided patches). Adopt
  as the default starting point for learned tactile work.

### Zero-shot force transfer across GelSight Mini units
- **arXiv:2608.18240** — *Zero-Shot Transfer of Force Map Estimation
  Across GelSight Mini Sensors* (2026-08-18)
  https://arxiv.org/abs/2608.18240
- Two-stage: UniT-based domain adaptation reconstructs any unit's
  image as a canonical tactile image (SSIM 0.9338 ± 0.0358), then a
  U-Net estimates 3D force maps (MAE_F 1.1294 ± 1.5934 N) — across
  units and versions, with no per-unit retraining.
- **So what:** handmade sensors vary; this is the recipe for not
  recalibrating from scratch at every cartridge swap (pairs with
  §4's replaceable fingertip and DexSkin's calibration transfer).
  The replaceable-skin doctrine now has a full stack: replaceable
  hardware, calibration transfer, and zero-shot model transfer.

### ML compensation for knitted force sensors
- **arXiv:2306.12129** — *Machine Learning Based Compensation for
  Inconsistencies in Knitted Force Sensors* (2023-06-21; included
  despite predating the 2024 window — it is the direct
  drift-compensation reference for knitted sensors)
  https://arxiv.org/abs/2306.12129
- Knitted sensors suffer offset, relaxation, and drift; exponential
  smoothing filters at several time constants feed a minimal ANN
  (3 layers, 8 neurons) that significantly improves force mapping,
  and the technique transfers across sensor materials/structures and
  to strain.
- **So what:** the CY doc's headline problem — 19–64% non-recoverable
  drift in yarn sensors — has a published, tiny, transferable
  compensator. Eight neurons is microcontroller-class: this can run
  in the digitizer at the patch, inside SS's architecture, today.

### EIT skin with deformation disentangling
- **arXiv:2504.05987** — *Learning-enhanced electronic skin for
  tactile sensing on deformable surface based on electrical
  impedance tomography* (2025-04-08)
  https://arxiv.org/abs/2504.05987
- EIT skins degrade on deforming surfaces because strain pollutes
  the tactile signal. This work tracks the deformation and fuses it
  into a deep reconstruction model: simulation correlations
  0.9660–0.9999, PSNR 28.7–55.5 dB; validated on a hydrogel EIT skin
  under multiple deformation scenarios.
- **So what:** every skin on a soft body lives on a deforming
  surface — this is the general problem, not an EIT quirk. The
  pattern (measure the deformation, condition the reconstruction on
  it) transfers to textile taxels stretched over joints.

## Top 5 to read in full

1. **arXiv:2604.17199** — DEA self-sensing review. The citation base
   for closing G3 in the sensor-layer spec.
2. **arXiv:2511.16898** — Single-Pixel Tactile Skin. The most
   braid-compatible readout architecture published this year;
   could reshape low-density zone design.
3. **arXiv:2605.16870** — SSTL. Proximal-only tendon hysteresis
   sensing is a direct design input to the tendon system, not just
   the sensor layer.
4. **arXiv:2608.24242** — Durable tactile fingertip. The durability
   benchmark (>100×) and cartridge doctrine for all hotspot modules.
5. **arXiv:2603.10537** — Event-driven e-skin + SNN. The numbers
   (12.8× scan reduction, 99% sparsity) to cite when SS rule 2 is
   next revised.

## What did not move

- **G5 (PPS RoboTact figures):** still no verification found.
- **G7 (sealing a sweating body):** no paper in this sweep addresses
  fluid sealing of sensor skins on a perspiring body. Remains a
  genuinely open problem — and therefore a publishable one.
- **Braided sensor structures specifically:** keyword searches for
  braided sensing returned almost nothing new on arXiv; the field is
  publishing *knitted/woven* textiles and *overbraided* elements
  remain mostly in journals. The braid-native sensing niche SPS
  identified is still unoccupied in the preprint record.
