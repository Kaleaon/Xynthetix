# The Synthetic Body Plan — A Research Map

**Status:** v1 — 2026-11-23
**Scope:** This document decomposes a complete synthetic body into
subsystems, names the interfaces between them, and for each subsystem
lists the open engineering questions that matter most, the published
work that already exists, and a first measurable experiment. It is the
research map for the whole Xynthetix programme: the braiding work in
this repo is one subsystem's supply chain, not the destination.

Conventions: factual claims carry a citation. Open questions are
written as questions and are *not* claims. Numbers quoted from vendor
or trade-press sources are flagged as such — per this repo's
principles, a number we have not measured ourselves is a lead, not a
result.

---

## 1. Subsystem decomposition

A complete synthetic body, decomposed by function. Every subsystem is
replaceable in principle; the interfaces are the design.

| # | Subsystem | What it does | Key interfaces |
|---|-----------|--------------|----------------|
| 1 | Skeleton | Load-bearing structure; sets proportions and mass distribution | Mechanical to joints (mounting, alignment); routing channels for tendons, wiring, cooling |
| 2 | Joints | Permit and constrain relative motion between skeleton segments | Mechanical to skeleton and muscles; sensing (angle, torque); skin must flex over them |
| 3 | Muscles / actuation | Convert stored energy into force and motion | Force out via tendons or direct joint drive; power in from power subsystem; heat out to thermal; commands from control |
| 4 | Tendons & transmission | Transmit force from actuators to joints, often remotely | Friction/length behaviour couples to control; routing couples to skeleton geometry |
| 5 | Skin & surface | Protection, appearance, thermal exchange, first contact layer | Must transmit tactile sensing; must pass or block heat per thermal design; flexes over joints |
| 6 | Sensing & proprioception | Tactile, joint position, force/tension, temperature, inertial state | Data to compute/control; physical integration into skin, tendons, joints |
| 7 | Power | Energy storage and distribution | Mass and placement couple to skeleton and balance; peak current couples to actuation; heat to thermal |
| 8 | Thermal | Reject actuator/compute heat; hold a warm surface temperature where wanted | Paths through skeleton and skin; conflicts with insulation and with skin-as-display/sensor |
| 9 | Compute & control | State estimation, balance, motion control, learned behaviour | Consumes sensing; commands actuation at multiple rates; consumes power, produces heat |
| 10 | Face & head | Expression, gaze, speech interface, primary social signalling | Actuation density vs mass at the end of the neck; skin flexibility; sensing (cameras, microphones) |
| 11 | Hands | Manipulation: grasp, in-hand motion, tool use | Tendon routing up the arm; tactile density at fingertips; force limits from actuation |
| 12 | Spine & torso | Connects pelvis to shoulders; posture, reach envelope, load path for arms and head | Highest structural loads in the body; houses power and compute in most designs |
| 13 | Tails & extra morphologies | Inertial balance aid, expression, additional contact/manipulation limb | Attachment structure at pelvis; angular-momentum coupling to whole-body control |

### Interface rules that recur everywhere

- **Mass is an interface.** Every subsystem's mass is carried by the
  skeleton, lifted by the muscles, powered by the battery, and cooled
  by the thermal system. A gram added anywhere is paid for four times.
- **Heat is an interface.** Actuators and compute produce it inside an
  insulated soft body whose surface may simultaneously be asked to
  feel warm. Where heat enters and leaves must be designed, not
  discovered.
- **Compliance is an interface.** Softness can live in the actuator
  (series elasticity), the transmission (tendon stretch), the joint
  (ligament-like constraints), or the skin. Where it lives determines
  what the controller can sense and how fast it can respond.
- **Repair is an interface.** If a worn braided section, muscle, or
  skin panel cannot be swapped as a unit, the body is not maintainable
  — modular boundaries should follow wear boundaries.

---

## 2. Subsystems: questions, published work, first experiments

### 2.1 Skeleton

**Open questions**

