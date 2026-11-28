# arXiv Actuator Update — November 2026

**Date:** 2026-11-28. **Scope:** artificial-muscle / soft-actuator papers
on arXiv, prioritising 2024–2026, read against
[docs/artificial-muscle-landscape.md](artificial-muscle-landscape.md)
and [docs/dea-deep-dive.md](dea-deep-dive.md).
**Method:** arXiv API queries per actuator class; every paper below was
opened at abstract level at minimum. Numbers are as reported in the
abstracts — where an abstract gives no number, this doc says so rather
than guessing. Modelling/simulation-only papers are flagged as such.
**Papers covered:** 30.

## The verdict first

Nothing in the 2024–2026 arXiv record found by this sweep moves the
landscape doc's large-joint verdict:

- **No new soft-actuator force record at body scale.** No DEA paper
  reports a device force anywhere near the 66 N largest device in the
  deep dive, let alone the ~3–3.7 kN of tendon force a functional
  100 kg knee extensor needs. The hydraulic McKibben (7 kN, 15 mm OD)
  remains the only soft class with demonstrated kN force, and no new
  arXiv paper this sweep adds a second one.
- **The DEA watch triple is still unmet.** No paper found publishes a
  *device* at ≥300 kPa, ≥15% strain, ≥10⁶ cycles simultaneously.
- **Lifetime moved methodologically, not absolutely.** The strongest
  lifetime paper (2602.20963) *doubles* DEA lifetime at boundary
  operating conditions by automated parameter scanning — a method we
  can copy — but its abstract reports no absolute cycle count at
  working strain, so the 10⁵–10⁷ electrode-dependent picture stands.
- **What actually advanced in 2024–2026 is everything around the
  muscle:** self-sensing (HASEL to 20 Hz, TCP force from inductance,
  SMA pose from resistance), control (data-driven models that handle
  hysteresis well enough for antagonistic joints), manufacturing
  automation for DEA, and pneumatic infrastructure miniaturisation
  (valves inside the McKibben). The muscles themselves barely moved;
  the systems engineering around them moved a lot. That is good news
  for a programme whose bet is architecture, not a miracle material.

---

## 1. Dielectric elastomer actuators (DEA)

### 1.1 Lifetime scanning as a self-driving lab — the lifetime paper to copy
**arXiv:2602.20963** (2026-02-24) — *A Robotic Testing Platform for
Pipelined Discovery of Resilient Soft Actuators.*
https://arxiv.org/abs/2602.20963
A testing robot scans linear DEA lifetime across voltage, frequency,
electrode material concentration, and connection filler. Optimal
parameter combinations improved operational lifetime under boundary
conditions **by up to 100%** (i.e. ~2×), and the optimised actuators
were scaled up and run on a modular quadruped carrying **>100% of its
untethered body weight** in payload (>700% of combined actuator
weight). Abstract reports no absolute cycle counts.
*So what:* our docs treat DEA lifetime as a materials lottery. This
says it is partly a *search* problem: per-cartridge parameter scanning
is exactly the QA step the cartridge architecture in the deep dive
already proposes (Section 9) — this paper is the working template for
that test rig, and a Phase 0/1 bench we can build before any body.

### 1.2 Automated DEA manufacturing
**arXiv:2608.00369** (2026-08-01) — *A Robotic System for Automated
Manufacturing of Dielectric Elastomer Actuators.*
https://arxiv.org/abs/2608.00369
Robotic spin-coating + CNT electrode stamping produced **20 multilayer
DEAs, 12 dielectric layers each, mean layer thickness 55.37 ± 2.04 µm**,
cutting total process time 14.2% and removing the operator from 56.1%
of it.
*So what:* the deep dive identified electrode *process* (printed vs
hand-applied) as the lifetime lever — <10⁵ vs >10⁷ cycles. Automated,
repeatable layer/electrode formation is how that lever gets pulled at
production scale. Directly relevant to making cartridges in quantity.

