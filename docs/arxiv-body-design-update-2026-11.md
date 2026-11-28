# arXiv Body-Design Update — November 2026

**Date:** 2026-11-28
**Scope:** Body *design* research from arXiv, prioritising 2024–2026:
musculoskeletal humanoid builds, compliant and bearing-free joints,
hands, spines and torsos, tails, morphology design methods, and
soft-rigid hybrid architectures. Actuator materials, sensing, and
control papers are covered by sibling sweeps; this one is about the
shape of the body itself.
**Method:** arXiv API queries run 2026-11-28 across the topic areas
below (~215 results screened, 35 papers included). Every entry was
read at abstract level or better. Dates are arXiv submission dates.
**Companion docs:** this update is written against
`docs/body-plan-research-map.md` (cited as "the map, §x.y") and
`docs/skeleton-materials-comparison.md`.

## Headline findings

1. **The muscle is becoming a module.** The newest musculoskeletal
   work treats each muscle as a standardised, swappable unit —
   QDD motor modules (arXiv:2611.24279), LEGO-compatible pneumatic
   muscle bricks (arXiv:2610.40285) — which is the map's "muscle
   cartridge" idea (§2.3) arriving from the field, with hardware.
2. **Linkage-driven hands are mounting a serious challenge to tendon
   drive.** Two 2026 hands (Torch-Hand, PHD-Hand) argue explicitly
   that tendons lose on cost, maintenance, and durability, and reach
   3 DOA per digit with linkages and flexure hinges instead. The
   tendon camp answered with better tooling (PACT, Aero Hand Open),
   not with denial. Our hand choice is now a genuine fork, not a
   default.
3. **Variable stiffness has moved from actuators into structure.**
   Locking cells (950% stiffness change per unit, no holding power),
   beaded-string jamming joints, tensegrity legs, and ligament-linked
   carpal bones all modulate stiffness mechanically — directly
   relevant to the map's open question of variable joint stiffness
   without a dedicated actuator per joint (§2.2).
4. **Morphology design is becoming computational and open.** BRIDGE
   open-sources a whole humanoid designed by morphology-control
   co-design; LEGO learns the design space itself from existing
   mechanisms; and tendon *routing* — our §2.4 bottleneck — now has a
   3D optimisation method that handles wire crossings.
5. **The spine is the gap.** In two years of arXiv, essentially no
   new articulated-spine or torso-structure work for humanoids
   appeared. The map's spine references (Kenta, Acroban) remain the
   state of the art by default. That is either a warning or an open
   field; §4 below lays out what little exists.

---

## 1. Musculoskeletal humanoids: builds, muscle modules, tendon routing

### QDD-MM: A Simple and Compact Open-Source Muscle Module with Quasi-Direct-Drive Motor for Tendon-driven Robots
- **arXiv:** 2611.24279 — https://arxiv.org/abs/2611.24279 (2026-11-18)
- **What was built:** an open-source muscle unit for tendon-driven
  robots built around a quasi-direct-drive motor. Low gear ratio
  gives backdrivability and actuation speed that earlier geared
  muscle modules lacked; because a QDD motor senses force through
  current, the module drops the dedicated force sensor entirely.
  It supports wire exit in multiple directions and module-to-module
  connection, so the same unit serves different muscle arrangements.
- **So what for Xynthetix:** this is the closest published artefact
  to the map's replaceable muscle cartridge (§2.3, §2.4). The lesson
  cuts both ways: standardising the muscle unit is clearly the
  direction of travel, but QDD-MM standardises around a *motor* —
  a DEA or McKibben cartridge standard would need its own
  mechanical/pneumatic/electrical interface definition, and nobody
  has published one. First-mover opportunity, noted in §8.

### Characteristics, Management, and Utilization of Muscles in Musculoskeletal Humanoids: Empirical Study on Kengoro and Musashi
- **arXiv:** 2602.08518 — https://arxiv.org/abs/2602.08518 (2026-02-09)
- **What it is:** the UTokyo JSK lab's consolidated account of a
  decade of musculoskeletal humanoids, classifying muscle behaviour
  into five properties — redundancy, independency, anisotropy,
  variable moment arm, and nonlinear elasticity — and organising the
  advantages, disadvantages, and management techniques (muscle
  grouping, body-schema learning, reflex control) that follow from
  each combination.
- **So what for Xynthetix:** the single best reference for what a
  tendon-driven body is actually like to live with, from the only
  lab that has operated several for years. The five-property frame
  belongs in our body-plan vocabulary: any Xynthetix muscle
  arrangement should be specifiable in those terms, and the map's
  §2.4 tendon questions should be re-read against the anisotropy and
  variable-moment-arm properties before the next design pass.

### Design Optimization of Musculoskeletal Humanoids with Maximization of Redundancy to Compensate for Muscle Rupture
- **arXiv:** 2502.12803 — https://arxiv.org/abs/2502.12803 (2025-02-18)
- **What was done:** muscle *arrangement* is optimised for a failure
  criterion — maximise the minimum joint torque still available
  after any single muscle ruptures. Applied to Musashi's elbow in
  simulation, design policies extracted, and the result confirmed on
  the real robot.