- Which structural material wins per segment — printed polymer,
  carbon tube/laminate, aluminium, or hybrid — once *repairability*
  and makerspace fabrication are scored alongside stiffness/weight?
- How much routing (tendon channels, wiring, cooling passages) can be
  integrated into the structure before the structure itself becomes
  the maintenance problem?
- What mass fraction of the total body should the skeleton be, and
  how does that fraction change with body size (see §3)?

**Published work**

- The University of Tokyo's musculoskeletal humanoids derive skeleton
  proportions and mass distribution from human statistical data
  rather than engineering convenience, and compare the result against
  human anatomy directly (Asano et al., *Science Robotics* 2017,
  "Design principles of a human mimetic humanoid").
  https://docslib.org/download/3873473/design-principles-of-a-human-mimetic-humanoid-humanoid-platform-to-study-human-intelligence-and-internal-body-system-yuki-asano-kei-okada-and-masayuki-inaba
- Kengoro's skeleton is 3D-printed porous aluminium that doubles as a
  cooling structure: water routed near the motors evaporates through
  the pores to remove heat — structure and thermal system as one part
  (platform summary with specifications).
  https://humanoidversus.com/robots/tokyo-kengoro
- Vendor data (flagged: vendor figures, verify before designing to
  them) put unidirectional carbon laminate specific stiffness at
  roughly 75–100 GPa per g/cm³ versus ≈25.6 for aluminium 6061-T6,
  titanium, and steel alike — the reason stiffness-designed robot
  links go carbon first.
  https://www.yongxian.co/en/blog/cf-humanoid-robot-structural-parts

**First measurable experiment**

Print/machine one forearm-length segment in three candidate materials
at equal bending stiffness; publish mass, cost, fabrication time, and
cycles-to-visible-damage under a repeated side-load rig.

### 2.2 Joints

**Open questions**

- For each joint class, which wins: conventional bearings, printed
  compliant/ligament-constrained joints, or hybrid (bearing for load,
  ligament for centring and range limits)?
- What range of motion does each joint actually need for the body's
  intended life (not for a demo), and what wears out first at that
  range under load?
- Can joint stiffness be *variable* — stiff under load, soft on
  contact — without a dedicated actuator per joint?

**Published work**

- Yoshimura et al. (UTokyo, *Advanced Intelligent Systems* 2026)
  built a life-sized (~0.95 m) leg with **no bearings at all**: 2D
  ligament patterns projected onto joint surfaces define the range of
  motion, and a single TPU material provides muscle-, tendon-, and
  ligament-like regions by lattice geometry alone. Their structures
  survived 999 loading cycles without rupture, with measurable
  stiffness change; stepping was demonstrated only under partial
  body-weight support, and autonomous walking was not demonstrated.
  Paper: https://doi.org/10.1002/aisy.70537 — project page:
  https://ssk-yoshimura.github.io/muscle-leg/
- The same work reports that moving lattice strut thickness from
  1.5 mm to 3 mm changed stiffness by roughly a factor of 28 —
  geometry, not material switching, as the stiffness dial (secondary
  summary of the paper).
  https://3dprinting.com/news/university-of-tokyo-team-3d-prints-robot-legs-with-tpu-muscles-and-ligaments/

**First measurable experiment**

One knee-class joint in two constructions (bearing vs printed
ligament), cycled under a fixed load spectrum; log range, backlash,
friction torque, and stiffness drift every 100 cycles to failure or
10k cycles.

### 2.3 Muscles / actuation

**Open questions**

- Which actuator class is the primary mover at each joint size — and
  is the honest answer different for knee/hip than for fingers/face?
- What does a *replaceable muscle cartridge* standard look like
  (mechanical, electrical, thermal interfaces) so muscles are
  consumables, not surgery?
- What cycle life is actually required? A body that walks daily
  accumulates ~10⁶ gait cycles per leg per year at human cadence —
  which candidate technologies have published life within an order of
  magnitude of that?

**Published work**