### 1.3 Low-voltage thin DEA: 220 V via 8 µm layers
**arXiv:2512.17940** (2025-12-12) — *Untethered thin dielectric
elastomer actuated soft robot.*
https://arxiv.org/abs/2512.17940
Thin in-plane DEA robot, 38 mm long, 2.34 g, fully untethered. Layers
spin-coated at 50 µm and biaxially stretched to **8 µm**, giving
actuation at **220 V** (vs the 0.45–8 kV range in our landscape table),
resonant operation at **86 Hz**; bare actuator locomotion 12.36 mm/s,
untethered robot 0.5 mm/s.
*So what:* does not change force scaling (gram-scale robot), but it
attacks the other DEA objection — kilovolt electronics — from the
geometry side. Thin-layer fabrication is a cartridge-manufacturing
input, and 220 V-class drive would simplify the HV safety case for
face/skin cartridges.

### 1.4 Portable high-voltage drive electronics keep shrinking
**arXiv:2502.06166** (2025-02-10) — *Portable, High-Frequency, and
High-Voltage Control Circuits for Untethered Miniature Robots Driven
by Dielectric Elastomer Actuators.*
https://arxiv.org/abs/2502.06166
Single-channel board controls up to **1.8 kV at 0–1 kHz and weighs
2.5 g**; a 42 g untethered crawler ran a cylindrical DEA at 15 Hz
while streaming camera video.
*So what:* per-channel HV electronics at gram scale is the enabling
assumption behind distributed DEA cartridges; this is evidence the
electronics roadmap is on schedule even though the actuators are not.

### 1.5 DEA integration platform: six muscles, autonomous
**arXiv:2606.00197** (2026-05-29) — *Cuttlebot: a platform
demonstration for complex, autonomous, bio-inspired swimmers.*
https://arxiv.org/abs/2606.00197
The CORE platform drives **six DEA artificial muscles** with onboard
sensing/compute; the Cuttlebot demonstrator swims at 2.5 cm/s with
controllable force/torque output in six axes.
*So what:* multi-muscle DEA *systems* (not single devices) are starting
to appear. Still small forces — but system integration, not device
physics, was the stated bottleneck, and it is being worked.

### 1.6 Resilient silicone chemistry for DEAs
**arXiv:2603.04352** (2026-03-04) — *A Soft Robotic Demonstration in
the Stratosphere.*
https://arxiv.org/abs/2603.04352
UV-cured silicone crosslinking chemistry giving DEA operation from
**−40 °C to 120 °C** and near-vacuum; autonomous DEA grippers flown on
two stratospheric balloon missions to **23.6 km, <0.05 atm, −55 °C**.
*So what:* tangential to bodies, but the chemistry targets exactly the
failure axis our docs worry about — elastomer operating-window limits
— and the authors note it extends to adhesion and additive
manufacturing of silicones, both live problems for skin/cartridge work.

### 1.7 DEA Delta robot: electrode consistency + force modelling
**arXiv:2409.20344** (2024-09-30) — *Design, manufacturing, and inverse
dynamic modeling of soft parallel robots actuated by dielectric
elastomer actuators.*
https://arxiv.org/abs/2409.20344
DEA-actuated Delta parallel robot with angular stroke amplification.
Laser-scanned conductive-paint electrodes showed more consistent
dynamic behaviour than carbon grease (qualitative in abstract);
inverse dynamic model predicted stationary output force with **12.4%
RMSE**, trajectory tracking <2.5% RMSE.
*So what:* another vote for processed electrodes over grease, and a
worked example of model-based force prediction for a multi-DEA
mechanism — the control pattern a cartridge-driven joint would need.

### 1.8 Review: DEA modelling, control, self-sensing (2026)
**arXiv:2604.17199** (2026-04-19) — *Modeling, Control and Self-sensing
of Dielectric Elastomer Soft Actuators: A Review.*
https://arxiv.org/abs/2604.17199
Surveys physics-based and phenomenological models, four control
families, and physics-based vs data-driven self-sensing for DEA
displacement reconstruction.
*So what:* the reference to hand a control engineer joining the
programme; confirms our docs' framing that creep/hysteresis modelling,
not raw strain, is the practical DEA bottleneck.

---

## 2. HASEL / electrohydraulic actuators

