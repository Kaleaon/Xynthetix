# Artificial Muscle Landscape — Actuator Technologies for Synthetic Bodies

**Status:** Research survey v1.0 — 2026-11-23
**Scope:** Every major artificial-muscle / soft-actuator class that could
move a full synthetic body, compared on sourced numbers, with an honest
treatment of the large-joint problem. This is the first Artificial
Muscles backlog item in `docs/research-queue.md`.

## How to read the numbers

Artificial-muscle papers report three very different kinds of number,
and mixing them is how bad actuator decisions happen:

1. **Material records** — best single-film / single-fibre results, often
   prestrained, at fields or temperatures no product could sustain.
2. **Device results** — a complete actuator lifting a load, with its
   frame, spring, or stack included.
3. **Commercial specs** — what a vendor will sell you and stand behind.

Where a number below is a record rather than a device or commercial
value, it is labelled as such. Numbers marked *(estimate)* are arithmetic
done for this survey from sourced inputs, not measurements.

The reference point throughout is mammalian skeletal muscle as tabulated
in the textile artificial-muscle review (used for most cross-class
comparisons below): 20–40% strain, 0.15–0.3 MPa actuation stress,
50–284 W/kg specific power, 20–70 J/kg specific work, up to ~40%
efficiency, >10⁹ cycles
([IOP review, Table 1](https://iopscience.iop.org/article/10.1088/1361-665X/ac3d9d)).

## The hard problem first: large joints

Before the classes, the load case that decides which of them matter.

- Healthy adults produce maximum voluntary isometric knee-extension
  torque of ~2.9–3.5 N·m per kg of body mass at ~60° flexion
  ([Research Square / Sci. Rep. study](https://www.researchsquare.com/article/rs-7653142/v1.pdf?c=1771276389000)).
  For a 100 kg body that is ~290–350 N·m peak at one knee.
- In deep-flexion daily activities (rising from kneeling, stair work),
  measured knee-extensor (quadriceps) force exceeds 4× body weight —
  >2,400 N in the study cohort — with total joint reaction forces above
  7× body weight at flexion over 130°
  ([ORS study, PDF](https://www.ors.org/transactions/51/0473.pdf)).
- Modelled stair ascent peaks at 3.87× body weight of quadriceps force
  ([PubMed 36054682](https://pubmed.ncbi.nlm.nih.gov/36054682/)).

So a human-scale knee extensor must deliver **several kilonewtons of
tendon force, repeatedly, for years**. With a patellar-tendon moment arm
of roughly 4–5 cm *(estimate — standard biomechanics range)*, even a
functional (sub-maximal) 150 N·m knee torque means ~3–3.7 kN of tendon
force. Every class below is judged against that bar, not against
"beats muscle on one axis in a lab demo."

---

## 1. Dielectric elastomer actuators (DEA) — deepest treatment

### Principle

A DEA is a soft capacitor: a thin elastomer film (silicone, acrylic,
polyurethane) between two compliant electrodes. Applied voltage squeezes
the film in thickness via Maxwell stress (p ∝ εE²) and it expands in
area; geometry converts that area change into useful motion. Drive is
inherently in the kilovolt range for useful fields
([Ma & Sameoto review, PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC9693343/)).
The founding result: prestrained films reached 117% linear strain
(silicone) and 215% (acrylic), with silicone's strain, pressure and
response time already exceeding natural muscle in 2000
([Pelrine et al., Science 2000](https://www.science.org/doi/10.1126/science.287.5454.836)).
Material-level ceilings tabulated in the IOP review: <380% strain,
<7.2 MPa stress, 3,600–5,000 W/kg specific power, up to <90% theoretical
efficiency, <1,000 Hz bandwidth, >10⁶ cycles
([IOP review, Table 1](https://iopscience.iop.org/article/10.1088/1361-665X/ac3d9d)).
Treat those as ceilings, not design values — most record performances
require prestrain on a rigid frame, and un-prestrained devices generally
show <100% strain and worse everything else
([PMC review](https://pmc.ncbi.nlm.nih.gov/articles/PMC9693343/)).

### Geometries

- **Planar / framed membrane.** The lab workhorse and the source of
  nearly all record numbers. Needs a rigid prestrain frame — a poor fit
  for a soft body except as skin-level or diaphragm elements.
- **Stack.** Hundreds to thousands of thin layers; thickness contractions
  sum, so the stack is the only DEA geometry that *contracts* like a
  muscle belly, and force scales with electrode area. Best device result
  found: Duduta et al. stacked 1,170 disk layers into a 6.3 cm, 20 g
  muscle that lifted 1 kg by 8 mm at 3.5 kV — 24% peak strain, 19.8 J/kg
  energy density (near mammalian muscle's range) — but full-stroke
  bandwidth was only 0.1 Hz at 3 kV
  ([PMC review, §2](https://pmc.ncbi.nlm.nih.gov/articles/PMC9693343/);
  [SmartMat review](https://onlinelibrary.wiley.com/doi/full/10.1002/smm2.1203)).
  A commercially available stack evaluated in the wearable-robots review
  reached high force/energy density but <4% strain
  ([JIMSS wearable DEA review, PDF](https://www.researchgate.net/profile/Gabriel-Vargas-3/publication/365252540_Dielectric_elastomer_actuators_as_artificial_muscles_for_wearable_robots/links/63a1adf2e42faa7e75db2cbf/Dielectric-elastomer-actuators-as-artificial-muscles-for-wearable-robots.pdf)).
  Stacks trade strain and speed for force, and every layer is another
  chance to fail (see lifetime, below).
- **Roll / spring roll.** Prestrained film rolled around a central
  compression spring (SRI's multifunctional electroelastomer rolls):
  the roll extends, bends, and senses, in 1–3 DOF versions. The honest
  device numbers are sobering — a documented 65 mm roll (45 mm active,
  20 acrylic layers, 1.2 cm diameter) produced ~26% strain at 5 Hz and a
  maximum force of **15 N** (~0.4 MPa); going from 20 to 35 layers raised
  force only to 21 N
  ([Humanoid Robots chapter, PDF](https://cdn.intechopen.com/pdfs/163.pdf)).
  SRI's material figures for acrylics — up to 8 MPa stress, 3.4 J/g
  specific elastic energy density, 60–90% electromechanical coupling —
  are material ceilings the roll geometry does not reach
  ([Pei et al., SPIE](https://www.academia.edu/178697872/Multifunctional_electroelastomer_rolls_and_their_application_for_biomimetic_walking_robots)).
- **Cone / diaphragm.** A membrane biased by a conical frame or bias
  spring converts area expansion into axial displacement of the cone
  apex — compact, genuinely contracting units used in pumps, speakers
  and tactile devices. It is one of the standard DEA configurations
  catalogued alongside stack, roll and balloon geometries
  ([SmartMat review](https://onlinelibrary.wiley.com/doi/full/10.1002/smm2.1203)).
  Force is limited by the same Maxwell-stress ceiling as every DEA;
  the cone buys stroke geometry, not stress.
- **Bending / DEMES.** A prestrained membrane bonded to a flexible frame
  settles into a bent minimum-energy structure; voltage changes the
  bend angle. Forces are tiny — a rollable DEMES gripper segment
  produced 2.2 mN of gripping force
  ([EPFL DEMES paper, PDF](https://infoscience.epfl.ch/server/api/core/bitstreams/e3e21f6a-49c6-4a3d-a993-1d6410fd596e/content)) —
  but for faces, ears, eyelids and fingers, tiny force at large angle is
  exactly the requirement. This is the most body-relevant DEA geometry
  per gram for expression.
- **Fibre / printed.** Direct-ink-written DEA fibres elongated ~12% in a
  5×5 bundle at 4 Hz resonance
  ([PMC review](https://pmc.ncbi.nlm.nih.gov/articles/PMC9693343/)) —
  early, but a fibre form factor is what a braided body actually wants.

### Drive, sensing, and control

- **Voltage:** kilovolts, at very low current. Field, not voltage, is
  the real variable (tens of V/µm); thin layers cut voltage — a
  low-voltage stack with ~6 µm layers actuated at 450 V
  ([PMC review](https://pmc.ncbi.nlm.nih.gov/articles/PMC9693343/)).
  High-voltage DC-DC converters are a per-channel cost and mass driver
  that muscle-count body designs must budget honestly.
- **Self-sensing:** a DEA is a capacitor whose capacitance tracks its
  deformation, so strain can be inferred electrically with no added
  sensor — a core reason DEAs suit proprioceptive bodies
  ([Anderson et al. 2012](https://www.open-access-button.org/paper/W2166445683/multi-functional-dielectric-elastomer-artificial-muscles-for)).
- **Efficiency:** theoretical coupling up to 60–90% for acrylics
  ([Pei et al.](https://www.academia.edu/178697872/Multifunctional_electroelastomer_rolls_and_their_application_for_biomimetic_walking_robots)),
  but experimentally measured DEA conversion efficiency is typically
  10–30%
  ([Acome et al., Science 2018, annotated](https://www.scienceintheclassroom.org/research-papers/hydraulically-amplified-self-healing-electrostatic-actuators-muscle-performance)).
  Charge-recovery drive electronics are where the gap is won or lost.

### Failure modes and lifetime evidence

This is DEA's weak axis, and the evidence is unusually specific:

- **Dielectric breakdown is statistical (Weibull)** — failure
  probability grows with electrode area and field, which is precisely
  the direction force scaling pushes. The HASEL paper makes this
  argument explicitly against large-area stacked DEAs
  ([Acome et al.](https://www.scienceintheclassroom.org/research-papers/hydraulically-amplified-self-healing-electrostatic-actuators-muscle-performance)).
- **Electrode choice dominates cycle life.** In high-cycle aging tests
  at 5% strain, silicone DEAs with hand-applied carbon-grease electrodes
  lasted <10⁵ cycles, while inkjet-printed carbon powder and stamped
  silicone–carbon composite electrodes exceeded 10⁷ cycles; aging
  tracked total actuated time, not frequency (10–200 Hz)
  ([IOP high-cycle aging study](https://iopscience.iop.org/article/10.1088/1361-665X/aa9f45/meta)).
- **Humidity and field dominate DC lifetime.** Mean time to failure for
  one common silicone at 100 V/µm, 85 °C / 85% RH was 1.6 h, rising to
  >200 h at 20% RH; thin encapsulation raised MTTF by factors of
  2.2–75×; >1,000 h DC life was extrapolated only below ~70–85 V/µm,
  i.e. at ~1.5–2.5% strain
  ([IOP DEA lifetime study](https://iopscience.iop.org/article/10.1088/1361-665X/ac3433/meta)).
  A warm, humid body interior is close to the worst-case corner of
  that dataset — encapsulation and field derating are not optional.
- Recent automated lifetime-scanning work confirms short life under
  high fields is still the field's stated blocker, with optimised
  parameters roughly doubling lifetime at boundary conditions
  ([arXiv 2602.20963](https://arxiv.org/abs/2602.20963v1)).

### Maturity and cost drivers

Materials are cheap (silicone/acrylic film, carbon electrodes); the
costs are fabrication yield over thousands of defect-free layers,
per-channel kilovolt electronics, and lifetime validation. There is no
catalogue DEA muscle at human-limb force scale; commercial stacks are
haptic/speaker-class devices with <4% strain at high force
([JIMSS review](https://www.researchgate.net/profile/Gabriel-Vargas-3/publication/365252540_Dielectric_elastomer_actuators_as_artificial_muscles_for_wearable_robots/links/63a1adf2e42faa7e75db2cbf/Dielectric-elastomer-actuators-as-artificial-muscles-for-wearable-robots.pdf)).

**DEA verdict:** unmatched strain, bandwidth, silence and self-sensing
per gram at small scale; at large-joint scale the arithmetic is brutal.
At an optimistic 1 MPa usable stress, 3.5 kN of knee-extensor force
needs ~35 cm² of active stack cross-section *(estimate)* — and stress
falls as the stack contracts, before any lifetime derating (Maxwell
stress falls with the *square* of field derating). Scaling Duduta's
device linearly, 3.5 kN ≈ 350 of those 20 g muscles ≈ 7 kg for one
knee, at 0.1 Hz full-stroke *(estimate from
[PMC review](https://pmc.ncbi.nlm.nih.gov/articles/PMC9693343/))*.
DEA is a face, hand, surface and fine-motion technology today, and a
research bet — not a plan — for prime movers.

---

## 2. McKibben / pneumatic artificial muscles (braided)

### Principle and numbers

An elastomer bladder inside a braided sleeve: pressurise, the bladder
expands radially, the braid converts it to axial contraction. This is
the class Xynthetix's braiding workstream feeds directly.

- Typical working pressure 400–600 kPa; commercial Festo muscles span
  5–40 mm diameters and contract up to ~25%
  ([PAM modelling chapter](https://1library.net/article/modelling-of-the-pneumatic-artificial-muscle-pam.zx6ol9vz)).
- Strain 30% and specific power ~2,000 W/kg in the IOP comparison
  table, with 32–49% efficiency and >10⁵ cycles
  ([IOP review, Table 1](https://iopscience.iop.org/article/10.1088/1361-665X/ac3d9d));
  other reviews put typical maximum pressure at 500–800 kPa and stroke
  at 25–40% of active length
  ([Tiwari et al., hydraulic AM](https://www.researchgate.net/publication/254116218_Hydraulic_artificial_muscles)).
- Initial braid angle is the master design variable: experimentally,
  ~25–30° balances force and stroke
  ([Actuators 2025 PAM review, PDF](https://mdpi-res.com/d_attachment/actuators/actuators-14-00582/article_deploy/actuators-14-00582.pdf?version=1764589630)) —
  exactly the angle → performance map the roadmap notes is unpublished
  for sleeves braided to spec.
- Force scales with pressure × cross-section, so kN-class force is
  available from fat muscles at the cost of volume and air supply.
  Force falls steeply with contraction (the braid geometry term
  (3cos²θ − 1) goes to zero), so rated force is a *blocked* force.

### The hydraulic variant changes the class

Same braid, incompressible working fluid: the Tokyo Tech / Bridgestone
hydraulic McKibben runs at **5 MPa** (vs 0.3–0.6 MPa pneumatic), is
15 mm in outer diameter, and delivers **7 kN maximum contraction force
at up to 30% contraction**, with a claimed strength-to-weight ratio
5–10× conventional electric motors and hydraulic cylinders
([Tokyo Tech news](https://www.titech.ac.jp/english/news/2017/037286);
[EurekAlert](https://www.eurekalert.org/news-releases/602746)).
That single data point proves braided geometry reaches large-joint
force. The price is the hydraulic power unit: pump, reservoir, valves,
and leak management inside a body.

### Failure, maturity, cost

Bladder fatigue and braid abrasion at the end fittings are the classic
failure modes; the class is the most mature in this survey (commercial
product lines exist — Festo's Fluidic Muscle descends from
Bridgestone's 1980s Rubbertuator
([PAM review](https://mdpi-res.com/d_attachment/actuators/actuators-14-00582/article_deploy/actuators-14-00582.pdf?version=1764589630))).
System efficiency is set less by the muscle than by the compressor:
pneumatic systems waste most energy in compression and throttling.
Cost drivers: compressor/pump mass and noise, valves per channel,
fittings. Antagonistic pairs are mandatory (a McKibben only pulls).

**McKibben verdict:** the only soft class with demonstrated kN force
(hydraulic form) *and* a direct line into this programme's braiding
core skill. Pneumatic form suits upper body and prototyping; hydraulic
form is a credible large-joint candidate if the power unit problem is
accepted.

## 3. Twisted & coiled polymer (TCP) actuators

Twist a nylon/polyethylene fibre until it coils; heating (usually Joule
heating of a conductive coating) untwists the coil and it contracts.

- Haines et al. (Science 2014): coiled muscles contract up to 49%,
  lift loads >100× equivalent human muscle, and generate 5.3 kW/kg peak
  mechanical power; precursor fibre costs ~$5/kg
  ([Haines et al., Science 2014, PDF](http://fennetic.net/irc/ray_baughman_coiled_monofilament_fishing_line_actuator_muscle.pdf)).
- Working numbers from the electrically-driven review: 21% strain at
  22 MPa loading stress, 9.3% at 50 MPa, maximum specific energy
  2.48 kJ/kg, average specific power 27.1 kW/kg *during contraction* —
  but efficiency ~1%, and full-cycle specific power is far lower
  because cooling dominates the cycle; a self-coiled nylon 6,6 muscle
  survived >10⁶ cycles at 1 Hz, 20% duty
  ([Ma & Sameoto review](https://www.mdpi.com/2072-666X/13/11/1881/xml)).
- Operating temperatures are the hidden cost: actuation typically needs
  fibre temperatures well above 80 °C, with 130–200 °C cited for common
  nylon systems — inside an insulated body, that heat must go somewhere
  ([IOP paediatric TCP study context](https://iopscience.iop.org/article/10.1088/1361-665X/ad50b0)).

**Failure/limits:** thermal — efficiency ~1%, bandwidth cooling-limited
to ≲1 Hz for useful bundles (thick bundles cool slower, so force
scaling fights bandwidth), creep and coating degradation over life.
**Maturity/cost:** cheapest actuator material in this survey by far;
research-grade only. **Verdict:** superb for slow, strong, cheap
secondary motions (posture trim, tail bias, grip assist) and for
textile-integrated actuation; disqualified as a dynamic prime mover by
physics — it is a heat engine with a ~1% ceiling in practice.

## 4. HASEL and other electrohydraulic actuators

### Principle

A sealed polymer pouch of liquid dielectric with flexible electrodes.
Voltage zips the electrodes together, displacing liquid and changing
the pouch's shape — electrostatic force hydraulically amplified, with
no pump. Because the dielectric is liquid, breakdown events self-heal
instead of destroying the device
([Acome et al., Science 2018](https://www.scienceintheclassroom.org/research-papers/hydraulically-amplified-self-healing-electrostatic-actuators-muscle-performance)).

### Numbers

- Original donut HASEL: >1 million cycles at 15% strain lifting 150 g
  with no perceivable performance loss; measured full-cycle efficiency
  21%; survived 50 dielectric breakdown events
  ([Acome et al.](https://www.scienceintheclassroom.org/research-papers/hydraulically-amplified-self-healing-electrostatic-actuators-muscle-performance)).
- Planar HASEL: 79% linear strain under 250 g (~32 kPa); at resonance,
  107–124% strain; two-unit device peak specific power 614 W/kg and
  specific work 70 J/kg; a single unit held 16% strain under 1.5 kg
  (~0.3 MPa — mammalian muscle's maximum stress); six in parallel
  lifted ~4 kg at 69% strain
  ([Acome et al.](https://www.scienceintheclassroom.org/research-papers/hydraulically-amplified-self-healing-electrostatic-actuators-muscle-performance)).
- At high specific power (358 W/kg average), a single unit ran to
  mechanical rupture at 158,061 cycles — the lifetime limit moved from
  electrical to mechanical (shell fatigue)
  ([Acome et al.](https://www.scienceintheclassroom.org/research-papers/hydraulically-amplified-self-healing-electrostatic-actuators-muscle-performance)).
- Peano-HASEL (the linearly contracting geometry): up to 10%
  contraction, 900%/s strain rate, actuation at 50 Hz, lifting >200×
  its own weight, with capacitive self-sensing
  ([Kellaris et al., Science Robotics 2018](https://www.science.org/doi/10.1126/scirobotics.aar3276)).
- The open HASEL toolkit reports actuators with >100% linear strain,
  >150 W/kg specific power, and ~20% strain at frequencies above
  100 Hz
  ([Mitchell et al., Adv. Sci., PDF](https://par.nsf.gov/servlets/purl/10119486)).
- Commercial reality check (Artimus Robotics, the CU Boulder spinout):
  the C-5015 contracting stack — 127 g, five units — is specified at
  2–8 kV drive, **150 N blocking force, 7 mm free stroke, typical
  lifetime 10⁴–10⁵ cycles**
  ([C-5015 datasheet, PDF](https://www.hannovermesse.de/apollo/hannover_messe_2021/obs/Binary/A1089438/C-5015%20Datasheet.pdf)).
  The vendor's own capability summary puts typical HASEL forces at
  10s–100s of N, strains up to 100%, frequencies DC to 100s of Hz
  ([Artimus capabilities](https://www.artimusrobotics.com/post/artimus-101-capabilities-of-hasel-actuators-artimus-robotics-information)),
  while claiming 1M+ cycle lifetimes in its newer commercialisation
  updates
  ([SEMI talk abstract](https://www.semi.org/en/connect/events/2024-future-of-electronics-speaker-abstract-bio-eric-acome)) —
  note the gap between the datasheet's 10⁴–10⁵ and the marketing
  figure; design to the datasheet.

### Failure, maturity, cost

Self-healing removes DEA's worst failure mode, but shell fatigue,
electrode damage, gas bubbles from breakdown events, and pouch sealing
yield become the limits. Drive is kilovolt-class like DEA (2–8 kV
commercial). Cost drivers: HV electronics per channel, pouch
fabrication yield, dielectric fluid handling. **Verdict:** the
strongest all-round soft candidate after McKibben — muscle-like stress
(0.3 MPa demonstrated), >100% strain at resonance, self-sensing, and a
commercial supplier — but demonstrated force is still 10¹–10² N per
unit; a knee would need dozens of units in parallel *(estimate)* and
nobody has published that system.

## 5. Shape-memory alloy (SMA) wires and springs

NiTi wire heated (Joule) through its phase transformation contracts
with very high stress and almost no strain.

- Commercial recovery strain 3–5% (up to 8% single-use); stresses up to
  ~400 MPa cited in the IOP review's SMA section, with ~150–200 MPa
  the recommended working recovery stress in vendor/application data
  ([IOP review](https://iopscience.iop.org/article/10.1088/1361-665X/ac3d9d);
  [SMA-as-muscle comparison table](https://www.academia.edu/65256491/Shape_Memory_Alloys_as_Artificial_Muscles)).
- Work density is the attraction: ~6,450 kJ/m³ in the comparison table
  — an order of magnitude above muscle per unit volume — at ~3–5%
  efficiency
  ([academia.edu table](https://www.academia.edu/65256491/Shape_Memory_Alloys_as_Artificial_Muscles);
  [IOP Table 1](https://iopscience.iop.org/article/10.1088/1361-665X/ac3d9d): ~1,200 J/kg specific work, 1,000 W/kg, ~10⁵ cycles, <3 Hz bandwidth).
- Vendor wire contracts 4–5% on heating and must be re-stretched by a
  bias force on cooling
  ([Dynalloy technical characteristics, PDF](https://static.rapidonline.com:443/pdf/87-6118.pdf)).

**Failure/limits:** cooling-limited bandwidth (thin wires in still air
cycle at ~1 Hz class), 10–30 K transformation hysteresis makes control
nonlinear, functional fatigue erodes recoverable strain early in life
(a wire at 310 MPa dropped from 4.5% to 3.5% recoverable strain in the
first 100 cycles in one study
([AZoRobotics survey](https://www.azorobotics.com/Article.aspx?ArticleID=853))),
and holding a contraction costs continuous power. Springs trade stress
for more stroke at lower force. **Verdict:** unbeatable where a few
millimetres of very strong, silent pull are needed in a tiny volume —
latches, locks, ear/finger trim, variable-stiffness elements — and
structurally incapable of large-joint stroke: 4% strain over a 40 cm
muscle is 16 mm of excursion, against the ~10+ cm a knee tendon path
needs *(estimate from excursion = moment arm × angle)*.

## 6. Baseline to beat: motors, hydraulics, SEA and cable-tendon drive

The incumbent architecture — an electric motor, usually geared, driving
the joint directly or through a cable tendon — is what every class
above must beat *as a system*, and mostly doesn't, yet.

- **Why gears exist:** electric motors have poor torque density and
  deliver power at high speed, so gearing is used to reach joint
  torques; gearing adds friction, backlash, torque ripple, and an N²
  increase in reflected inertia that makes impacts destructive
  ([Pratt & Williamson, SEA paper, PDF](https://fab.cba.mit.edu/classes/865.15/people/rebecca.kleinberger/assets/papers/SEA_Pratt.pdf)).
- **Series-elastic actuators** deliberately insert a spring between
  gearmotor and load, buying shock tolerance, lower reflected inertia,
  accurate and stable force control (spring deflection *is* the force
  sensor), and energy storage — at the cost of zero-motion force
  bandwidth
  ([Pratt & Williamson](https://fab.cba.mit.edu/classes/865.15/people/rebecca.kleinberger/assets/papers/SEA_Pratt.pdf)).
  SEAs are the proven route to backdrivable, human-safe motor joints
  (NASA's Valkyrie humanoid used SEAs throughout
  ([SEA overview](https://robotics.growbotics.ai/glossary/terms/series-elastic-actuator))).
- **Cable-tendon drive** moves the motor mass proximally (motors in the
  torso/pelvis, tendons to the joints) — the architecture this
  programme's braided tendon system is built around; its design rules
  (UHMWPE tendon, PTFE sheath, capstan friction budgeting, creep
  management) are in
  [docs/braided-mesh-integration.md](braided-mesh-integration.md).
- **Conventional hydraulics** (cylinders + central pump) deliver the
  highest force density of anything here and powered generations of
  legged robots, at the cost of mass, leaks, noise, and poor
  part-load efficiency. Hydraulic McKibben (§2) is the soft-bodied
  descendant of this line.

**Baseline verdict:** for a first full body that must stand, walk and
not fall apart, geared motors with series elasticity (or
quasi-direct-drive) on the large joints, tendon-routed, remain the
only option with solved torque, control bandwidth, efficiency
(motor+gear ~50–80% class) and supply chain. The soft classes win
specific places in the body, not the whole body — yet.

---

## Comparison table

Class-level values from the IOP textile review's Table 1
([source](https://iopscience.iop.org/article/10.1088/1361-665X/ac3d9d))
unless a cell cites otherwise. These are literature ranges (records
included), **not** design values — see each section for device-level
reality.

| Class | Strain | Stress | Specific power | Specific work | Efficiency | Bandwidth | Cycle life | Drive |
|---|---|---|---|---|---|---|---|---|
| Human muscle (ref) | 20–40% | 0.15–0.3 MPa | 50–284 W/kg | 20–70 J/kg | ≤40% | ~20 Hz | >10⁹ | chemical |
| DEA | <380% (record) | <7.2 MPa (record); ~0.4 MPa device ([IntechOpen](https://cdn.intechopen.com/pdfs/163.pdf)) | 3,600–5,000 W/kg | 3,400 J/kg (record); 19.8 J/kg device ([PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC9693343/)) | <90% theory; 10–30% measured ([Acome](https://www.scienceintheclassroom.org/research-papers/hydraulically-amplified-self-healing-electrostatic-actuators-muscle-performance)) | <1,000 Hz | >10⁶ claimed; 10⁵–10⁷ at 5% strain, electrode-dependent ([IOP aging](https://iopscience.iop.org/article/10.1088/1361-665X/aa9f45/meta)) | 0.45–8 kV |
| McKibben (pneumatic) | ~30% | ~0.6 MPa | ~2,000 W/kg | — (system-set) | 32–49% (muscle); system lower | ~1–10 Hz practical (valve/airflow-set) | >10⁵ | 0.4–0.8 MPa air |
| McKibben (hydraulic) | up to 30% | multi-MPa class; 7 kN from 15 mm OD ([Tokyo Tech](https://www.titech.ac.jp/english/news/2017/037286)) | high (5–10× motor strength/weight claimed) | — | not well published — open question, §6 | faster/stiffer than pneumatic (incompressible fluid) | bladder/sleeve fatigue-set | 5 MPa oil |
| TCP | up to 49% | 19 MPa (table); 21% strain @ 22 MPa ([MDPI](https://www.mdpi.com/2072-666X/13/11/1881/xml)) | 27.1 kW/kg (contraction only) | 2,480 J/kg | ~1% | ~1–2 Hz, cooling-limited | >10⁶ at low duty ([MDPI](https://www.mdpi.com/2072-666X/13/11/1881/xml)); table lists >10² for early devices | heat (Joule), fibre >80 °C |
| HASEL | 15% (table, early); 79–124% planar ([Acome](https://www.scienceintheclassroom.org/research-papers/hydraulically-amplified-self-healing-electrostatic-actuators-muscle-performance)); 10% Peano ([Sci. Robot.](https://www.science.org/doi/10.1126/scirobotics.aar3276)) | 0.3 MPa demonstrated ([Acome](https://www.scienceintheclassroom.org/research-papers/hydraulically-amplified-self-healing-electrostatic-actuators-muscle-performance)) | 614 W/kg peak ([Acome](https://www.scienceintheclassroom.org/research-papers/hydraulically-amplified-self-healing-electrostatic-actuators-muscle-performance)) | 70 J/kg ([Acome](https://www.scienceintheclassroom.org/research-papers/hydraulically-amplified-self-healing-electrostatic-actuators-muscle-performance)) | 21% measured; 10–30% range | 50 Hz Peano; >100 Hz toolkit | >10⁶ donut at low stress; 10⁴–10⁵ commercial datasheet ([Artimus](https://www.hannovermesse.de/apollo/hannover_messe_2021/obs/Binary/A1089438/C-5015%20Datasheet.pdf)) | 2–8 kV |
| SMA (NiTi) | 3–5% (8% max) | 100–200 MPa working; up to 400 MPa cited | ~1,000 W/kg | ~1,200 J/kg | ~3–5% | <3 Hz | ~10⁵ | Joule heat, low V / high A |
| Motor + gear / SEA + tendon | n/a (rotary) | set by gearing — kN tendon forces routine | set by motor | n/a | ~50–80% system *(estimate, class-typical)* | 10s–100s Hz torque loop | 10⁷+ (bearing/gear wear) | 12–48 V bus |

## Scale map: what can move what

- **Face, ears, eyelids, lips (mN–N, large angle, silent):** DEA
  bending/DEMES and small DEA membranes; SMA trim. Nothing else is
  close on silence and thinness.
- **Fingers and hands (N–100 N, cm stroke):** tendon drive from
  proximal motors (proven), HASEL stacks, DEA stacks, pneumatic
  McKibben for grippers. All viable; choice is control vs compliance.
- **Upper limb (100 N–1 kN):** HASEL parallel arrays (unproven as a
  system), pneumatic McKibben, tendon+motor. DEA stacks are ~an order
  of magnitude short on force at acceptable mass *(estimate, §1)*.
- **Hip / knee / ankle at 60–120 kg body scale (kN, 10⁷-cycle life):**
  today only motor+SEA/tendon and hydraulic classes close the force
  budget with margin. Hydraulic McKibben is the one soft class with a
  demonstrated single-unit force (7 kN) in range.
- **Tails, spines, posture (slow, distributed, moderate force):** TCP
  and pneumatic McKibben segments — bandwidth doesn't matter, cost
  and textile integration do.

## Failure modes & lifetime — the summary nobody publishes together

| Class | Dominant failure | Lifetime evidence |
|---|---|---|
| DEA | Dielectric breakdown (area/field/humidity-driven); electrode cracking | 10⁵ (grease) to >10⁷ cycles (printed electrodes) at 5% strain; DC MTTF collapses at high field + humidity ([IOP aging](https://iopscience.iop.org/article/10.1088/1361-665X/aa9f45/meta); [IOP lifetime](https://iopscience.iop.org/article/10.1088/1361-665X/ac3433/meta)) |
| McKibben | Bladder fatigue, braid abrasion at fittings | >10⁵ cycles (table); commercial service history |
| TCP | Coating loss, creep, thermal degradation | >10⁶ cycles at 1 Hz / 20% duty, low load ([MDPI](https://www.mdpi.com/2072-666X/13/11/1881/xml)) |
| HASEL | Shell mechanical rupture; seal failure; bubble accumulation | >10⁶ cycles at low stress; 1.6×10⁵ at high power; 10⁴–10⁵ commercial rating |
| SMA | Functional fatigue (strain decay), overheating | ~10⁵ cycles class-typical; early-life strain decay documented |
| Motor/SEA | Gear wear, bearing wear, cable fatigue | Industrial service lives; the benchmark |

## What this means for Xynthetix

The body architecture in this repo — braided tissue over a skeletal
core, tendon-driven, with sensing co-braided in — maps onto the
landscape like this:

1. **Primary movers, large joints: motor + SEA, tendon-routed, for
   the first bodies.** It is the only option that meets the knee
   numbers in §0 with control bandwidth and service life to spare.
   The braid programme's job for these joints is the tendon system
   itself: sheaths, guides, low-creep fibre, re-tensioning
   ([braided-mesh-integration.md](braided-mesh-integration.md)).
2. **Braided McKibben is the programme's home-grown muscle.** Pneumatic
   for prototypes and upper body; the hydraulic variant is the most
   credible soft path to large-joint force anyone has demonstrated,
   and sleeve angle is a variable *we* control because we braid to
   spec. The Phase 2 angle dataset (roadmap) is directly the missing
   design data for this class.
3. **DEA is the expression and surface layer, and a long-term bet.**
   Face, ears, eyelids, skin tensioning, variable stiffness, and
   self-sensing proprioceptive patches are DEA-shaped problems *now*.
   The cartridge idea in the backlog — a replaceable DEA unit, swapped
   like a battery — is the right response to the lifetime evidence:
   design for the measured 10⁵–10⁷ cycle reality instead of hoping
   for 10⁹. DEA as prime mover stays a research question (§ below),
   not a roadmap commitment.
4. **HASEL is the mid-body complement to watch and prototype with:**
   hands, forearms, tail segments — muscle-like stress, self-sensing,
   self-healing, and a buyable dev kit to learn from. Its HV
   electronics are shared with the DEA workstream, so one HV platform
   serves both.
5. **TCP and SMA are trim actuators:** cheap, strong, slow. Posture
   bias, tail stiffness, latches, grip assist, thermal-management
   shutters. Specify them where 1 Hz and 1–5% efficiency don't hurt.
6. **One HV bus, one tendon standard.** DEA + HASEL share kilovolt
   drive and capacitive self-sensing; everything else shares the
   tendon/sheath standard. Two infrastructure investments cover five
   actuator classes.

### Open research questions (feeding the backlog)

- Can a DEA stack be derated (field, humidity sealing) to a *verified*
  10⁷-cycle life at ≥10% strain and ≥0.5 MPa — and what does it weigh
  per kN then? No published device answers all four numbers at once.
- Hydraulic McKibben at body scale: can pump/valve mass and noise fit
  a torso, and what is the *system* efficiency end-to-end?
- HASEL parallel scaling: does force really add linearly to 10¹–10²
  units, and what fails first in a bundle — shell, seal, or driver?
- TCP inside an insulated body: where does the heat go, and can the
  body's own thermal system (warm-skin budget) use it instead of
  fighting it?
- Hybrid joints: motor/SEA for peak torque + soft muscle for
  compliance and silent low-load motion — control allocation between
  two physically different actuators on one tendon is unpublished
  territory.
- Self-sensing fusion: DEA/HASEL capacitance + tendon tension + joint
  encoders — which combination gives proprioception good enough to
  drop encoders from distal joints?

## Sources

Reviews and comparisons:
- IOP textile artificial-muscle review, Table 1 — https://iopscience.iop.org/article/10.1088/1361-665X/ac3d9d
- Ma & Sameoto, electrically driven soft actuators review (PMC) — https://pmc.ncbi.nlm.nih.gov/articles/PMC9693343/
- Ma & Sameoto (MDPI XML, TCP data) — https://www.mdpi.com/2072-666X/13/11/1881/xml
- Actuators 2025 PAM review — https://mdpi-res.com/d_attachment/actuators/actuators-14-00582/article_deploy/actuators-14-00582.pdf?version=1764589630

DEA:
- Pelrine et al., Science 2000 — https://www.science.org/doi/10.1126/science.287.5454.836
- Pei et al., SRI electroelastomer rolls — https://www.academia.edu/178697872/Multifunctional_electroelastomer_rolls_and_their_application_for_biomimetic_walking_robots
- Roll actuator device data, Humanoid Robots chapter — https://cdn.intechopen.com/pdfs/163.pdf
- Anderson et al. 2012, multi-functional DE artificial muscles — https://www.open-access-button.org/paper/W2166445683/multi-functional-dielectric-elastomer-artificial-muscles-for
- SmartMat DEA materials review 2023 — https://onlinelibrary.wiley.com/doi/full/10.1002/smm2.1203
- Wearable-robots DEA review (commercial stack data) — https://www.researchgate.net/profile/Gabriel-Vargas-3/publication/365252540_Dielectric_elastomer_actuators_as_artificial_muscles_for_wearable_robots/links/63a1adf2e42faa7e75db2cbf/Dielectric-elastomer-actuators-as-artificial-muscles-for-wearable-robots.pdf
- DEA lifetime under DC (IOP) — https://iopscience.iop.org/article/10.1088/1361-665X/ac3433/meta
- DEA high-cycle aging (IOP) — https://iopscience.iop.org/article/10.1088/1361-665X/aa9f45/meta
- DEMES gripper (EPFL) — https://infoscience.epfl.ch/server/api/core/bitstreams/e3e21f6a-49c6-4a3d-a993-1d6410fd596e/content
- DEA lifetime-scanning platform (arXiv) — https://arxiv.org/abs/2602.20963v1

McKibben / TCP / HASEL / SMA / baseline:
- PAM modelling chapter (Festo data) — https://1library.net/article/modelling-of-the-pneumatic-artificial-muscle-pam.zx6ol9vz
- Tiwari et al., hydraulic artificial muscles — https://www.researchgate.net/publication/254116218_Hydraulic_artificial_muscles
- Tokyo Tech / Bridgestone hydraulic muscle — https://www.titech.ac.jp/english/news/2017/037286 and https://www.eurekalert.org/news-releases/602746
- Haines et al., Science 2014 (TCP) — http://fennetic.net/irc/ray_baughman_coiled_monofilament_fishing_line_actuator_muscle.pdf
- TCP operating-temperature context (IOP) — https://iopscience.iop.org/article/10.1088/1361-665X/ad50b0
- Acome et al., Science 2018 (HASEL, annotated full text) — https://www.scienceintheclassroom.org/research-papers/hydraulically-amplified-self-healing-electrostatic-actuators-muscle-performance
- Kellaris et al., Peano-HASEL, Science Robotics 2018 — https://www.science.org/doi/10.1126/scirobotics.aar3276
- Mitchell et al., HASEL toolkit — https://par.nsf.gov/servlets/purl/10119486
- Artimus Robotics C-5015 datasheet — https://www.hannovermesse.de/apollo/hannover_messe_2021/obs/Binary/A1089438/C-5015%20Datasheet.pdf
- Artimus capabilities page — https://www.artimusrobotics.com/post/artimus-101-capabilities-of-hasel-actuators-artimus-robotics-information
- Artimus commercialisation milestones (SEMI) — https://www.semi.org/en/connect/events/2024-future-of-electronics-speaker-abstract-bio-eric-acome
- SMA as artificial muscles (comparison table) — https://www.academia.edu/65256491/Shape_Memory_Alloys_as_Artificial_Muscles
- Dynalloy muscle-wire technical characteristics — https://static.rapidonline.com:443/pdf/87-6118.pdf
- SMA fatigue survey (AZoRobotics) — https://www.azorobotics.com/Article.aspx?ArticleID=853
- Pratt & Williamson, series elastic actuators — https://fab.cba.mit.edu/classes/865.15/people/rebecca.kleinberger/assets/papers/SEA_Pratt.pdf
- SEA overview (Valkyrie) — https://robotics.growbotics.ai/glossary/terms/series-elastic-actuator

Load case:
- Knee extensor force in deep flexion (ORS) — https://www.ors.org/transactions/51/0473.pdf
- Knee MVIC torque per kg — https://www.researchsquare.com/article/rs-7653142/v1.pdf?c=1771276389000
- Stair-ascent quadriceps force (PubMed) — https://pubmed.ncbi.nlm.nih.gov/36054682/