- Dielectric elastomer actuators (DEA) are the programme's lead
  candidate: reviews describe large deformation, fast response, and
  high energy density, with material fatigue and viscoelastic effects
  as the standing challenges (MDPI review, 2025).
  https://www.mdpi.com/2075-1702/13/2/101
- A self-healing DEA reported in *Nature Communications* (2026) held
  a stable 125% strain at 25 MV/m over 150,000 cycles and recovered
  from mechanical and electrical damage; the same paper puts natural
  muscle stress at ~0.35 MPa as the benchmark to match.
  https://www.nature.com/articles/s41467-026-72611-5.pdf
- HASEL electrohydraulic actuators (Acome et al., *Science* 2018)
  couple electrostatic and hydraulic forces in a soft pouch, are
  self-sensing, and repeatedly self-heal after dielectric breakdown
  because the dielectric is a liquid.
  https://www.science.org/doi/pdf/10.1126/science.aao6139 and
  https://is.mpg.de/rm/en/publications/keplinger18-s-hydraulically
- Twisted & coiled polymer (TCP) muscles from fishing line and
  sewing thread contract by up to 49%, lift loads over 100× what
  human muscle of the same length and weight can lift, and reach
  5.3 kW/kg peak mechanical power — but are thermally driven, so
  cooling rate bounds their bandwidth (Haines et al., *Science*
  2014).
  https://www.science.org/doi/10.1126/science.1246906
- McKibben pneumatic muscles — the braided actuator this repo's
  Phase 2 benchmarks — reach axial strains of ~30–35% in
  state-of-the-art builds across a 1–50 mm diameter range, with
  hysteresis and nonlinear control as the documented weaknesses
  (critical design review, *Bioinspiration & Biomimetics* 2026).
  https://beta.iopscience.iop.org:443/article/10.1088/1748-3190/ae66c0/meta
- Series elastic actuators (Pratt & Williamson, IROS 1995) remain the
  reference for motor-driven joints: a deliberate spring between
  gearbox and load buys shock tolerance, lower reflected inertia,
  accurate and stable force control, and energy storage, at the cost
  of force bandwidth.
  https://fab.cba.mit.edu/classes/865.15/people/rebecca.kleinberger/assets/papers/SEA_Pratt.pdf

**First measurable experiment**

The repo's Phase 2 dataset is exactly this: sleeves braided at
30°/45°/55°, contraction, force, and cycles-to-failure logged per
angle (see `docs/company-roadmap.md`). Extend the same bench protocol
to one DEA stack and one TCP coil so all three classes share a single
comparable table.

### 2.4 Tendons & transmission

**Open questions**

- What is the friction budget of a full-body tendon network — summed
  over every bend from motor to joint — and at what total bend angle
  does tension control become impractical?
- Braided conduit vs PTFE liner vs open pulley routing: which wears
  slowest, and which is field-replaceable?
- Should tension be sensed at the motor, at the joint, or both — and
  what does each choice do to control stability?

**Published work**

- Bowden-cable friction is a function of the cable's total bending
  angle, which changes as the body moves; Jeong & Cho (IROS 2015)
  showed that "loop routing" — holding total bend constant at 2π —
  makes friction predictable enough for feedforward compensation,
  achieving 4.3% RMS tension error without a tension sensor.
  http://www.cs.cmu.edu/~cga/c/0273.pdf
- Tendon–sheath mechanisms generally suffer nonlinear friction,
  tendon elongation, and backlash-like hysteresis that depends on the
  (time-varying) routing configuration — the central control problem
  for any tendon-driven body (review, 2026).
  https://onlinelibrary.wiley.com/doi/10.1002/smb2.70031
- Kenshiro's muscle-tendon complex control pairs tension-controlled
  muscles with non-linear spring "ligaments" to get active-plus-
  passive compliance from a tendon drive (Kozuki et al., BioRob
  2014).
  http://vigir.missouri.edu/~gdesouza/Research/Conference_CDs/BioRob_2014/media/files/0243.pdf