### 2.1 Sensorless Peano-HASEL hand — self-sensing from current alone
**arXiv:2603.24357** (2026-03-25) — *A Sensorless, Inherently Compliant
Anthropomorphic Musculoskeletal Hand Driven by Electrohydraulic
Actuators.*
https://arxiv.org/abs/2603.24357
Musculoskeletal hand powered entirely by remote Peano-HASEL actuators
relocated to the forearm (proximal-mass strategy, electrical hazard
kept away from the grasp interface), with a **1:2 pulley** amplifying
tendon displacement against HASEL's limited contraction. Grasp
detection and contact-aware closed-loop control are achieved **by
monitoring operating current alone** — no force transducers or
encoders. Demonstrated grasp taxonomy coverage and non-destructive
grasping of a paper balloon. The design explicitly prioritises
compliance over payload.
*So what:* this is our architecture in miniature — proximal actuators,
tendon routing, self-sensing as the proprioception channel — and it
validates the sensing survey's G3 gap (muscle self-sensing missing
from our sensor spec). It also honestly confirms the trade: force is
what you give up.

### 2.2 Antagonistic HASEL + electrostatic clutches: full joint range
**arXiv:2409.11017** (2024-09-17) — *Stretchable Electrohydraulic
Artificial Muscle for Full Motion Ranges in Musculoskeletal
Antagonistic Joints.*
https://arxiv.org/abs/2409.11017
Non-stretchable HASELs paired with electrostatic clutches in an
antagonistic joint achieve **both contraction and extension** with no
displacement loss to tendon slack, with synchronised muscle/clutch
transitions at up to **3.2 Hz**. The authors note the clutch concept
transfers to other non-stretchable muscles, including McKibben.
*So what:* tendon slack at direction reversal is a real tax on every
antagonistic layout in our body plan; clutches are a published fix
that composes with both HASEL and McKibben muscles.

### 2.3 AC drive fixes HASEL's DC displacement decay
**arXiv:2401.13941** (2024-01-25) — *AC-Driven Series Elastic
Electrohydraulic Actuator for Stable and Smooth Displacement Output.*
https://arxiv.org/abs/2401.13941
Models why HASEL displacement **declines over time under constant DC
voltage**, shows AC square-wave drive holds displacement relatively
stable, and adds a series-elastic element (SE-HASEL) + PI feedback to
smooth the AC ripple and remove hysteresis; demonstrated in a rotary
joint and an MRI-compatible needle-biopsy robot concept.
*So what:* a design rule for any HASEL use in a body: budget for AC
drive and series elasticity from the start, or sustained-posture force
will sag. Our landscape doc lists HASEL strain/force but not this
drift; see corrections (§7).

### 2.4 F-HASEL: dedicated sensing electrodes push self-sensing to 20 Hz
**arXiv:2404.04071** (2024-04-05) — *High-Frequency Capacitive Sensing
for Electrohydraulic Soft Actuators.*
https://arxiv.org/abs/2404.04071
Adding an electrode pair used *exclusively* for capacitive sensing to
a Peano-HASEL gives displacement estimation during actuation **up to
20 Hz** with miniaturised, off-the-shelf circuitry and a miniature HV
supply; multi-actuator estimation circuitry demonstrated in a wearable
joint-tracking application.
*So what:* earlier HASEL self-sensing stalled above ~1 Hz. A separate
sensing electrode is a cheap, manufacturable answer — directly
applicable to a braided muscle with a sensing layer.

### 2.5 Self-sensing electrohydraulic shoulder, 2-DOF antagonistic
**arXiv:2404.04079** (2024-04-05) — *Self-Sensing Feedback Control of
an Electrohydraulic Robotic Shoulder.*
https://arxiv.org/abs/2404.04079
Antagonistic 2-DOF shoulder driven by self-sensing HASELs with the
high-voltage actuation decoupled from low-voltage sensing electrodes;
proprioceptive trajectory control in task space benchmarked against
motion capture, with **no rotary encoders**.
*So what:* shoulder-scale (not finger-scale) evidence that
encoder-free proprioception works on a real joint — relevant to our
proprioception backlog item, now partly answered by literature.