- **So what for Xynthetix:** redundancy is usually argued as a
  control convenience; this makes it a *survivability spec* with an
  objective function. For bodies meant to operate daily for years,
  "keeps moving with one muscle dead" is a design requirement we can
  now copy as a method: arrangement optimisation with a rupture
  constraint belongs in the muscle-layout step of the body plan
  (map §2.3), alongside the cartridge idea — cartridges make repair
  fast, redundancy makes repair non-urgent.

### MUSBRIC: LEGO-Compatible Pneumatic Muscle Bricks for Reconfigurable Musculoskeletal Robots
- **arXiv:** 2610.40285 — https://arxiv.org/abs/2610.40285 (2026-10-29)
- **What was built:** fibre-reinforced extensile pneumatic muscles
  given LEGO-compatible endcaps, turning each muscle into a reusable
  brick that plugs into standard LEGO structure; a MuJoCo simulator
  with experimentally identified actuator behaviour accompanies it.
  An elbow prototype validated load-dependent flexion/extension,
  pulley-guided routing for reversible motion, and a mechanical stop
  for posture stability.
- **So what for Xynthetix:** a working demonstration that
  *prototyping* a musculoskeletal body can be a kit exercise rather
  than a fabrication project. For Phase 2-scale experiments (the
  map's bench segments, §2.12's three-vertebra test), a brick-style
  muscle with a characterised sim twin is exactly the iteration
  speed we want — and the fibre-reinforced extensile muscle is a
  braided-structure product, which is our own supply chain.

### PANDORA: The Open-Source, Structurally Elastic Humanoid Robot
- **arXiv:** 2407.18558 — https://arxiv.org/abs/2407.18558 (2024-07-26)
- **What was built:** a full open-source humanoid whose structural
  elements are mostly 3D-printed compliant materials. Instead of
  putting elasticity inside the actuator, the *structure itself* is
  elastic under load — cutting cost, fabrication time, and assembly
  complexity, at the price of harder state estimation and control.
  The paper documents mechanical/electrical subsystems, sensor
  placement, and the measured effect of the structural elasticity.