**First measurable experiment**

A single tendon routed through a conduit over a printed joint, bend
angle swept 0–360°; publish input/output tension curves (loading and
unloading) — the hysteresis loop is the deliverable.

### 2.5 Skin & surface

**Open questions**

- How thick can skin be over a tactile sensor before the sensing is
  useless — and does the answer force sensors *into* the skin rather
  than under it?
- Cast silicone, printed elastomer, or textile/fur systems: which
  survives a year of contact, cleaning, and UV, and which can be
  replaced panel-by-panel?
- Can one skin system carry appearance, tactile sensing, *and*
  thermal exchange, or do the three functions fight (insulation vs
  heat rejection vs sensor compliance)?

**Published work**

- Electronic-skin research treats stretchability, self-healing, and
  large-area integration on 3D surfaces as the three gating problems,
  with tactile modalities (pressure, strain, slip, force vector,
  temperature) expected of the skin itself (Yang et al., *Advanced
  Materials* 2019 review).
  https://pubmed.ncbi.nlm.nih.gov/31538370
- Self-healing e-skins based on reversible-bond materials can restore
  mechanical and electrical function after cracks — directly relevant
  to a body whose skin is a wear item (Chen et al., *Gels* 2022
  review).
  https://mdpi-res.com/d_attachment/gels/gels-08-00356/article_deploy/gels-08-00356.pdf
- This repo's own sensor-layer spec already commits to low-voltage
  tactile + thermal sensing integrated with the braid; see
  `docs/sensor-layer-spec.md` and `docs/braided-mesh-integration.md`.

**First measurable experiment**

Cast/print three skin coupons (silicone, TPU, textile) over the same
pressure sensor; publish force-transmission loss vs thickness, then
abrade each coupon a fixed number of cycles and repeat.

### 2.6 Sensing & proprioception

**Open questions**

- What is the minimum proprioceptive set per joint (angle only?
  angle + tension? angle + tension + temperature?) for stable
  whole-body control?
- Can the actuators self-sense well enough (DEA/HASEL capacitance,
  tendon tension) to delete dedicated joint sensors?
- How is a body-wide tactile array wired and read out without the
  harness becoming a top-three mass item?

**Published work**

- GelSight sensors turn a soft elastomer slab plus a camera into a
  high-resolution geometry sensor, inferring force, shear, and slip
  from the elastomer's deformation — the reference design for
  vision-based tactile fingertips (Yuan et al., *Sensors* 2017).
  https://doi.org/10.3390/s17122762
- HASEL actuators are inherently self-sensing (capacitance tracks
  displacement) while also self-healing — sensing integrated into
  the muscle rather than added to it (Acome et al. 2018, above).
  https://is.mpg.de/rm/en/publications/keplinger18-s-hydraulically
- Early dielectric-elastomer work already demonstrated rolls that act
  as structural elements *and* incorporate position sensing —
  self-sensing soft actuators are a two-decade-old idea still
  waiting for a body to land in (Pelrine et al., SPIE 2002).
  https://polypedal.berkeley.edu/publications/075_Pelrine_DielectricElastomerArtificialMuscleActuators_SPIE_2002.pdf
- Kengoro carries 116 sensor-driver-integrated muscle modules —
  tension sensing distributed at the muscle, not centralised
  (platform summary).
  https://humanoidversus.com/robots/tokyo-kengoro

**First measurable experiment**

Instrument one tendon-driven joint three ways (rotary encoder,
tendon tension cell, actuator self-sensing if applicable); publish
angle-estimation error of each channel against ground truth through
a load cycle.

### 2.7 Power

**Open questions**

- What runtime does the body actually need per charge for its
  intended life, and what average power does that imply backwards
  from cell energy density?
- Central pack vs split packs (torso + limbs): what do split packs
  cost in wiring and management, and buy in balance and hot-swap?
- How are multi-kilowatt peaks (balance recovery, lifting) served
  without sizing the whole pack for the peak?