### 2.6 Data-driven HASEL control without physics models (SSM)
**arXiv:2601.03247** (2026-01-06) — *Nonlinear Spectral Modeling and
Control of Soft-Robotic Muscles from Data.*
https://arxiv.org/abs/2601.03247
Spectral-submanifold reduction learns an input→output map for HASEL
actuators from forced-response data alone and runs real-time control
of an antagonistic HASEL-clutch joint, with substantially lower
tracking error than feedback-only or feedforward-only baselines under
identical settings.
*So what:* hysteresis/memory — the standard objection to HASEL in
joints — is increasingly a solved control problem rather than a
materials veto. Pairs with 2.2 (same clutch-joint lineage).

### 2.7 HASEL micro parallel robot (scaling down, not up)
**arXiv:2604.25337** (2026-04-28) — *Design and Modeling of a HASEL
Actuator-Based Micro Parallel Robot.*
https://arxiv.org/abs/2604.25337
3-DOF 3PS parallel robot with three base-integrated HASELs;
port-Hamiltonian model + grey-box parameter ID for control.
*So what:* noted for completeness — HASEL integration work continues
at micro scale; nothing here speaks to body-scale force.

---

## 3. Twisted/coiled polymer (TCP) and textile muscles

### 3.1 Hierarchical TCP: force decoupled from stroke limits (modelling)
**arXiv:2602.06067** (2026-02-01) — *Mechanics of hierarchical twisted
and coiled polymer artificial muscles: Decoupling force from kinematic
limits.* *(model + analysis; not a device demonstration)*
https://arxiv.org/abs/2602.06067
A coupled thermo-mechanical model of hierarchically bundled TCP
predicts significantly amplified isometric stress vs monofilament
baselines while holding **~22% contraction stroke**, identifies an
optimal bundle complexity beyond which inter-filament friction jams
actuation, and finds volumetric energy density **scale-invariant** in
bundle radius — implying force can be scaled linearly by geometric
upsizing without efficiency loss, *if* the model holds in hardware.
*So what:* TCP's known ceiling was the force/stroke trade. This is the
first principled route around it we have seen, and its scale-invariance
claim is testable on a bench for very little money. It does **not**
fix TCP's ~1% efficiency / cooling-dominated cycle from the landscape
doc — thermal actuation stays slow. Watch, and replicate the model
against a physical bundle before believing the scaling claim.

### 3.2 Pneumatic TCP with inductance-based force self-sensing
**arXiv:2603.18555** (2026-03-19) — *Inductance-Based Force Self-Sensing
in Fiber-Reinforced Pneumatic Twisted-and-Coiled Actuators.*
https://arxiv.org/abs/2603.18555
A conductive nickel wire integrated into a fiber-reinforced pneumatic
twisted-and-coiled actuator gives a deterministic, **low-hysteresis
inductance–force relationship** (even though inductance–length is
strongly hysteretic); an EKF + constrained-optimisation observer
achieves force estimation **comparable to external load cells**.
*So what:* tendon/muscle force sensing is one of our open gaps (G4 in
the sensing survey). A sensing element that is literally a wire in
the muscle is braid-compatible in spirit — worth tracking for the
tendon-force problem.

### 3.3 TCP wrist with model-predictive control
**arXiv:2503.05508** (2025-03-07) — *Design, Dynamic Modeling and
Control of a 2-DOF Robotic Wrist Actuated by Twisted and Coiled
Actuators.*
https://arxiv.org/abs/2503.05508
Modular 2-DOF wrist (3RRRR parallel mechanism) driven by twisted and
coiled actuators, with a Lagrangian dynamic model and NMPC beating PID
in comparative tests; integrated into a multi-segment soft arm.
*So what:* TCP remains a wrist/fine-motion technology, but the
control maturity (full dynamic model + NMPC on hardware) is ahead of
where our landscape doc implicitly places it.

### 3.4 TCP mechanics reference (2024)
**arXiv:2404.00802** (2024-03-31) — *The mechanics and physics of
twisted and coiled polymer actuators.*
https://arxiv.org/abs/2404.00802
Microstructure + Kirchhoff-rod model predicting TCPA equilibrium
shape, stiffness in active/passive states, and contraction under load;
validated against torsional actuation experiments on nylon.
*So what:* the modelling baseline for anyone replicating 3.1.

