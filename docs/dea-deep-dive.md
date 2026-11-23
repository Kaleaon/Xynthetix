# DEA Deep Dive — Dielectric Elastomer Actuators for Synthetic Bodies

**Status:** research note, 2026-11-23. Artificial-muscles workstream,
second backlog item. Companion to the artificial muscle landscape
survey. Every quantitative claim below is cited to a source that was
opened and read for this note; back-of-envelope arithmetic is labelled
as ours, with its assumptions stated. Where the literature disagrees
with itself (it does, often), the disagreement is reported, not
smoothed over.

## 1. The physics in one paragraph

A DEA is a compliant capacitor: an elastomer film sandwiched between
two stretchable electrodes. Applied voltage puts opposite charge on
the electrodes; their attraction (Maxwell pressure,
*p* = ε₀εᵣ*E*²) squeezes the film thinner, and because the elastomer
is nearly incompressible it expands in area. Remove the voltage and
elasticity restores the shape. The same equation is given in both the
SmartMat materials review and the stacked-actuator benchmarking paper
([Guo et al. 2023](https://onlinelibrary.wiley.com/doi/full/10.1002/smm2.1203);
[Behboodi & Lee, PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC8050934/)).
Three consequences drive everything else in this note:

- **Stress scales with εᵣ·E².** You win by raising permittivity,
  raising the field, or thinning the film (same voltage, higher
  field). All three routes have hard limits (Section 4, Section 7).
- **The device is a capacitor, not a resistor.** A charged DEA draws
  only leakage current — the CTsystems stack benchmark measured
  39 µA steady-state — so holding force is nearly free energetically,
  and the charge can in principle be recovered on discharge
  ([Behboodi & Lee](https://pmc.ncbi.nlm.nih.gov/articles/PMC8050934/)).
- **Strain is large, stress is modest.** That asymmetry is the whole
  story of Section 8.

## 2. Geometries

### 2.1 Planar / diaphragm (circular membrane)

The laboratory workhorse: a prestretched membrane on a rigid frame,
electroded in a circular patch. Voltage expands the patch in-plane.
Pelrine et al.'s founding 2000 *Science* result was this geometry:
actuated strains up to **117% for silicone and 215% for acrylic**
elastomers with prestrain
([PubMed abstract](https://pubmed.ncbi.nlm.nih.gov/10657293/);
[paper](https://www.science.org/doi/10.1126/science.287.5454.836)).
Frame-based, so it is a test coupon and a component (lenses, pumps,
haptics), not a muscle form factor by itself.

### 2.2 Cone / diaphragm with bias element (out-of-plane)

Push the centre of an annular membrane out of plane with a rigid
disc and a bias spring (or a second, antagonistic membrane) and the
in-plane expansion becomes a linear stroke. The circular DEAP
configuration "also known as cone or diaphragm actuator" is used for
pumps, valves, micro-positioners and loudspeakers, and its output
scales linearly with size in the sizes tested
([ASME SMASIS 2014 abstract](https://asmedigitalcollection.asme.org/SMASIS/proceedings-abstract/SMASIS2014/46155/286190)).
An antagonistic cone pair — two cones opposed — was modelled and
built specifically to fix the single cone's limited deformation
range, and demonstrated driving a pump
([Guo et al., Extreme Mechanics Letters 2021](http://smart.hit.edu.cn/_upload/article/files/15/97/be9e866a4167a0588f12fd1b56b1/9d2748b0-82f2-45b2-aa07-41e6f5715099.pdf)).
Segmenting the cone's electrodes gives multiple degrees of freedom
from one membrane (same source). Cone/diaphragm is the natural DEA
geometry for **pumps, valves, faces and diaphragms** in a body —
anywhere the load is a pressure or a small out-of-plane motion —
not for limb joints.

### 2.3 Stack

Many thin layers mechanically in series, electrically in parallel,
between rigid end plates. Stroke adds per layer; force is set by
footprint area. This is the geometry that most resembles skeletal
muscle and the only one with a commercial product lineage:

- Kovacs et al.'s stacked actuator produced **32 N isometric force
  and 15–18% strain** from a 25 × 20 mm, 4 g device at 4,200 V,
  lifting a 1.1 kg tensile load; it became the CTsystems product
  ([benchmark comparison table](https://pmc.ncbi.nlm.nih.gov/articles/PMC8050934/)).
- The benchmarked CTsystems unit (CT25.0-15-15-71) is 1,600 layers of
  25 µm film in a 39 × 17 × 17 mm, 11.3 g package; manufacturer
  figures reproduced in the benchmark paper list 10 N max force, 5%
  strain, <100 Hz actuation and a claimed 50 million cycle life;
  independent measurement found **21.74 N, 3.3% strain, 21 ms
  electromechanical delay, 660 %/s strain rate and 426 W/kg**
  power-to-mass
  ([Behboodi & Lee](https://pmc.ncbi.nlm.nih.gov/articles/PMC8050934/)).
- A later evaluation of the newer Dätwyler-made version (15 × 15 ×
  50 mm) measured up to **25 N and ~115 kPa stress with ~11%
  longitudinal strain** — stress the authors note exceeds human
  biceps — up from 10 N / 3.3% in the previous generation
  ([Actuators 2024](https://www.mdpi.com/2977106)).
- Manufacturing note relevant to cartridges (Section 9): CTsystems
  layers are "first stacked into modules, which are tested and then
  stacked to the final actuator height"
  ([modelling paper, arXiv:2308.01675](https://arxiv.org/pdf/2308.01675)).
- Stacked *membrane* (cone) units push force higher: Hau et al.
  report one system lifting 7.5 kg and another generating **66 N at
  2.25 mm stroke**
  ([Hau & York, ACTUATOR 2016](https://www.researchgate.net/profile/Steffen-Hau-2/publication/304011501_A_Compact_High-Force_Dielectric_Elastomer_Membrane_Actuator/links/5da56b44299bf116fea82a91/A-Compact-High-Force-Dielectric-Elastomer-Membrane-Actuator.pdf));
  a secondary summary of the same work cites 72 N for the stacked
  configuration ([PMC benchmarking intro](https://pmc.ncbi.nlm.nih.gov/articles/PMC8050934/)).
  **66 N is the largest single-device DEA force we found in a
  primary source for this note.**

Stack specific work density is quoted at "approaching 13 J/kg" in a
simulation study citing Carpi and Kovacs
([SIMULIA 2013](https://www.3ds.com/assets/invest/2023-11/multi-gpu-computing-abaqus-benchmarking-scaling-multiphysics-13.pdf)) —
far below the material-level records in Section 5, which is the
difference between a film coupon and a packaged actuator.

### 2.4 Roll / spring roll

Prestretch a multilayer film and wind it around a compliant core
(typically a compression spring). The roll elongates axially when
energised. Two reference points:

- Wound-roll VHB actuators (Rajamani et al., IEEE/ASME Trans.
  Mechatronics 2008): **12% strain, 144 N/m stiffness, 3,480 cycles
  at maximum strain**; their finite-element model flags the innermost
  layer — thinnest, highest radial compressive stress — as the
  likely failure origin
  ([paper](https://www.academia.edu/10320244/Wound_Roll_Dielectric_Elastomer_Actuators_Fabrication_Analysis_and_Experiments)).
- Pei et al.'s spring-roll: **15 N force and 23% strain** from a
  60 mm cylinder
  ([cited in PMC benchmarking](https://pmc.ncbi.nlm.nih.gov/articles/PMC8050934/)).
- The spring-roll design study by Moscardo, Zhao, Suo & Lapusta
  works through the failure-mode budget for this geometry —
  breakdown, electromechanical instability, loss of tension, tensile
  rupture, spring compression limit — and shows loss of tension in
  the axial direction precedes electromechanical instability in
  spring rolls specifically
  ([iMechanica preprint](https://imechanica.egr.uh.edu/sites/default/files/Spring_Roll_Actuator_2008_07_03%20submit.pdf)).
- Modern rolled multilayers get thin: a Tsinghua aquatic robot rolls
  nine ~31 µm silicone layers with CNT electrodes into a 4 mm ×
  25 mm tube; layers under 35 µm bring the drive voltage down to
  ~1,500 V, and the finished bending actuator produces ~55 mN
  blocked force at 1,300 V / 17 Hz — insect/mesoscale territory,
  cited here to show where rolls are actually used today
  ([arXiv:2310.11426](https://arxiv.org/pdf/2310.11426)).

### 2.5 Folded, helical, tubular

Catalogued in the benchmarking paper's comparison table: tubular
(3% strain, 2,700 V, 105 g), helical (~8% strain, ~0.65 N, ~1,200 V),
folded (5% strain, ~3 N, ~1,000 V) — all an order of magnitude below
the stack on force
([PMC Table I](https://pmc.ncbi.nlm.nih.gov/articles/PMC8050934/)).
They matter for distributed, low-force actuation (skins, valves,
peristalsis), not prime movers.

## 3. Dielectric materials

Values below are ranges across sources, and the sources themselves
warn that breakdown field in particular depends strongly on test
method, strain state and ramp rate — treat any single number with
suspicion ([materials chapter](https://1library.net/article/materials-fundamentals-of-dielectric-elastomers.yj9g005z);
[Tröls et al., breakdown vs stretch](https://services.phaidra.univie.ac.at/api/object/o:359987/download)).

| Material | εᵣ | Breakdown field | Young's modulus | Response | Notes |
|---|---|---|---|---|---|
| Acrylic — 3M VHB 4910 | ~4.8 | ~55–412 V/µm (strongly stretch-dependent) | 0.2–3 MPa | ms–s | Strains to 380%; strong viscoelasticity → creep, slow |
| Silicone (generic) | 2.8–3.7 | ~80–130 V/µm | 0.1–1 MPa | µs–ms | Low viscous loss; kHz actuation demonstrated |
| Silicone — Wacker Elastosil film | ~2.8 | ~80–100 V/µm | ~1 MPa | µs–ms | Commercial film, the usual silicone baseline |
| Polyurethane | ~7 | ~160 V/µm | ~17 MPa | ms–s | Higher εᵣ, much stiffer |

Table compiled from
([materials chapter, Table 2.1](https://1library.net/article/materials-fundamentals-of-dielectric-elastomers.yj9g005z)),
cross-checked against a second review's table (VHB ε ≈ 4.8,
breakdown 63–150 MV/m; PDMS ε ≈ 2.7, breakdown 20–100 MV/m; PU
ε ≈ 7)
([Wiley, TENG–DEA review](https://onlinelibrary.wiley.com/doi/full/10.1002/eom2.70066)).
The two sources disagree on silicone breakdown by ~2× at the low
end — a fair sample of the state of published DE data.

**Acrylic (VHB).** The research default because of its huge strains,
but its "strong viscoelastic behavior… causes creep and low
actuation speed" (materials chapter, above). For a body that must
hold a pose for minutes, creep is not a footnote, it is the spec.

**Silicones.** "Unless very high actuation strains (> 80%) are
needed, silicone is the material of choice for commercial DEA
applications," with lower viscous losses and high-speed actuation
"up to the kHz-range" (materials chapter, above). Every commercial
stack in Section 2.3 is silicone. This is our default dielectric
family.

**Newer elastomers.**

- **Bottlebrush silicones.** Molecular architecture (dense side
  chains on a backbone) gives extreme softness without prestrain —
  stiffness reduced "by 1,000 times" versus conventional dry
  elastomers in the originating work, with built-in strain-stiffening
  that suppresses electromechanical instability
  ([NC State news on the 2016 paper](https://news.ncsu.edu/2016/11/bottlebrush-2016/)).
  A 2023 ROMP/thiol-ene bottlebrush formulation casts defect-free
  films under 100 µm, reaches permittivity 5.5 with polar backbone
  groups, gives **12% lateral actuation at 1,000 V and survives
  >10,000 cycles at up to 10 Hz**
  ([ACS AMI 2023, PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC10141291/)).
  A polar-brush polynorbornene variant reports εᵣ 4.4 at modulus
  below 100 kPa ([EPFL thesis record](https://infoscience.epfl.ch/server/api/core/bitstreams/58423cfc-e90f-49b1-ba4d-7bbfdc5c72b9/content)).
- **Interpenetrating polymer networks (IPNs).** Silicone + ionic
  IPNs report ε′ "as high as 7500 at 0.1 Hz" while keeping silicone's
  breakdown strength and modulus — but with higher dielectric losses
  than pure silicone, and that headline permittivity is a 0.1 Hz
  number, i.e. not available at actuation bandwidths
  ([RSC Advances 2015](https://pubs.rsc.org/en/content/articlehtml/2015/ra/c5ra07375h)).
  Interesting for quasi-static, low-voltage actuation; not a
  drop-in upgrade.
- **Filled silicones.** Silicone rubber with 10% BaTiO₃ reached a
  maximum energy density of 0.05 MJ/m³ at prestretch 1.6, comparable
  to VHB 4910 at its own optimum (3.4) in the same study — fillers
  raise εᵣ but the win is modest and bought with stiffness
  ([Jiang et al. 2015](https://d.docksci.com/investigation-into-the-electromechanical-properties-of-dielectric-elastomers-sub_5a63f092d64ab2f956ac5a36.html)).

## 4. Electrodes

Electrodes must stay conductive at 10–200%+ strain for millions of
cycles without stiffening the film or delaminating
([Guo et al. 2023](https://onlinelibrary.wiley.com/doi/full/10.1002/smm2.1203)).
Sheet-resistance figures from the high-frequency DEA review
([Tang et al. 2024](https://onlinelibrary.wiley.com/doi/full/10.1002/aisy.202300047)):

- **Carbon grease** (e.g. MG Chemicals 846): ~100 kΩ/sq for a 10 µm
  film. The lab default; messy, migrates, and — critically — the
  worst lifetime performer in the aging study of Section 7.
- **Carbon black / carbon-filled silicone composites:** patternable,
  bondable, the commercial-stack choice (CTsystems uses carbon
  powder electrodes, [arXiv:2308.01675](https://arxiv.org/pdf/2308.01675)).
- **Carbon nanotube networks:** sheet resistance in the
  10⁻³–10² kΩ/sq range shared with AgNW and hydrogels (Tang review);
  Guo et al. emphasise CNT electrodes' operational stability and
  **self-healing** behaviour — a broken CNT network can re-form
  conductive paths.
- **Silver nanowire networks:** similarly conductive, patternable;
  cost and oxidation are the open questions (no long-cycle DEA aging
  data found for AgNW in this pass — see Section 10).
- **Corrugated / microstructured metal films:** <1 kΩ/sq unstretched
  but conductivity "would decrease rapidly" above ~3% strain for
  plain metal films (Tang review). Only viable where the electrode
  itself is strain-isolated.
- **Ionic hydrogels / ionogels:** conductive past 100% strain,
  transparent; an ionogel-electrode DEA held its area strain for
  **≥10⁶ cycles at 15 kV, 16 Hz** with no delamination observed
  ([PMC, ionogel conductors](https://pmc.ncbi.nlm.nih.gov/articles/PMC12111308/)).
  Water-based hydrogels dry out; ionogels are the durable variant.

Electrode choice is a *lifetime* decision as much as an electrical
one — see the 100× lifetime spread in Section 7.

## 5. Performance records — and what they actually are

Read this section carefully: the spectacular numbers are
**material-level peaks from different devices**, not one actuator.

- A 2025 review's compiled optimum table gives DEAs (best-reported,
  across the literature): strain >500%, stress 7.7 MPa, work density
  3,400 kJ/m³, efficiency up to 90% — against human skeletal muscle
  at 40% strain, 0.35 MPa, ~70 kJ/m³
  ([Machines 2025 review](https://mdpi-res.com/d_attachment/machines/machines-13-00101/article_deploy/machines-13-00101.pdf?version=1737976587)).
- The SmartMat review similarly reports material-level strains
  >1,000%, energy densities exceeding 3 J/g, response <1 ms and
  theoretical efficiency up to 90%
  ([Guo et al. 2023](https://onlinelibrary.wiley.com/doi/full/10.1002/smm2.1203)).
- Power density is real at small scale: damage-tolerant flight DEAs
  exceed **700 W/kg** at >400 Hz bandwidth
  ([Science Robotics 2023](https://www.science.org/doi/10.1126/scirobotics.adf4278?cookieSet=1));
  the commercial stack benchmark measured 426 W/kg
  ([PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC8050934/)).

But packaged, purchasable, or independently benchmarked devices sit
at: **10–32 N force, 3–18% strain, ~65–115 kPa stress** (Section
2.3). The gap between coupon records and device reality — roughly
an order of magnitude on stress — is mostly packaging, bias
structures, derating for lifetime, and electrodes. Any Xynthetix
planning number should come from the device row, not the coupon row.

## 6. Drive voltage and high-voltage electronics

- **Voltage scale.** Working devices span ~1,000–6,000 V: CTsystems
  stack max recommended 1,200 V (tolerable 1,400 V)
  ([PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC8050934/));
  Kovacs stack 4,200 V; rolled multilayer robots ~1,300–1,500 V once
  layers are <35 µm ([arXiv:2310.11426](https://arxiv.org/pdf/2310.11426)).
  Voltage falls linearly with layer thickness — thin-film
  manufacturing *is* the voltage-reduction strategy.
- **Currents are tiny** (µA steady state; charge transients set the
  speed), so supplies are power-cheap but must be *fast, bidirectional
  and multi-channel*: a DEA that cannot discharge quickly cannot
  relax quickly, and one that cannot recover charge wastes the
  technology's efficiency advantage.
- **Miniature HV converters.** A published four-quadrant DEA supply
  built around XP Power EMCO A60P-5 modules (0.7–5 V in, ×1200 gain)
  generates independent 100–6,000 V arbitrary waveforms per quadrant
  in an ~80 × 80 × 50 mm package; the paper notes a parallel bleed
  resistor is required to discharge the DEA and that its value trades
  waveform fidelity against converter load
  ([Sensors 2024](https://www.mdpi.com/1424-8220/24/18/6080);
  [PMC version](https://pmc.ncbi.nlm.nih.gov/articles/PMC11435627/)).
- **Bidirectional flyback converters** are the established topology
  for stack actuators with energy recovery, and double as the
  self-sensing front end in the closed-loop work of Section 8
  ([Frontiers 2019](https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2019.00133/full)).
- **Implication for bodies:** HV electronics want to be *distributed*
  (one converter per muscle or muscle group, short HV runs) both for
  cable weight and because a body may need dozens of channels. Nobody
  sells a 40-channel, body-scale DEA driver; that is an Xynthetix
  build item, not a catalogue item (no source — our assessment from
  the supplies actually published, which are 1–4 channels).

## 7. Failure modes and lifetime evidence

1. **Dielectric breakdown.** Local defects puncture the film; one
   severe low-resistance defect can kill the whole device, and this
   "severely limits DEA performance, lifetime, and size scalability"
   ([Science Robotics 2023](https://www.science.org/doi/10.1126/scirobotics.adf4278?cookieSet=1)).
   Mitigations with published evidence: self-clearing electrodes
   (the electrode around a defect ablates and isolates it — works
   for minor defects only, same source); laser isolation repair of
   severe defects, demonstrated on DEAs enduring >100 punctures
   while keeping >700 W/kg (same source); and simply *derating* —
   maximum output needs ~80% of breakdown field, where lifetime is
   shortest ([arXiv lifetime-scanning preprint](https://arxiv.org/html/2602.20963v1)).
2. **Pull-in / electromechanical instability (EMI).** As the film
   thins under voltage, field rises, which thins it further —
   runaway to breakdown. Prestrain suppresses it: pre-stretch is
   "an effective approach to increasing actuated strain and
   dielectric strength and eliminating pull-in instability", with
   material-specific optima (silicone/BaTiO₃ at λ 1.6–1.9, VHB at
   λ 2.6–3.0)
   ([Jiang et al. 2015](https://d.docksci.com/investigation-into-the-electromechanical-properties-of-dielectric-elastomers-sub_5a63f092d64ab2f956ac5a36.html)).
   Strain-stiffening bottlebrush elastomers attack the same failure
   by material design instead of by frame prestrain (Section 3).
3. **Viscoelastic creep and drift.** VHB's strong viscoelasticity
   (Section 3) makes held strain drift; even silicone DEAs show
   initial cyclic drift before settling (noted in the ionogel DEA's
   cycling data, [PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC12111308/)).
   Control must close the loop (Section 8) rather than trust
   open-loop voltage→position maps.
4. **Electrode aging — the sleeper variable.** In high-cycle aging
   tests on silicone DEAs, manually applied carbon-grease electrodes
   lasted **<10⁵ cycles at 5% strain**, while inkjet-printed carbon
   powder and stamped silicone-carbon composite electrodes exceeded
   **10⁷ cycles at 5% strain**; aging depended on total time spent
   actuated, not frequency (10–200 Hz)
   ([Smart Mater. Struct. 2018](https://iopscience.iop.org/article/10.1088/1361-665X/aa9f45/meta)).
   Two orders of magnitude of lifetime from the electrode process
   alone.
5. **Fatigue under field.** Constant-electric-stress campaigns on
   Elastosil 2030 silicone films at 65–80 MV/m exist precisely
   because published fatigue data are scarce
   ([Chen et al., SPIE 2019](https://cris.unibo.it/bitstream/11585/710442/3/SPIE%202019_RV_7_MF.pdf)).
   A 2026 *npj Robotics* review summarises the spread: acrylate DEAs
   typically survive thousands to hundreds of thousands of cycles,
   silicone-based devices often exceed ten million, with breakdown,
   leakage, rupture and delamination as the common failure modes
   ([review](https://www.nature.com/articles/s44182-026-00074-3),
   as summarised in [AzoRobotics coverage](https://www.azorobotics.com/News.aspx?newsID=16341)).
6. **Optimisation evidence.** A robotic lifetime-scanning platform
   ("self-driving lab") varying field, frequency, electrode
   concentration and connection filler improved Elastosil linear-DEA
   lifetime at boundary operating conditions by up to 100%, and
   found the electrical-connection filler alone could swing lifetime
   by up to 500% between materials
   ([arXiv preprint](https://arxiv.org/html/2602.20963v1)).
   Connections and terminations are lifetime components, not
   afterthoughts.

**Honest summary:** >10⁷ cycles is demonstrated for silicone DEAs at
modest strain (5%) with the right electrodes. We found **no**
published >10⁶-cycle dataset for a DEA working at ≥15% strain and
≥100 kPa simultaneously — the operating point a limb muscle actually
needs. That dataset does not exist yet; generating it is a
legitimate Xynthetix deliverable (and matches the roadmap's
"measure, then claim" principle).

## 8. Self-sensing via capacitance

A DEA's capacitance is C = ε₀εᵣA/d; because the elastomer is
incompressible, deformation changes A and d together, so capacitance
is a direct, monotonic readout of deformation. The transducer
"combines actuator and sensor functionality within one transducer so
that no external sensors to measure the deformation or to detect
collisions are required"
([Frontiers 2019](https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2019.00133/full)).

- That paper demonstrates full self-sensing *control* of a stack
  transducer: an extended-Kalman-filter estimator reconstructs
  mechanical state from electrical measurements at the bidirectional
  flyback converter, and voltage, force or deformation can each be
  closed-loop controlled with accuracy comparable to sensor-based
  control (same source).
- A tri-modal actuator (linear actuation + loudspeaker + sensing)
  reconstructs low-frequency displacement from capacitance estimated
  out of the drive current signal, with no dedicated probing signal
  and no added transducer
  ([Sensors & Actuators A 2024](https://iris.unitn.it/retrieve/1044897b-6e40-474c-8b14-b78e0656232a/1-s2.0-S092442472400325X-main%20%281%29.pdf)).
- Limits, from the same literature: leakage current, permittivity
  drift with stretch/temperature, and the need to separate the
  sensing signal from a kV drive signal all degrade accuracy; early
  self-sensing methods were "accurate only under certain
  circumstances" (stationary, negligible leakage, low speed)
  ([US patent app. 2012/0086366, background survey](https://patents.justia.com/patent/20120086366)).
  Self-sensing gives proprioception good enough for control and
  collision detection; it does not replace a calibration reference
  at commissioning or after a cartridge swap (our assessment).

For a braided body this is a major architectural gift: the muscle
*is* the joint-position and contact sensor, so the sensor layer and
the actuator layer stop competing for the same volume.

## 9. What a replaceable "muscle cartridge" architecture implies

Design reasoning from the evidence above (this section is
Xynthetix analysis, not sourced claims):

1. **Cartridges are forced by the lifetime data.** Breakdown is
   stochastic and defect-driven (Section 7.1); even good devices are
   consumables on a 10⁵–10⁷-cycle envelope. A body whose muscles
   cannot be swapped is a body with an expiry date. Design the
   muscle as a sealed, connectorised unit from day one.
2. **The CTsystems precedent shows the manufacturing pattern:**
   layers → tested modules → stacked unit
   ([arXiv:2308.01675](https://arxiv.org/pdf/2308.01675)).
   Test-at-module-level maps directly onto cartridge QA: every
   cartridge ships with a measured force/strain/capacitance curve,
   and the body's controller loads *that cartridge's* curve.
3. **Interfaces a cartridge needs:** (a) two mechanical end
   fittings rated for the tendon load, keyed against misassembly;
   (b) one HV connector, recessed/interlocked so a cartridge cannot
   be handled live — the drive is 1–6 kV even though currents are
   µA; (c) a low-voltage ID/health line — capacitance self-sensing
   (Section 8) doubles as the health channel: a cartridge whose
   rest capacitance or leakage drifts out of family is flagged
   before it fails in service.
4. **Parallel redundancy beats heroic reliability.** Muscle groups
   in parallel (several cartridges per joint action) degrade
   gracefully: one failed cartridge costs a fraction of force, not
   the joint. This is also how biology handles motor-unit loss.
5. **Standardise a small number of cartridge sizes** (e.g. by
   footprint/force class), because force scales with area and stroke
   with length (Section 2.3): a product line of 2–3 footprints ×
   2–3 lengths covers most joints if the tendon routing sets the
   moment arm.
6. **The braid is the packaging.** In the Xynthetix architecture
   the braided sleeve over the skeletal core is the cartridge's
   abrasion shield, strain limiter and cosmetic surface in one —
   and a worn cartridge is swapped whole, the way the roadmap
   already treats braided sections as replaceable units.

## 10. Gap analysis: DEAs vs large-joint torque at 100 kg body scale

The demand side, from biomechanics: peak knee flexion moment in
stair climbing is **1.16 ± 0.24 Nm/kg**
([Costigan et al., Gait & Posture 2002](https://pubmed.ncbi.nlm.nih.gov/12127184/));
an orthosis design review compiles knee flexion moments of
1.04 Nm/kg (normal walking), 1.67 Nm/kg (fast walking) and
1.71 Nm/kg (stair climbing)
([Yakimovich et al., JRRD 2009](https://permanent.fdlp.gov/lps3362/lps3362/www.rehab.research.va.gov/jour/09/46/2/pdf/yakimovich.pdf)).

**Our arithmetic** (assumptions stated; check it, don't quote it as
literature):

- 100 kg body, stairs: peak knee moment ≈ 1.16–1.71 Nm/kg × 100 kg
  ≈ **116–171 Nm**.
- Quadriceps tendon moment arm at the knee is a few cm; at an
  assumed 0.04 m, tendon force ≈ 116/0.04 to 171/0.04 ≈
  **2,900–4,300 N**.
- At the best independently measured commercial-stack stress
  (~115 kPa, Section 2.3), 2,900 N needs ~0.025 m² of actuator
  cross-section — **~250 cm², an 18 cm-diameter bundle** — for one
  joint action, before antagonists. At human muscle's ~350 kPa
  (Section 5) the same force needs ~83 cm². The quadriceps
  cross-section that would have to fit inside a thigh does not
  exist at 115 kPa.
- Stroke is the second wall: knee tendon excursion over functional
  range is several cm; a stack gives 3–11% of its length, so a
  1 cm stroke needs a 10–30 cm stack *in series* — length a thigh
  can offer only along its whole extent, for one muscle group.
- Work per cycle tells the same story: ~115 kPa × ~10% ≈
  10 kJ/m³-class packaged work density vs the 40–70 kJ/m³ muscle
  figures in the Section 5 table.

**Verdict, honestly:** with published, packaged DEA performance,
DEAs cannot be the prime movers for hip/knee/ankle extension in a
100 kg body. The gap is roughly **3× on stress and 3× on strain
simultaneously** against muscle, and force records for complete
devices top out at tens of newtons (Section 2.3), three orders of
magnitude under the ~3–4 kN tendon force computed above. Anyone
claiming a DEA-driven full-size humanoid today is extrapolating
from coupon data.

**Where DEAs do fit a large body, on current evidence:**

- **Face, eyelids, ears, fingers' fine motion, skin and surface
  actuation** — small forces, high bandwidth, silence, and
  self-sensing are exactly what these need.
- **Variable-stiffness and damping elements** in parallel with a
  prime mover: a DEA that only has to *modulate* a joint's impedance
  works at a fraction of prime-mover force.
- **Pumps and valves** (cone/diaphragm, Section 2.2) for hydraulic
  or cooling circuits inside the body.
- **Distributed proprioceptive skin**: the same film technology,
  run primarily as sensors with local actuation (Section 8).
- **Smaller bodies and upper-body joints** scale kinder: torque
  demand falls with body mass while DEA stress does not, so
  shoulder/elbow/wrist actions in a ≤40 kg body are a defensible
  DEA target years before knees are.

The prime-mover seat at 100 kg scale stays with tendon-driven
motors / series-elastic or hydraulic actuation until a DEA device —
not a coupon — publishes ≥300 kPa at ≥15% strain over ≥10⁶ cycles.
That triple is the number to watch, and the cartridge architecture
of Section 9 is what lets a body adopt DEAs joint-by-joint as
devices cross it.

## 11. Evidence quality and open questions

- Published DE material constants vary by ~2× between reputable
  sources (Section 3); Xynthetix should measure, not adopt.
- Manufacturer cycle-life claims (e.g. CTsystems' 50 million cycles,
  reproduced in the benchmark paper's Table II) are **not**
  independently verified in anything we found; the independent
  aging literature (Section 7.4) is the trustworthy floor.
- We found no published force measurement above ~72 N for any
  complete DEA device, and no long-cycle dataset at limb-muscle
  operating points (Section 7). Both absences are findings, not
  oversights of this search — but a dedicated patent/commercial
  sweep is still owed before treating them as settled.
- AgNW electrode aging in DEAs, and bottlebrush elastomer behaviour
  in *stack* (not diaphragm) geometry, were both thin in this pass
  and are queued as follow-ups.

## Sources

All opened and read for this note, 2026-11-23:

1. Pelrine et al., *Science* 2000 — https://pubmed.ncbi.nlm.nih.gov/10657293/
2. Machines 2025 DEA review — https://mdpi-res.com/d_attachment/machines/machines-13-00101/article_deploy/machines-13-00101.pdf?version=1737976587
3. Guo et al., SmartMat 2023 — https://onlinelibrary.wiley.com/doi/full/10.1002/smm2.1203
4. Behboodi & Lee, CTsystems benchmark — https://pmc.ncbi.nlm.nih.gov/articles/PMC8050934/
5. Actuators 2024, SDEA as motor units — https://www.mdpi.com/2977106
6. Hau & York, high-force membrane stack — https://www.researchgate.net/profile/Steffen-Hau-2/publication/304011501_A_Compact_High-Force_Dielectric_Elastomer_Membrane_Actuator/links/5da56b44299bf116fea82a91/A-Compact-High-Force-Dielectric-Elastomer-Membrane-Actuator.pdf
7. Rajamani et al., wound roll actuators — https://www.academia.edu/10320244/Wound_Roll_Dielectric_Elastomer_Actuators_Fabrication_Analysis_and_Experiments
8. Moscardo et al., spring-roll design — https://imechanica.egr.uh.edu/sites/default/files/Spring_Roll_Actuator_2008_07_03%20submit.pdf
9. Zhang et al., rolled DEA aquatic robot — https://arxiv.org/pdf/2310.11426
10. Guo et al., antagonistic cone DEA — http://smart.hit.edu.cn/_upload/article/files/15/97/be9e866a4167a0588f12fd1b56b1/9d2748b0-82f2-45b2-aa07-41e6f5715099.pdf
11. ASME SMASIS 2014, circular DEAP geometries — https://asmedigitalcollection.asme.org/SMASIS/proceedings-abstract/SMASIS2014/46155/286190
12. DE materials chapter (properties table) — https://1library.net/article/materials-fundamentals-of-dielectric-elastomers.yj9g005z
13. TENG–DEA review (materials table) — https://onlinelibrary.wiley.com/doi/full/10.1002/eom2.70066
14. Tröls et al., breakdown vs stretch — https://services.phaidra.univie.ac.at/api/object/o:359987/download
15. Jiang et al. 2015, prestress & BaTiO₃ — https://d.docksci.com/investigation-into-the-electromechanical-properties-of-dielectric-elastomers-sub_5a63f092d64ab2f956ac5a36.html
16. NC State, bottlebrush elastomers 2016 — https://news.ncsu.edu/2016/11/bottlebrush-2016/
17. ACS AMI 2023, bottlebrush ROMP films — https://pmc.ncbi.nlm.nih.gov/articles/PMC10141291/
18. Adeli thesis, bottlebrush DE — https://infoscience.epfl.ch/server/api/core/bitstreams/58423cfc-e90f-49b1-ba4d-7bbfdc5c72b9/content
19. RSC Advances 2015, silicone/ionic IPNs — https://pubs.rsc.org/en/content/articlehtml/2015/ra/c5ra07375h
20. Tang et al. 2024, high-frequency DEA review (electrodes) — https://onlinelibrary.wiley.com/doi/full/10.1002/aisy.202300047
21. Ionogel conductor DEA, 10⁶ cycles — https://pmc.ncbi.nlm.nih.gov/articles/PMC12111308/
22. Sensors 2024, four-quadrant HV supply — https://www.mdpi.com/1424-8220/24/18/6080
23. Science Robotics 2023, laser failure recovery — https://www.science.org/doi/10.1126/scirobotics.adf4278?cookieSet=1
24. Smart Mater. Struct. 2018, high-cycle electrode aging — https://iopscience.iop.org/article/10.1088/1361-665X/aa9f45/meta
25. Chen et al., SPIE 2019, silicone fatigue life — https://cris.unibo.it/bitstream/11585/710442/3/SPIE%202019_RV_7_MF.pdf
26. npj Robotics 2026 review (via coverage) — https://www.nature.com/articles/s44182-026-00074-3 and https://www.azorobotics.com/News.aspx?newsID=16341
27. Lifetime-scanning preprint — https://arxiv.org/html/2602.20963v1
28. Frontiers 2019, self-sensing control — https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2019.00133/full
29. Sensors & Actuators A 2024, tri-modal DEA — https://iris.unitn.it/retrieve/1044897b-6e40-474c-8b14-b78e0656232a/1-s2.0-S092442472400325X-main%20%281%29.pdf
30. US 2012/0086366, self-sensing background — https://patents.justia.com/patent/20120086366
31. Commercial stack modelling — https://arxiv.org/pdf/2308.01675
32. SIMULIA 2013, stack work density — https://www.3ds.com/assets/invest/2023-11/multi-gpu-computing-abaqus-benchmarking-scaling-multiphysics-13.pdf
33. Costigan et al. 2002, stair knee kinetics — https://pubmed.ncbi.nlm.nih.gov/12127184/
34. Yakimovich et al. 2009, knee-orthosis design review — https://permanent.fdlp.gov/lps3362/lps3362/www.rehab.research.va.gov/jour/09/46/2/pdf/yakimovich.pdf