**Published work**

- Industry summaries (flagged: trade press, not peer-reviewed) put
  current Li-ion at ~250–300 Wh/kg at cell level and ~150–200 Wh/kg
  at pack level, with most humanoids achieving 2–4 hours of active
  operation; they also note the weight spiral — a heavier pack raises
  joint torque demand (~20% in one analysis), which demands larger
  actuators, which demand more battery.
  https://embodiedglobal.com/en/article/battery-bottleneck-humanoid-runtime-wall-2026
  and https://www.grandpasai.com/research/robotics/category/06-power-energy.html
- Published pack examples in the same trade coverage: 0.5–2.3 kWh
  packs are typical of current humanoids, with hot-swap designs
  common precisely because runtime is short.
  https://www.robotichina.com/humanoid-robot-battery-power-bom.html

**First measurable experiment**

No new hardware needed: instrument any existing robot arm or the
Phase 2 actuator bench with a power logger through a scripted duty
cycle, and publish average/peak W and Wh per task — the first honest
row of the body's power budget (§4).

### 2.8 Thermal

**Open questions**

- Where does the heat *go* in a body that is deliberately soft and
  insulated? Conduction paths to the skin must be designed like
  circuits — what are the thermal resistances of candidate stacks?
- Is a warm-to-touch surface (a social requirement) compatible with
  using the same surface as the radiator (an engineering
  requirement)? At what ambient temperature do the two collide?
- Evaporative ("sweating"), liquid-loop, heat-pipe, or passive:
  which cooling class scales from a 40 kg body to a 300 kg body?

**Published work**

- The human reference: basal metabolic rate ≈100 W for a resting
  adult, ≈60 W/m² over ~1.7 m² of skin; holding a 37 °C core
  requires skin near 33 °C, and basal rate scales with mass to the
  2/3–3/4 power across species — a body that wants to *feel* warm
  must move roughly this much heat through its surface even before
  its actuators add theirs (UBC environmental-physics notes).
  https://c21.phas.ubc.ca/article/heat-balance-in-the-human-body-2/
- Kengoro is the existence proof that actuator heat is a design-
  driver in tendon-driven bodies: its porous aluminium skeleton
  evaporates water to cool its motors — the robot literally sweats
  (platform summary; *Science Robotics* 2017 design paper above).
  https://humanoidversus.com/robots/tokyo-kengoro

**First measurable experiment**

Wrap an actuator bench joint in candidate skin/insulation, run a
fixed duty cycle, and publish internal temperature vs time and
surface temperature at equilibrium — one curve per skin candidate.

### 2.9 Compute & control

**Open questions**

- Which control layers must be classical (balance, joint limits,
  safety) and which can be learned — and what is the failure
  behaviour of the learned layers on a body morphology no dataset
  contains?
- How much compute rides on the body vs off it, given the power and
  thermal budgets above?
- Can one body description (URDF/MJCF) serve design, simulation,
  and control without drift between the three?

**Published work**

- GR00T N1 (NVIDIA, arXiv:2503.14734) is an open vision-language-
  action foundation model for humanoids with a dual-system
  architecture — a vision-language module interpreting the scene at
  ~10 Hz and a diffusion-transformer module generating motor actions
  — trained on real-robot trajectories, human video, and synthetic
  data, and deployed on a Fourier GR-1 humanoid.
  https://arxiv.org/abs/2503.14734
- The two dominant simulation stacks for learned control are MuJoCo
  (with MJX for GPU-parallel training; soft-contact model favoured
  for contact-rich work) and NVIDIA Isaac Lab (GPU-native, thousands
  of parallel environments, favoured for locomotion at scale) —
  per a 2026 comparison of the two ecosystems (secondary summary).
  https://www.roboticscenter.ai/rl-environments/mujoco-vs-isaac-sim
- Musculoskeletal bodies specifically defeat conventional control:
  Kenshiro/Kengoro carry 64–114 joint DOF with redundant,
  antagonistic muscles, which is why the JSK lab's work pairs the
  hardware with muscle-tendon-complex control models rather than
  per-joint PID (Asano et al. 2017; Kozuki et al. 2014, above).