---

## 4. McKibben / pneumatic / hydraulic

### 4.1 UMArm: valves inside the McKibben — the infrastructure objection weakens
**arXiv:2505.11476** (2025-05-16) — *UMArm: Untethered, Modular,
Portable, Soft Pneumatic Arm.*
https://arxiv.org/abs/2505.11476
Rigid–soft hybrid arm densely integrating **modified McKibben
actuators with valves and controllers inside the actuator itself** —
no individual pressure lines, no external regulators. Fully untethered
operation with directionally tunable compliance; demonstrated as a
wearable assistive arm and reconfigured as an inchworm robot. (The
abstract claims "high payload capacity" without a number — unverified
at abstract level.)
*So what:* our landscape doc's McKibben caveat is system-level:
compressors, valves, plumbing. Moving regulation *into* the muscle is
the same move as the DEA cartridge, applied to pneumatics — it does
not fix pneumatic system efficiency, but it undercuts the "bulky
external infrastructure" argument. Full text owed for the payload
number.

### 4.2 Antagonistic PAM dynamics, learned well enough to plan stiffness
**arXiv:2602.23670** (2026-02-27) — *Physics-Embedded Neural ODEs for
Learning Antagonistic Pneumatic Artificial Muscle Dynamics.*
https://arxiv.org/abs/2602.23670
Hybrid neural-ODE model of antagonistic PAM joints: median **R² =
0.89** over 196 held-out co-contraction conditions; inverse model
computes feedforward pressures for desired motion/stiffness/payload.
Identified stiffness landed **within 3% of commanded** across
136–176 N/mm; payload displacement under loads **up to 173 N**
predicted within 14%, with feedforward removing **93–95%** of it
(vs 81–82% for a static model).
*So what:* co-contraction stiffness control is the mechanism our body
plan assumes for PAM joints; this is quantitative evidence it can be
planned, not just tuned. The 173 N payload scale is arm-class, not
leg-class — noted, not oversold.

### 4.3 MUSBRIC: LEGO-compatible pneumatic muscle bricks
**arXiv:2610.40285** (2026-10-29) — *MUSBRIC: LEGO-Compatible
Pneumatic Muscle Bricks for Reconfigurable Musculoskeletal Robots.*
https://arxiv.org/abs/2610.40285
Fiber-reinforced extensile PAMs with LEGO-compatible endcaps become
plug-and-play muscle bricks with a matched MuJoCo simulator;
15 leg configurations swept in hardware + simulation, quadruped
walking demonstrated; designs/code to be released open source.
*So what:* a prototyping accelerator for exactly the Phase 1/2 bench
work in our roadmap — attachment-geometry sweeps for musculoskeletal
layouts without refabrication. Relevant to the body plan's "first
measurable experiment per subsystem" pattern.

### 4.4 Multi-mode PAMs from hybrid positive–negative pressure
**arXiv:2603.15066** (2026-03-16) — *Multi-Mode Pneumatic Artificial
Muscles Driven by Hybrid Positive-Negative Pressure.*
https://arxiv.org/abs/2603.15066
IN-FOAM actuators: heat-sealed sheet construction, programmable
skeleton patterns giving contraction, bending, twisting, rotation
from one architecture, with force/contraction tuned by mixing positive
pressure and vacuum; multilayer and multi-channel variants increase
contraction and combine modes.
*So what:* sheet/heat-seal fabrication is cheap and flat-pack —
interesting for skin-adjacent or disposable actuators, not for kN
joints. Adds a fabrication option to the muscle menu, at low force.

### 4.5 Water-hydraulic muscle control keeps maturing
**arXiv:2408.14223** (2024-08-26) — *Hierarchical-type Model Predictive
Control and Experimental Evaluation for a Water-Hydraulic Artificial
Muscle with Direct Data-Driven Adaptive Model Matching.*
https://arxiv.org/abs/2408.14223
Data-driven adaptive MPC for a water-hydraulic artificial muscle,
robust to poor initial data while respecting input constraints.
*So what:* hydraulic McKibben is our one kN-class soft muscle; its
control literature is industrial and steadily improving. No new force
numbers — the 7 kN figure in the landscape doc remains the reference.