- **So what for Xynthetix:** the strongest published counterpoint to
  the skeleton doc's stiffness-first framing. Our skeleton comparison
  scores printed polymers poorly on stiffness per weight — PANDORA
  argues that is the wrong axis when compliance is a *feature* the
  body plan wants anyway (map §2.1/§2.2: "compliance is an
  interface"). A structurally elastic skeleton will not suit a
  100 kg+ body, but for small bodies and for limb segments it is a
  real option the skeleton doc should acknowledge explicitly.

### Joint-Space Control of a Structurally Elastic Humanoid Robot
- **arXiv:** 2411.11734 — https://arxiv.org/abs/2411.11734 (2024-11-18)
- **What was done:** the control half of PANDORA: a disturbance
  observer modelled from an ideal elastic actuator treats the
  printed structure's model variation as a disturbance, so
  mechanical designers can iterate printed linkages *without*
  re-identifying the system or retuning joint control each time.
- **So what for Xynthetix:** included because it answers the obvious
  objection to printed/elastic structure — "you'll never keep it
  tuned." If control absorbs structural variation, the
  makerspace-fabrication advantage of printed skeletons (skeleton
  doc §5, repairability) survives contact with control engineering.
  It also sets a design rule: choose structure and joint control as
  a pair, not sequentially.

---

## 2. Compliant, bearing-free, and variable-stiffness joints

### RoboANKLE: Design, Development, and Functional Evaluation of a Robotic Ankle with a Motorized Compliant Unit
- **arXiv:** 2510.14414 — https://arxiv.org/abs/2510.14414 (2025-10-16)
- **What was built:** a powered transtibial prosthesis ankle with
  full push-off assistance: an energy-store-and-extended-release
  mechanism plus a novel extra energy-storage mechanism, sized from
  kinematic/kinetic analysis to reproduce a natural ankle torque
  profile within a RoM, weight, and autonomy budget.
- **So what for Xynthetix:** the ankle is the joint where our body
  plan's torque problem and energy problem meet (map §2.2, §3).
  RoboANKLE is a worked example of the passive-elastic answer:
  store energy in structure during stance, release it at push-off,
  and let the motor top up rather than supply peak torque. Any
  Xynthetix ankle design should be benchmarked against this
  store-and-release pattern before defaulting to a bigger motor.

### Programmable Locking Cells (PLC) for Modular Robots with High Stiffness Tunability and Morphological Adaptability
- **arXiv:** 2509.07916 — https://arxiv.org/abs/2509.07916 (2025-09-09)
- **What was built:** a modular tendon-driven unit whose joints
  mechanically interlock under cable tension, switching discretely
  between compliant and firm states — up to 950% stiffness change
  per unit, no continuous holding power, and no damage susceptibility
  in the firm state under high payload. Units assemble into larger
  morphologies.
- **So what for Xynthetix:** the cleanest answer yet to the map's
  §2.2 question "can joint stiffness be variable without a dedicated
  actuator per joint?" — yes, by *locking*, with one shared tendon
  doing the switching. A PLC-like cell is also a candidate spine
  vertebra (§4): a torso that locks firm to lift and unlocks soft to
  hug is precisely the map's §2.12 stiffness-modulation question,
  and this is a mechanism, not a hope.

### Tensegrity-based Robot Leg Design with Variable Stiffness
- **arXiv:** 2504.19685 — https://arxiv.org/abs/2504.19685 (2025-04-28)
- **What was built:** a robot leg whose compliance comes from
  tensegrity structure — cables in tension, struts in compression —
  with antagonistic elements actively modulating leg stiffness the
  way animal muscle pairs do, and tendons/ligaments acting as
  energy-storing springs.
- **So what for Xynthetix:** tensegrity is the structural language
  closest to a braided body: tension networks over compression
  members is what our woven tissue over a skeletal core already is
  (map §1). This paper gives that intuition a leg-scale mechanism
  with active stiffness control, and a candidate architecture for
  lower limbs where shock absorption matters more than positional
  precision.

### Compliant Beaded-String Jamming For Variable Stiffness Anthropomorphic Fingers
- **arXiv:** 2502.04190 — https://arxiv.org/abs/2502.04190 (2025-02-06)
- **What was built:** a compliant joint-jamming mechanism for
  anthropomorphic fingers — beaded strings that jam under tension
  to stiffen the joint, designed to keep residual compliance (the
  failure of most jamming approaches), avoid bulk, and respond
  faster than layer/granular jamming.
- **So what for Xynthetix:** variable stiffness at *finger* scale,
  where a per-joint actuator is least affordable (map §2.11). Pairs
  with the PLC result above: locking/jamming is emerging as the
  general mechanism family for stiffness modulation across scales,
  from fingers to (potentially) spines.

### Anthropomimetic Soft Robotic Forearm with Independently Articulated Carpal Bones Enabling Human-Like Adaptive Stiffness Modulability
- **arXiv:** 2609.29176 — https://arxiv.org/abs/2609.29176 (2026-09-24)
- **What was built:** an anatomically accurate soft forearm with
  eight independently movable carpal bones joined by ligaments,
  22 actuated muscles, and compliant fingertips. Wrist stiffness was
  measured under four muscle activation patterns across three
  skeleton variants — real carpals, a fused proximal row, and a
  plain ellipsoidal skeleton — isolating what the carpal
  architecture itself contributes to stiffness anisotropy (e.g. low
  stiffness along the dart-throwing direction under finger-muscle
  activation).
- **So what for Xynthetix:** rare and valuable: an *ablation study
  of anatomy*. It demonstrates that a ligament-linked multi-bone
  joint produces stiffness behaviour a single fused joint cannot,
  and measures the difference. For our wrist design (map §2.11/§2.2)
  this is the evidence that copying the carpal trick is worth its
  complexity for manipulation-heavy hands — and a template for how
  to test anatomical copying elsewhere: build the fused version too,
  and measure both.

### Design of a Biomimetic Joint-Covering Skin with Tissue-Like Structure to Enhance Proprioception in a Musculoskeletal Humanoid
- **arXiv:** 2608.23304 — https://arxiv.org/abs/2608.23304 (2026-08-24)
- **What was built:** a layered, tissue-like skin covering the
  joints of the musculoskeletal humanoid Musashi-W, embedding
  pressure- and stretch-sensitive elements in the joint-covering
  tissue; its proprioceptive contribution was evaluated both alone
  and fused with muscle sensing.
- **So what for Xynthetix:** a body-design point more than a sensing
  one: the joint covering is a *structural* component of the body
  plan — it has to flex, protect, and now also sense. It validates
  designing skin-over-joint as its own subsystem interface (map
  §2.2/§2.5/§2.6 boundary) rather than an afterthought stretched
  over finished joints, and it is directly relevant to a braided
  joint covering, which is a natural Xynthetix part.

---

## 3. Hands: the tendon-vs-linkage fork

The hand literature in 2025–2026 is the most active body-design area
on arXiv, and it has split into camps. The map (§2.11) framed the
choice as direct-drive vs tendon drive; the field has added a third
contender — linkage drive — and started arguing in public.

### A fully articulated humanoid dexterous hand with human-level joint structure enabled by linkage-based actuation (Torch-Hand)
- **arXiv:** 2610.36789 — https://arxiv.org/abs/2610.36789 (2026-10-27)
- **What was built:** a 21-DOF hand replicating the human joint
  structure — five-DOF thumb with multi-axis CMC motion, four DOF
  per finger — driven entirely by linkages rather than tendons,
  targeting the trade-off among kinematic fidelity, robustness,
  load capacity, and control simplicity.
- **So what for Xynthetix:** the strongest statement of the linkage
  case at full anthropomorphic fidelity. If a hand must survive
  daily body use with minimal maintenance (our bodies are not lab
  demos), Torch-Hand's argument — tendons are the maintenance
  problem — has to be answered, not ignored.

### PHD-Hand: A Printable Humanoid Dexterous Hand with Linkage-Driven 3-DOA Digits
- **arXiv:** 2610.29030 — https://arxiv.org/abs/2610.29030 (2026-10-21)
- **What was built:** a printable linkage-driven hand with three
  degrees of actuation per digit, built around a novel flexure
  hinge and elastic drive elements. The paper opens by naming
  tendon-driven designs' weaknesses directly: high cost, demanding
  maintenance, poor reliability, short durability.
- **So what for Xynthetix:** two imports. First, the *flexure hinge*
  as the hand's joint — a printed, bearing-free joint at finger
  scale, connecting §2's compliant-joint theme to the hand.
  Second, a fabrication stance aligned with ours: printable first.
  PHD-Hand is the design to beat if we choose linkage, and its
  flexure data is the comparison set for a braided-tendon finger.

### Ruka-v2: Tendon Driven Open-Source Dexterous Hand with Wrist and Abduction for Robot Learning
- **arXiv:** 2603.26660 — https://arxiv.org/abs/2603.26660 (2026-03-27)
- **What was built:** the second generation of the open-source Ruka
  hand (v1: 11 DOF, under $1,300 in parts): adds a decoupled 2-DOF
  parallel wrist (flexion/extension plus radial/ulnar deviation) and
  finger abduction/adduction — the two DOF sets v1 lacked for
  human-like behaviour — while staying fully open-source and
  tendon-driven, with a data-driven controller that models tendon
  dynamics.
- **So what for Xynthetix:** the tendon camp's flagship open
  platform, and a lesson in iteration honesty: the v1→v2 delta is
  precisely "the wrist matters as much as the fingers" — which
  compounds the carpal-forearm result above (§2). If we build a
  tendon hand, Ruka-v2 is the baseline to fork or beat, and its
  wrist is the part to study first.

### RUKA: Rethinking the Design of Humanoid Hands with Learning
- **arXiv:** 2504.13165 — https://arxiv.org/abs/2504.13165 (2025-04-17)
- **What was built:** a tendon-driven hand from 3D-printed parts and
  off-the-shelf components: five fingers, 15 underactuated DOF,
  compact and low-cost, with learning-based control used
  deliberately to relax the hardware precision requirements that
  make tendon hands expensive.
- **So what for Xynthetix:** the design philosophy matters more than
  the specs: *let learning absorb hardware sloppiness* is the same
  bargain PANDORA's disturbance observer strikes for structure
  (§1). For a makerspace-built body, that bargain — cheap compliant
  hardware plus learned compensation — is likely our whole
  fabrication strategy, stated here for hands.

### ORCA: An Open-Source, Reliable, Cost-Effective, Anthropomorphic Robotic Hand for Uninterrupted Dexterous Task Learning
- **arXiv:** 2504.04259 — https://arxiv.org/abs/2504.04259 (2025-04-05)
- **What was built:** a 17-DOF tendon-driven anthropomorphic hand
  with integrated tactile sensors, designed for *uninterrupted*
  operation in learning experiments — reliability and fast assembly
  (under a day) treated as first-class design goals.
- **So what for Xynthetix:** ORCA's contribution to the body plan is
  its reliability framing: a hand on a body that lives with people
  fails socially when it is always in the shop. Its tendon routing
  and wear choices, made under an uptime requirement, are the
  closest published analogue to our service-life thinking (map
  §2.11's "what wears out first" question).

### Tactile SoftHand-A: 3D-Printed, Tactile, Highly-underactuated, Anthropomorphic Robot Hand with an Antagonistic Tendon Mechanism
- **arXiv:** 2406.12731 — https://arxiv.org/abs/2406.12731 (2024-06-18)
- **What was built:** a 3D-printed five-finger hand in the
  Pisa/IIT SoftHand line: highly underactuated, with a dual-tendon
  antagonistic mechanism that can actively open *and* close, select
  which interphalangeal joints a grasp engages, and fully
  3D-printed vision-based tactile sensors inside the fingers.
- **So what for Xynthetix:** underactuation as a deliberate body
  choice: one mechanism, many grasps, minimal actuators — the
  opposite end of the DOF axis from Torch-Hand. The map's §2.11
  question "what is the grasp-success cost of each DOF removed?"
  gets partial data here: with the right tendon mechanism, the cost
  is lower than intuition suggests.

### Aero Hand Open: A Simulation-Ready Tendon-Driven Hand for Dexterous Manipulation Learning
- **arXiv:** 2608.28578 — https://arxiv.org/abs/2608.28578 (2026-08-28)
- **What was built:** an open tendon-driven anthropomorphic hand
  whose headline deliverable is its simulator: a model that
  reproduces the cable transmission — including the underactuation
  coupling that makes tendon hands hard to learn on — so policies
  train against the real transmission behaviour.
- **So what for Xynthetix:** names our §2.4/§2.9 problem exactly:
  tendon hands are cheap *because* the transmission is coupled, and
  coupled transmissions are what simulators omit. A simulation-ready
  tendon model is infrastructure our whole tendon-driven body needs,
  not just the hand — the same cable-coupling modelling applies to
  every braided conduit run in the body.

### Design, Control, and Teleoperation of a Dexterous Robotic Hand with Soft-Rigid Hybrid Fingers
- **arXiv:** 2611.32582 — https://arxiv.org/abs/2611.32582 (2026-11-24)
- **What was built:** a five-finger tendon-driven hand whose fingers
  combine structural compliance with a rigid skeleton — soft-rigid
  hybrid fingers — such that linear control suffices for soft
  grasping; validated across teleoperated manipulation tasks.
- **So what for Xynthetix:** the hybrid-finger result generalises:
  compliance placed in the *finger structure* simplifies control
  everywhere it is tried (see also PANDORA, §1). It is also a
  candidate finger architecture for a braided covering over a rigid
  phalanx core — our tissue-over-skeleton pattern at finger scale.

### A 21-DOF Humanoid Dexterous Hand with Hybrid SMA-Motor Actuation: CYJ Hand-0
- **arXiv:** 2507.14538 — https://arxiv.org/abs/2507.14538 (2025-07-19)
- **What was built:** a 21-DOF hand with a hybrid tendon system:
  DC-motor modules drive flexion, shape-memory-alloy modules drive
  extension and abduction, using high-strength fishing line as
  tendons over a 3D-printed AlSi10Mg metal frame replicating the
  human skeletal/tendon layout.
- **So what for Xynthetix:** two notes. The hybrid split — powered
  flexion, SMA return — matches how bodies actually budget force
  (grip is the power direction). And the printed *metal* frame is a
  data point for the skeleton doc: AlSi10Mg printing appears in the
  field exactly where printed polymer runs out of strength at small
  scale.

### A Sensorless, Inherently Compliant Anthropomorphic Musculoskeletal Hand Driven by Electrohydraulic Actuators
- **arXiv:** 2603.24357 — https://arxiv.org/abs/2603.24357 (2026-03-25)
- **What was built:** a musculoskeletal hand powered entirely by
  remote Peano-HASEL electrohydraulic actuators in the forearm —
  keeping electricity away from the grasping interface — with a 1:2
  pulley routing that amplifies the actuators' limited contraction
  into useful tendon travel. Compliance is inherent; sensing is via
  the actuators' self-sensing.
- **So what for Xynthetix:** the soft-actuator camp's hand entry,
  and a routing lesson with numbers attached: when your muscle's
  strain is small, the *transmission ratio* becomes a body-design
  variable (map §2.4). It also demonstrates the proximal-mass
  strategy — actuators in the forearm, slim hand — that our body
  plan already favours.

### PACT: Pose-Robust Actuation Co-Design for Tendon-Driven Robotic Hands
- **arXiv:** 2611.05302 — https://arxiv.org/abs/2611.05302 (2026-11-03)
- **What was done:** a co-design framework that optimises tendon
  routing, moment arms, and capstan dimensions against
  pose-dependent force requirements and drivetrain bandwidth, with
  a max-min objective that maximises task-force coverage at the
  *weakest* pose. On a 4-DOF finger it produced an asymmetric N+1
  tendon topology with QDD actuators, achieving 0.88–1.00
  task-force coverage across eight poses and ~5 Hz predicted
  minimum joint bandwidth.
- **So what for Xynthetix:** tendon routing stops being craft and
  becomes optimisation — and the objective is the right one
  (worst-pose force, not average). Together with the wire-arrangement
  optimiser in §6, this is the toolchain our tendon layouts should
  be produced by, and its weakest-pose criterion belongs in our
  design reviews verbatim.

---

## 4. Spines, torsos, and heads: the thin chapter

An honest result of this sweep: **articulated spine and torso
structure for humanoids is nearly absent from arXiv in 2024–2026.**
Targeted queries returned no new multi-vertebra humanoid spine
builds. The map's references — Kenta's ten-jointed tendon spine
(2002), the five-vertebra flexible spine (2001), Acroban — remain
the literature. Two adjacent results did appear:

### Communicative Efficiency of Single vs. Multi-Axis Robot Neck Motion
- **arXiv:** 2607.07390 — https://arxiv.org/abs/2607.07390 (2026-07-08)
- **What was done:** an information-theoretic study of the neck as a
  communication channel: 84 video stimuli across 3 rotational DOF
  on a robotic neck platform, measuring information transmitted
  (Shannon entropy of pixel change) against energy, validated by a
  perceptual study. Humans use one axis per gesture; robots are not
  so constrained, and the paper quantifies what extra axes buy.
- **So what for Xynthetix:** the head/neck is part of the body plan
  (map §2.10), and this is the first framework we have seen that
  prices neck DOF in *information per joule* — a defensible way to
  decide how many neck axes a social body actually needs, instead
  of copying human anatomy by default.

### Articulated Humanoid Head for a Robot Receptionist Capable of Natural Human Interaction
- **arXiv:** 2607.17042 — https://arxiv.org/abs/2607.17042 (2026-07-19)
- **What was built:** an articulated humanoid head designed for
  natural interaction in a receptionist role — the face/head as an
  integrated mechanical assembly rather than a display shell.
- **So what for Xynthetix:** modest but real: a current data point
  that head articulation for social signalling is being engineered
  as mechanism, at the end of the neck whose DOF budget the study
  above prices. The map's §2.10 actuation-density-vs-mass question
  remains open; these two papers are its newest inputs.

**Implication for the queue:** the spine gap cuts two ways. Either
the field has quietly decided rigid torsos plus a 3-DOF waist are
enough (the industrial consensus the map already records), or spine
work has moved to venues arXiv doesn't index well. Before Xynthetix
commits to a spine architecture, a targeted non-arXiv pass
(conference proceedings, DLR/UTokyo lab pages) is owed — added to
the new-questions list in §8. Meanwhile the PLC locking cell (§2)
is the most promising *mechanism* lead for a stiffness-modulating
torso.

---

## 5. Tails and extra morphologies

### Enhancing Balance and Posture in Material Handling Tasks with a Wearable Robotic Tail
- **arXiv:** 2611.11662 — https://arxiv.org/abs/2611.11662 (2026-11-08)
- **What was demonstrated:** a wearable robotic tail used as a
  dynamic counterbalance by ten human participants in a
  shelf loading/unloading task. Versus no tail, the active tail cut
  centre-of-pressure peak displacement by >20 mm, trunk motion by
  4.3°, and erector spinae / gastrocnemius activation by >9% /
  >20%. The passive tail helped less — active control is where the
  benefit lives.
- **So what for Xynthetix:** the first numbers we have for the map's
  §2.13 question at human scale, albeit wearable rather than
  built-in: an active tail measurably unloads the spine and legs
  during lifting. It also reframes the tail's value proposition —
  the strongest measured benefit here is *ergonomic* (less back
  strain), not acrobatic. For a body that lifts and carries daily,
  that may be the tail's real job.

### Learning Rapid Turning, Aerial Reorientation, and Balancing using Manipulator as a Tail
- **arXiv:** 2407.10420 — https://arxiv.org/abs/2407.10420 (2024-07-15)
- **What was demonstrated:** a 6-DOF manipulator mounted as a
  quadruped's tail, controlled by reinforcement learning, serving
  double duty as tail and arm — improving rapid turning, aerial
  reorientation, and balancing without a dedicated tail's dead
  weight and cost.
- **So what for Xynthetix:** the dual-use answer to the map's
  tail-mass question (§2.13: "how much tail before the benefit beats
  spending the mass elsewhere?"). If the appendage also manipulates,
  its mass is paid once for two functions — the interface rule
  "a gram is paid four times" cuts in our favour for once. A
  tail-that-is-also-a-limb belongs in the morphology options for
  non-humanoid body plans.

### Humanoid SRL: Augmenting Humanoids with Supernumerary Limbs for Coordinated Loco-Manipulation
- **arXiv:** 2610.25628 — https://arxiv.org/abs/2610.25628 (2026-10-19)
- **What was demonstrated:** a supernumerary arm integrated into a
  humanoid, with model-based trajectory optimisation coordinating
  the extra limb with whole-body balance; hardware experiments in
  two configurations show the added limb expanding the feasible
  action space (manipulation and support simultaneously) beyond the
  native two-arm morphology.
- **So what for Xynthetix:** extra morphologies are leaving the
  speculative shelf. For bodies whose forms are not constrained to
  the human template, SRL is the published proof that an added limb
  is a control problem with a solution, not a fantasy — and its
  whole-body coordination framing is the one our tail work should
  adopt.

---

## 6. Morphology design methods: co-design, optimisation, lightweighting

### BRIDGE: An Open-Source Humanoid Platform via Morphology-Control Co-Design for Physical AI
- **arXiv:** 2609.03497 — https://arxiv.org/abs/2609.03497 (2026-09-03)
- **What was done:** a data-driven morphology-control co-design
  framework that optimises humanoid morphology for human-like
  movement, scored by a new metric combining kinematic retargeting
  fidelity to human motion with dynamic tracking performance. It
  reports state-of-the-art results against baseline humanoids
  (Bumi, K1, ToddlerBot), and the resulting design — Bridge — is
  realised as an open-source humanoid platform.
- **So what for Xynthetix:** two gifts. A *method* (optimise the
  body against motion data, not intuition) and a *comparable*: an
  open humanoid whose proportions were chosen by that method, so
  our proportion choices can be diffed against a defensible
  baseline. It also pressures the map's §3 scaling discussion:
  co-design per size class may be the practical answer to "one
  architecture cannot span 1.4–2.7 m" — design each size with the
  optimiser, share the toolchain.

### Toward Humanoid Brain-Body Co-design: Joint Optimization of Control and Morphology for Fall Recovery (RoboCraft)
- **arXiv:** 2510.22336 — https://arxiv.org/abs/2510.22336 (2025-10-25)
- **What was done:** a scalable co-design framework that iteratively
  improves a shared control policy and the morphology together,
  targeted at fall recovery: a policy pretrained across many designs
  is finetuned on the high-performing morphologies, which are then
  re-scored, closing the loop efficiently.
- **So what for Xynthetix:** fall recovery is the morphology test
  that matters most for a body living in a home (a fall is the
  highest-energy event in its life). RoboCraft shows morphology can
  be optimised *for* recoverability — proportions and mass
  distribution as safety features. Our body-plan experiments (§2 of
  the map) should add a fall-recovery score to the budget template's
  closure checks.

### LEGO: Latent-space Exploration for Geometry-aware Optimization of Humanoid Kinematic Design
- **arXiv:** 2604.08636 — https://arxiv.org/abs/2604.08636 (2026-04-09)
- **What was done:** instead of hand-crafting the design space, LEGO
  learns it: screw-theory joint-axis representations of existing
  mechanical designs are embedded via isometric manifold learning
  into a compact, geometry-preserving latent space, and design
  optimisation runs inside it, with loss defined directly from
  human motion data via retargeting and Procrustes analysis.
  Demonstrated on humanoid upper-body design.
- **So what for Xynthetix:** the deepest method paper in this sweep.
  It converts "what proportions and joint axes should this body
  have?" from a drafting exercise into a search over *plausible*
  mechanisms — the latent space only contains designs resembling
  real ones. For non-human morphologies (extra joints, tails,
  non-human limb plans), a learned design space seeded with animal
  and robot mechanisms is a credible route to bodies no one would
  draft by hand.

### Evolving the Complete Muscle: Efficient Morphology-Control Co-design for Musculoskeletal Locomotion
- **arXiv:** 2604.12855 — https://arxiv.org/abs/2604.12855 (2026-04-14)
- **What was done:** co-design for musculoskeletal systems that
  evolves muscle *strength, velocity, and stiffness simultaneously*
  — a "complete muscle" morphological space — using a Spectral
  Design Evolution method to survive the exponential search space.
  Prior work optimised single attributes (usually stiffness) with
  the rest fixed.
- **So what for Xynthetix:** our muscle selection is currently a
  catalogue choice (which actuator class, which size). This says
  the physiological parameter *triple* is the design variable, and
  it is searchable. When the muscle landscape doc's comparison
  table is next revised, its axes (force/velocity/stiffness) are
  exactly this paper's evolution space — the table can become a
  design tool, not just a survey.

### Design Optimization of Three-Dimensional Wire Arrangement Considering Wire Crossings for Tendon-driven Robots
- **arXiv:** 2507.04235 — https://arxiv.org/abs/2507.04235 (2025-07-06)
- **What was done:** 3D tendon-route optimisation via multi-objective
  black-box optimisation that explicitly handles wire crossings —
  the effect most earlier work assumed away by restricting to 2D,
  constant moment arms, or no crossings. The authors note wire
  arrangement is traditionally empirical and becomes extremely
  challenging in complex structures (hands, wrists, waists).
- **So what for Xynthetix:** arguably the most directly usable paper
  in this sweep. Tendon routing is our §2.4 core problem and it runs
  through every subsystem of a braided body; a crossing-aware 3D
  optimiser is the missing tool between "route it where it fits"
  and a designed transmission. Priority follow-up: reproduce the
  formulation against one of our own routing problems (the
  three-vertebra bench segment is the right size).

### Systematic Lightweight Method for Robotics Based on Strain Energy Distribution Optimization
- **arXiv:** 2608.29146 — https://arxiv.org/abs/2608.29146 (2026-08-29)
- **What was done:** a system-level lightweighting criterion: in an
  optimal lightweight structure, strain energy per unit mass should
  be uniformly distributed. That single criterion decouples the
  system problem into per-part objectives, making whole-robot
  lightweight design tractable across many components and load
  cases.
- **So what for Xynthetix:** a companion method for the skeleton
  doc. The skeleton comparison optimises a link at a time (the
  worked femur); this optimises the *distribution* across the whole
  skeleton — which is where real mass hides (overbuilt low-stress
  parts). Uniform strain-energy density is a checkable design
  review criterion for every structural part we draw.

---

## 7. Soft-rigid hybrid architectures

### Automated design of soft-rigid hybrid robots for dynamic locomotion
- **arXiv:** 2605.29389 — https://arxiv.org/abs/2605.29389 (2026-05-28)
- **What was done:** an automated design method that jointly
  optimises a freeform soft-body shape, a stiff truss skeleton
  layout inside it, and multi-channel actuation, using a
  differentiable simulator coupling MPM (deformable body) with XPBD
  (truss elements). The optimised design was fabricated and
  reproduced its simulated walking behaviour in hardware.
- **So what for Xynthetix:** this is our body architecture — soft
  tissue over a stiff skeleton — with the design *automated*. The
  truss-layout optimisation is effectively skeleton design inside a
  soft body, and the sim-to-fabrication loop closed. Even at its
  current small scale, it is the methodological template for
  designing braided-tissue-over-core segments: optimise the core
  truss and the tissue shape together, not in sequence.

Cross-references within this update: the soft-rigid hybrid *hand*
(arXiv:2611.32582, §3) applies the same architecture at finger
scale, and PANDORA (§1) is the hybrid principle with the soft part
as primary structure. The pattern across all three: **rigid where
force flows, soft where the world touches, and the boundary between
them is a design variable** — which is the map's §1 interface
doctrine arriving independently from three directions.

---

## 8. Top 5 to read in full

1. **Characteristics, Management, and Utilization of Muscles in
   Musculoskeletal Humanoids** (arXiv:2602.08518) — the field's
   operating manual for tendon-driven bodies; everything we build
   will meet these five muscle properties.
2. **Design Optimization of Three-Dimensional Wire Arrangement
   Considering Wire Crossings** (arXiv:2507.04235) — the routing
   optimiser our tendon layouts need; most directly actionable
   method in the sweep.
3. **BRIDGE** (arXiv:2609.03497) — an open humanoid designed by
   co-design, with a fidelity metric we can adopt; our proportions
   should be diffed against it.
4. **Anthropomimetic Soft Robotic Forearm with Articulated Carpal
   Bones** (arXiv:2609.29176) — the anatomy-ablation method:
   proof that ligament-linked multi-bone joints earn their
   complexity, measured.
5. **QDD-MM** (arXiv:2611.24279) — the muscle-as-module standard,
   open-source; the interface definition our own cartridge standard
   will be compared against.

## 9. Updates to the research map's open questions

**Partially answered by this sweep:**

- *§2.2 — "Can joint stiffness be variable without a dedicated
  actuator per joint?"* Yes, by locking/jamming: PLC cells (950%
  per-unit change, no holding power, arXiv:2509.07916) and
  beaded-string jamming (arXiv:2502.04190) are mechanisms, not
  proposals. The question becomes which locking family survives
  10⁶ cycles — unanswered everywhere.
- *§2.3 — "What does a replaceable muscle cartridge standard look
  like?"* Now has two reference points (QDD-MM for motors,
  MUSBRIC for pneumatics) — but both standardise the *muscle*, not
  the *socket*. The interface definition (mechanical, power,
  signal, thermal) is still unpublished by anyone.
- *§2.11 — "Direct-drive vs tendon drive for hands?"* The question
  is now three-way: linkage drive (Torch-Hand, PHD-Hand) claims the
  maintenance/reliability ground tendons were assumed to hold.
  DOF-cost data also improved: underactuated antagonistic designs
  (SoftHand-A) lose less grasp capability per removed DOF than the
  map assumed.
- *§2.13 — "How much tail before the benefit beats the mass?"*
  First human-scale numbers exist (wearable tail: >20 mm CoP
  reduction, >20% gastrocnemius unloading, arXiv:2611.11662), and
  the dual-use manipulator-tail (arXiv:2407.10420) reframes the
  accounting. Still no built-in biped tail data.
- *§2.12 — "Can spine stiffness be modulated with tendon tension
  alone?"* No new spine evidence — but PLC (§2) is a candidate
  mechanism the original question didn't have.

**New questions this sweep adds:**

- If muscle units standardise (QDD-MM, MUSBRIC), what is the
  *socket* standard for a body that mixes motor, pneumatic, and
  electrohydraulic muscles in one frame?
- Locking/jamming stiffness mechanisms: what are their cycle lives
  under load, and does jamming wear change the locked stiffness
  over time? (No paper in this sweep reports life data.)
- Linkage vs tendon hands: is there a *hybrid* — linkage fingers,
  tendon wrist — that takes the maintenance win without losing the
  proximal-mass win? Nobody in 2024–2026 published one.
- Co-design optimisers (BRIDGE, LEGO, RoboCraft) all optimise for
  motion fidelity or task success. None optimises for
  *repairability or service life* — can maintainability enter the
  objective function, or is it structurally excluded?
- The spine gap: is articulated-spine research actually dormant, or
  published where arXiv doesn't reach? A proceedings/lab-page pass
  is owed before treating Kenta (2002) as current state of the art.
- Strain-energy-uniform lightweighting (arXiv:2608.29146) assumes
  known load cases; a soft body's load cases include hugs, falls,
  and being leaned on. What is the load-case set for a *social*
  body's skeleton?

---

*Screening note: ~215 arXiv results were screened for this update;
35 papers are included. Papers whose contribution was primarily
actuator materials, sensor devices, or control algorithms were
deferred to the sibling sweeps even when body-relevant.*