**First measurable experiment**

Build the Phase 1 finger-over-core demo in MuJoCo first: one
tendon-driven finger with the braid conduit modelled as a tendon
with friction; publish the sim-vs-bench tension discrepancy. That
number sizes the sim-to-real problem for the whole body.

### 2.10 Face & head

**Open questions**

- How many facial actuators does *recognisable* expression actually
  need, and which ones — is there a minimal expressive set?
- Cable-driven skin over a skull vs direct micro-actuators in the
  face: which survives, which is quieter, which is repairable?
- Where do gaze (eye cameras + eye motion), ears, and jaw speech
  motion share actuators, and where must they not?

**Published work**

- Engineered Arts' Ameca is the commercial reference for expressive
  heads: 27 actuated DOF in face and head under silicone skin, 50+
  programmed expressions (secondary source — aggregator summary of
  manufacturer data).
  http://aiwiki.ai/wiki/engineered_arts_ameca
- A 2026 *Frontiers in Robotics and AI* study transferring human
  expressions to a humanoid robot (Ameca) found transfer feasible
  but mechanically constrained: surprise and fear were recognised at
  moderate rates while anger (12.5%) and disgust (22.5%) were poorly
  recognised on the robot — actuator limits, not software, were the
  bottleneck.
  https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2026.1798227/full

**First measurable experiment**

A single-expression bench: one brow or one mouth corner driven two
ways (servo + tendon vs micro linear actuator) through the same
silicone coupon; publish displacement, force, noise, and cycles to
visible skin wear.

### 2.11 Hands

**Open questions**

- How many DOF per hand does the body's task list justify — and what
  is the grasp-success cost of each DOF removed?
- Direct-drive fingers (motors in hand) vs tendon drive from the
  forearm (light hand, heavy routing): which for a body whose arms
  also carry its social gestures?
- What fingertip force is enough, and what tactile resolution at the
  fingertip changes manipulation policy?

**Published work**

- LEAP Hand (Shaw et al., arXiv:2309.06440) is the open reference:
  an anthropomorphic hand with a novel knuckle mechanism preserving
  dexterity in all finger poses, ~30% larger than a human hand,
  assembled in 4 hours for ~$2,000 from off-the-shelf and printed
  parts, with URDF, assembly instructions, and sim2real pipeline
  released.
  https://arxiv.org/abs/2309.06440
- The tendon alternative is the musculoskeletal route of §2.4/§2.9:
  Kenshiro/Kengoro-class hands are tendon-driven from proximal
  motors, accepting Bowden friction in exchange for a light,
  human-proportioned hand.

**First measurable experiment**

The roadmap's Phase 2 tendon-conduit benchmark *is* the hand
experiment at one-joint scale: braided conduit vs stock cable guide
on a low-cost open arm, friction and cycle life logged.

### 2.12 Spine & torso

**Open questions**

- Rigid torso, 3-DOF waist, or many-vertebra spine: what does each
  additional spine DOF buy in reach and naturalness, and cost in
  control and structural margin?
- The torso carries the body's largest loads *and* its battery and
  compute in most designs — which of those should move out first as
  size grows?
- Can spine stiffness be modulated (stiff to lift, soft to hug) with
  tendon tension alone?

**Published work**

- Kenta (UTokyo) is the tendon-driven reference: a ten-jointed spine
  with rubber disks between vertebrae, driven by forty muscles with
  tension sensors, explicitly modelled on the human spine
  (Mizuuchi et al., IROS 2002).
  http://mizuuchi.lab.tuat.ac.jp/~ikuo/jsk/pdf/iros2002.pdf
- The same lab's earlier flexible-spine robot used five vertebrae of
  3 DOF each separated by silicone disks, controlled by eight
  tendons — variable flexibility as the design goal (IROS 2001).
  http://mizuuchi.lab.tuat.ac.jp/~ikuo/jsk/pdf/iros2001.pdf