---

## 5. Shape-memory alloy (SMA)

### 5.1 Consistent SMA force over long lifetimes — via swappable muscles + thermal supervision
**arXiv:2402.06201** (2024-02-09) — *Maximizing Consistent Force Output
for Shape Memory Alloy Artificial Muscles in Soft Robots.*
https://arxiv.org/abs/2402.06201
A fatigue-testing protocol plus supervisory control of the muscle's
internal temperature state holds SMA force consistent over long
lifetimes; demonstrated in a soft limb with **swap-able SMA muscles**,
maintaining high forces in a practical task over **hundreds of
cycles**.
*So what:* two ideas transfer directly. (1) The *swappable muscle*
is the DEA-cartridge pattern independently reinvented for SMA — more
evidence replaceability is where the field lands when lifetime is
finite. (2) Temperature-state supervision as the lifetime governor is
a control-layer pattern our cartridge QA could adopt wholesale.

### 5.2 SMA self-sensing: pose and contact from resistance + temperature
**arXiv:2409.17111** (2024-09-25) — *Self-Sensing for Proprioception
and Contact Detection in Soft Robots Using Shape Memory Alloy
Artificial Muscles.*
https://arxiv.org/abs/2409.17111
Polynomial regression on SMA electrical resistance + in-situ
temperature predicts limb pose with no dedicated sensors; adding one
true-pose measurement enables binary contact detection. Proof of
concept on a fully soft limb.
*So what:* completes the pattern across classes — DEA (capacitance),
HASEL (current/capacitance), TCP (inductance), SMA (resistance) all
now have published self-sensing routes. Our sensor-layer spec should
treat muscle self-sensing as a default input, not an extra.

---

## 6. Hybrid actuation & variable stiffness

### 6.1 One control framework across PAM, HASEL, and DEA antagonistic joints (simulation)
**arXiv:2511.09104** (2025-11-12) — *Decoupling Torque and Stiffness:
A Unified Modeling and Control Framework for Antagonistic Artificial
Muscles.* *(simulation study)*
https://arxiv.org/abs/2511.09104
A separable Padé force model + two-state dynamic wrapper and a
cascaded controller in co-contraction/bias coordinates gives
independent torque and stiffness tracking **across pneumatic,
electrohydraulic, and dielectric-elastomer muscle families**, running
<1 ms per control tick; depth-adaptive stiffness scheduling trades
shock load vs stability in contact.
*So what:* our recommended body is hybrid (motor+SEA large joints,
McKibben/HASEL mid-body, DEA surface). A single antagonistic control
abstraction spanning three of those families is precisely the glue
such a body needs. Simulation-only — hardware validation is the gap.

### 6.2 WAVE: worm-gear variable elasticity that unloads the motor at rest
**arXiv:2509.21878** (2025-09-26) — *WAVE: Worm Gear-based Adaptive
Variable Elasticity for Decoupling Actuators from External Forces.*
https://arxiv.org/abs/2509.21878
Non-backdrivable worm gear decouples motor from external forces;
impacts convert to spring energy; stiffness modulated continuously by
spring precompression. Experimentally, **motor load approaches zero
at rest even under external loading**.
*So what:* for the motor+SEA baseline that actually carries large
joints, holding posture for free is a direct runtime/thermal win —
compare the power-thermal budget's holding-torque heat problem.
Variable stiffness via precompression is also the mechanical analogue
of PAM co-contraction, in the class that scales to knees.

### 6.3 DSO-VSA: stiffness decoupled from output, dual-motor load sharing
**arXiv:2512.18712** (2025-12-21) — *DSO-VSA: a Variable Stiffness
Actuator with Decoupled Stiffness and Output Characteristics for
Rehabilitation Robotics.*
https://arxiv.org/abs/2512.18712
Variable-length lever + hypocycloidal mechanism gives a linear
torque–deflection relation and continuous stiffness from near-zero to
theoretically infinite, **decoupled from deflection angle**; planetary
differential lets two motors share load. Prototype validated on
stiffness calibration, torque control, and load sharing.
*So what:* dual-motor load sharing in a joint-sized package is a
practical route to kN-class tendon force without one oversized motor
— relevant to the knee-extensor backlog item's design space.