- Acroban explored a bio-inspired vertebral column for compliance
  and semi-passive dynamics in locomotion — the spine as an energy
  store, not just a structure (Ly, Lapeyre & Oudeyer).
  https://www.labri.fr/perso/ly/publications/Acroban-locomotion.pdf
- The conservative industrial reference: DLR's Justin uses a 3-DOF
  torso with torque sensors in all joints and 1 kHz whole-body
  control — few spine DOF, very well instrumented.
  https://www.dlr.de/en/rm/research/robotic-systems/humanoids/table-justin

**First measurable experiment**

A three-vertebra bench segment, tendon-driven, load applied at the
top: publish bending stiffness vs tendon tension, and hysteresis
over a load cycle. This is buildable from Phase 1 braider output.

### 2.13 Tails & extra morphologies

**Open questions**

- For a biped, how much tail (mass × length) is needed before the
  inertial benefit measurably beats spending the same mass on ankle
  or hip actuation?
- Is the tail's bigger value dynamic (balance, turning) or social
  (expression) — and do the two want different tails (massive and
  slow vs light and fast)?
- What is the pelvic attachment's load case when a long tail is
  swung hard — and does the skeleton need a reinforced sacral
  junction designed in from the start?

**Published work**

- Libby et al. (*Nature* 2012) established the mechanism: leaping
  lizards swing their tails to redirect angular momentum and
  stabilise body pitch, and a lizard-sized robot with an active,
  sensor-feedback tail reproduced the stabilisation; they define
  "tail effectiveness" — the tailless body rotation a tail can
  stabilise — as the comparison metric, and found a modelled
  *Velociraptor* tail more effective than the lizards'.
  https://www.nature.com/articles/nature10710?error=cookies_not_supported&code=42286e04-b661-4fd9-862d-a448cc319265

**First measurable experiment**

Simulation only: take the §2.9 MuJoCo body model, add tails of
0/5/10% body mass, apply a standard push perturbation, and publish
recovery success vs tail parameters using tail effectiveness as the
metric. No hardware spend until the curve says the tail earns its
mass.

---

## 3. Scaling: 1.4 m to 2.7 m bodies

The programme spans bodies from ~1.4 m to ~2.7 m tall — a length
ratio of ~1.93× — and tens to hundreds of kilograms. Scaling is
where body plans go to die, so the relations below are stated with
their sources and their assumptions.

**Published relations**

- *Isometric baseline:* if all lengths scale by L, mass scales as
  L³ and muscle/bone cross-sections (hence force capacity) as L² —
  relative strength falls as 1/L. This is the square–cube constraint
  every larger body must engineer around.
- *What robots actually do:* a survey of bipedal robots found mass
  scaling closer to **L² than the isometric L³**, across three
  orders of magnitude of leg length — real designs cheat the cube
  law by getting relatively lighter as they grow (thinner relative
  structure, proportionally less carried equipment). The same study
  found walking velocity follows dynamic similarity, **v ∝ L^1/2**,
  and required joint torque follows **τ ∝ mL** — hence torque scales
  as ~L³ under the empirical mass law and ~L⁴ under isometric mass
  (Allometric Scaling Laws for Bipedal Robots, arXiv:2603.22560).
  https://arxiv.org/html/2603.22560v1
- *Heat:* basal metabolic rate scales as m^(2/3)–m^(3/4) while
  surface area scales as L² — larger bodies have *less* surface per
  kilogram to reject heat through, even as their actuators produce
  more of it (§2.8 source).
  https://c21.phas.ubc.ca/article/heat-balance-in-the-human-body-2/
- *Heat at the joint:* in one documented hobbyist humanoid's mass
  budget, stance knee torque ran ≈1.1 N·m per kg of body mass, and
  motor copper loss scales with current² — i.e. with torque² — so
  10% more mass means ~21% more knee heating (project documentation,
  flagged: single-project figures).
  https://kranthie.github.io/marvin-bot/guide/07-mass-proportions/