### 6.4 Patterned Structure Muscle: printed TPU muscles in arbitrary shapes
**arXiv:2410.07682** (2024-10-10) — *Patterned Structure Muscle:
Arbitrary Shaped Wire-driven Artificial Muscle Utilizing Anisotropic
Flexible Structure for Musculoskeletal Robots.*
https://arxiv.org/abs/2410.07682
FDM-printed TPU anisotropic structures + wire drive produce muscles
in curved, flat, multi-DOF, joint-covering, and branched shapes; an
upper arm built from them shows wide range of motion and lifting
through environmental contact. (Abstract gives no force numbers.)
*So what:* shape freedom is the gap between cylindrical commercial
muscles and anatomical muscle layouts. Printed-muscle geometry +
wire drive is a low-cost complement to braided sleeves for odd-shaped
spaces (hands, face, shoulders).

---

## 7. Updates & corrections to our existing docs

**No headline claim in either doc is overturned.** Specifically:

- *Landscape doc, §DEA verdict / deep dive §10:* largest DEA device
  force (66 N) and the "no device meets 300 kPa + 15% strain +
  10⁶ cycles" watch triple — **unchanged**; nothing found in
  2024–2026 arXiv contradicts them.
- *Landscape doc, McKibben verdict:* hydraulic McKibben as the sole
  kN-class soft muscle — **unchanged**; no new kN-class soft result
  found.
- *Landscape doc, HASEL lifetime:* **add a caveat, not a correction** —
  HASEL displacement decays under sustained DC drive (2401.13941);
  sustained-force applications need AC drive + series elasticity.
  Our strain/force table entries are peak figures and should be read
  that way.
- *Landscape doc, McKibben system caveat:* **soften one clause** —
  "bulky external regulators" is being engineered away (UMArm,
  2505.11476, valves/controllers inside the actuator). Pneumatic
  *efficiency* objections stand; the *packaging* objection is weaker
  than written.
- *Sensing survey gap G3 (muscle self-sensing under-specified):*
  **strengthened** — add F-HASEL's dedicated sensing electrode
  (20 Hz, 2404.04071), current-only HASEL grasp sensing (2603.24357),
  TCP inductance force sensing (2603.18555), and SMA resistance
  self-sensing (2409.17111) as published, per-class solutions.
- *Deep dive §9 (cartridge architecture):* **add prior art** — SMA's
  swap-able muscle limb (2402.06201) and DEA lifetime-scanning QA
  (2602.20963) are independent implementations of the same
  replace-and-characterise pattern.

## 8. Top 5 to read in full

1. **arXiv:2602.20963** — DEA lifetime scanning. The method (and any
   absolute lifetimes in the full text) feeds directly into cartridge
   QA design.
2. **arXiv:2603.24357** — Peano-HASEL hand. Closest published system
   to our forearm-actuator + tendon + self-sensing architecture;
   full text should yield per-actuator force numbers the abstract
   omits.
3. **arXiv:2505.11476** — UMArm. Need the payload and efficiency
   numbers behind "high payload capacity" before updating the
   McKibben system assessment.
4. **arXiv:2602.06067** — Hierarchical TCP mechanics. The
   scale-invariance claim, if it survives contact with hardware,
   reopens TCP for mid-body muscles; check the model's assumptions.
5. **arXiv:2511.09104** — Unified antagonistic control. The control
   layer for the hybrid body; check how the Padé model parameters map
   to real HASEL/DEA data.

## 9. Caveats

- All numbers above are **abstract-reported** unless stated otherwise;
  several key papers (UMArm payload, DEA lifetime absolutes, PSM
  force) omit the number that matters most from their abstracts —
  flagged inline, and the reason §8 exists.
- Two entries are explicitly modelling/simulation only (2602.06067,
  2511.09104); their claims are labelled as such where they appear.
- This sweep used arXiv API queries per class on 2026-11-28; it is a
  sweep, not an exhaustive systematic review. Journal-only work (e.g.
  much of the Bridgestone hydraulic-muscle lineage) does not appear
  here by construction.