**Worked example — 1.4 m design scaled to 2.7 m (×1.93 in length)**

| Quantity | Scaling | Factor | Consequence |
|----------|---------|--------|-------------|
| Length | L | ×1.93 | Reach, step length |
| Surface area | L² | ×3.72 | Skin area, heat-rejection area, tactile area to wire |
| Mass (empirical robot law) | L² | ×3.72 | e.g. 40 kg → ~150 kg |
| Mass (isometric) | L³ | ×7.19 | e.g. 40 kg → ~290 kg |
| Joint torque (empirical) | mL with m∝L² | ×7.19 | Actuator class must change, not just size |
| Joint torque (isometric) | mL with m∝L³ | ×13.9 | Beyond most single-motor joints |
| Walking speed (dynamic similarity) | L^1/2 | ×1.39 | Bigger is faster per step, slower in cadence |
| Fall energy | mgh | ×7.2–13.9 | Structure and skin must absorb it; testing gets dangerous |

Reading of the table: the same architecture *cannot* simply be
scaled across the programme's size range. Somewhere between the two
ends, actuator class (§2.3), skeleton material (§2.1), cooling class
(§2.8), and probably spine design (§2.12) all change regime. Finding
*where* each regime breaks — with bench data, per subsystem — is a
research deliverable in itself, and the reason every experiment in
§2 is specified at a stated scale.

**Open scaling questions**

- At what body mass does evaporative cooling stop being optional?
- At what size does a tail's inertial benefit peak relative to its
  mass (§2.13)?
- Does the empirical m ∝ L² law survive the addition of skin,
  battery, and warmth requirements, which are closer to surface- or
  volume-driven than structure-driven?

---

## 4. Weight & power budget template

Every body design in this programme should carry a living budget in
this form. Rules: every row is either *measured* (with the test
named) or *estimated* (with the source named) — never silently
either; the totals must close (sum of rows = scale weight, within
5%) before any part is ordered.

| Subsystem | Mass budget (kg) | Mass actual (kg) | % of total | Avg power (W) | Peak power (W) | Heat to reject (W) | Source / test |
|-----------|------------------|------------------|------------|---------------|----------------|--------------------|---------------|
| Skeleton | | | | — | — | — | |
| Joints (bearings, housings) | | | | — | — | — | |
| Muscles / actuators | | | | | | | |
| Tendons & transmission | | | | — | — | — | |
| Skin & surface | | | | | | | |
| Sensing (tactile, encoders, cameras) | | | | | | | |
| Power (cells, BMS, distribution) | | | | — | | | |
| Thermal (pumps, pipes, radiators) | | | | | | — | |
| Compute & control electronics | | | | | | | |
| Face & head (actuation, eyes) | | | | | | | |
| Hands | | | | | | | |
| Spine actuators (if separate) | | | | | | | |
| Tail / extra morphology | | | | | | | |
| Wiring harness & connectors | | | | — | — | — | |
| Fasteners & misc (+10% contingency) | | | | — | — | — | |
| **Total** | | | **100%** | | | | |

Derived checks every filled budget must pass:

- **Runtime:** total stored energy (Wh) ÷ average power (W) ≥ target
  runtime, with the duty cycle named.
- **Torque closure:** worst-case joint torque from total mass and
  geometry (§3 relations) ≤ actuator continuous torque at that
  joint, with margin stated.
- **Thermal closure:** total heat to reject ≤ demonstrated surface
  rejection at the design surface temperature (§2.8 experiment).
- **Mass closure:** sum of actuals within 5% of a scale, or the
  missing mass is a named row, not a surprise.

---

## 5. How to use this map

Each §2 experiment is sized to be a single research-queue item.
When an experiment is run, its published result replaces the
corresponding open question's guesswork — update this map with the
measured number and the link. A question that survives two
experiments unchanged is probably the wrong question; rewrite it.
