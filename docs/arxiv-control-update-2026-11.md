# arXiv Control & Compute Update — November 2026

**Date:** 2026-11-28. **Scope:** control and compute for synthetic /
humanoid bodies, swept from arXiv with priority on 2024–2026 work.
Every paper below was opened at abstract level (arXiv API) on
2026-11-28; arXiv IDs and dates are as listed there. This doc feeds
the Compute & control subsystem of `docs/body-plan-research-map.md`
(§2.9) and the queue's open backlog item "Learned control for
tendon-driven bodies: sim-to-real state of the art, MuJoCo/Isaac
tooling, open datasets."

**Headline:** 2026 is the year tendon/muscle sim-to-real stopped being
aspirational for small systems — two independent pipelines (GenAN,
tendon-force modelling) transferred learned policies onto real
tendon-driven hardware with quantified gaps. The humanoid foundation
model layer, meanwhile, consolidated around behaviour foundation
models (BFMs) that adapt to a body's dynamics *in context*, and the
MuJoCo ecosystem acquired exactly the cable-transmission fidelity
tooling our tendon bodies need.

---

## 1. Whole-body control & humanoid foundation models

### GR00T N1 — the anchor (already in the body plan map)
- **arXiv:2503.14734** (2025-03-18) — https://arxiv.org/abs/2503.14734
- Open VLA foundation model, dual-system: vision-language module
  interprets scene/instructions, diffusion transformer generates
  motor actions in real time; trained on real-robot trajectories,
  human video, and synthetic data; deployed on a Fourier GR-1.
- *So what:* still the reference open model. Everything below is
  either built on its lineage or on the BFM alternative to it.

### One-Step Drifting Action Heads for GR00T N1.7
- **arXiv:2609.18108** (2026-09-16) — https://arxiv.org/abs/2609.18108
- Replaces N1.7's iterative diffusion action head with a one-step
  drifting head: action-head forward time 45.3 ms → 5.0 ms,
  backbone+head 70.0 ms → 30.6 ms — but LIBERO success drops
  systematically (e.g. 64% Spatial, 26% Long across seeds). Reported
  honestly as a speed–success trade-off, not an improvement.
- *So what:* quantifies the price of cutting inference latency in the
  action head. For our compute budget, the lesson is to measure
  success-rate cost per millisecond saved before adopting any
  one-step/distilled head on-body.

### DiffGR00T — execution-aware training on the GR00T lineage
- **arXiv:2611.32665** (2026-11-24) — https://arxiv.org/abs/2611.32665
- Couples GR00T N1.7 to SONIC, a pretrained whole-body BFM, and makes
  training differentiable end-to-end by replacing the simulator with
  a learned action-conditioned world model, so body-execution losses
  backpropagate through the frozen controller into the VLA head.
  +12.5 percentage points average success over the supervised base
  VLA (59.2% → 71.7%) on four HumanoidArena tasks.
- *So what:* the hierarchical split (VLA generates, WBC executes)
  normally leaves balance/tracking errors invisible to the
  generator. Execution-aware training is the current fix — relevant
  when our high-level layer must learn what a soft, tendon-driven
  body can actually track.

### ECHO — in-context dynamics adaptation for BFMs
- **arXiv:2611.25778** (2026-11-19) — https://arxiv.org/abs/2611.25778
- A behaviour foundation model that learns structured dynamics
  representations from interaction history and applies residual
  corrections to a frozen behaviour prior — adaptation to new
  physical conditions *without test-time parameter updates*.
  Deployed on a Unitree G1: whole-body teleoperation, acrobatics,
  terrain interaction, payload adaptation.
- *So what:* arguably the most body-programme-relevant idea in this
  section. A braided body's dynamics drift as sleeves wear, creep,
  and get replaced; a controller that infers dynamics from recent
  interaction history instead of assuming a fixed model is the right
  shape for that.

### Ada-BFM — adapting BFMs to scene interaction
- **arXiv:2611.31863** (2026-11-24) — https://arxiv.org/abs/2611.31863
- Post-training framework: a lightweight adapter on a pretrained BFM
  yields one shared model per interaction domain (terrain, objects),
  accelerating learning vs training from scratch while largely
  preserving pretrained whole-body competence. Sim + real-world
  experiments.
- *So what:* the adapter pattern — freeze the general controller,
  train small per-domain adapters — maps well onto per-body and
  per-morphology adaptation for bodies no dataset contains (the body
  plan map's open question in §2.9).

### S-BFM — control from sparse spatiotemporal goals
- **arXiv:2611.27552** (2026-11-20) — https://arxiv.org/abs/2611.27552
- BFM that generates whole-body transitions from target posture,
  position, heading, and arrival time alone — no dense reference
  trajectory. Cuts global joint-position error >32% vs the best
  baseline, raises fixed-goal reach 43.5% → 74.6%, terminal position
  error 1.67 m → 0.26 m; deployed on the full-size AGIBOT A3.
- *So what:* sparse-goal interfaces lower the authoring burden for
  new behaviours — useful for expressive/social motion (arrive here,
  in this posture, by then) without motion-capture pipelines.

### MoViC — whole-body control from monocular video
- **arXiv:2611.19998** (2026-11-15) — https://arxiv.org/abs/2611.19998
- Live RGB video as the control signal: monocular reconstruction +
  retargeting + a transformer BFM; an extrapolation method bridges
  10 Hz visual estimation with the 50 Hz controller. Hardware demos:
  dynamic motion tracking and device-free teleoperation.
- *So what:* a cheap teleoperation/data-collection route — one
  camera, no mocap suit — for teaching a body new motions.

### PredActor — steerable onboard control, proprioception only
- **arXiv:2609.24840** (2026-09-21) — https://arxiv.org/abs/2609.24840
- Joint state-action diffusion policy executed directly (no
  reference tracker, no privileged state), steerable at test time
  via classifier guidance on predicted future states. Complete
  callback: 16.79 ms median / 19.38 ms p95 on a Jetson Orin NX —
  inside a 20 ms control period. Deployed on a Unitree G1.
- *So what:* a concrete onboard latency datapoint for a learned
  whole-body policy on embedded hardware, and a design that needs
  only proprioception — the sensing our bodies will actually have.

### REA — asynchronous brain–cerebellum runtime
- **arXiv:2610.42053** (2026-10-30) — https://arxiv.org/abs/2610.42053
- Runtime architecture pairing a deliberative foundation model
  (System 2) with fast policies (Systems 1/0) under one rule: *no
  running policy waits on the brain*. Route memory, a
  boundary-triggered judge gate, and a bounded escalation ladder.
  95.9% success on 60 LIBERO-Pro tasks; transfers to a real Unitree
  G1.
- *So what:* answers the body plan map's "which layers classical,
  which learned" question at the systems level: the runtime, not
  the model, enforces the rate separation. Worth stealing as an
  architectural pattern regardless of model choice.

---

## 2. Sim-to-real for tendon-driven & musculoskeletal robots

### GenAN — Generalized Actuator Networks (the standout)
- **arXiv:2604.09487** (2026-04-10) — https://arxiv.org/abs/2604.09487
- Learns a neural model of tendon + pneumatic-muscle actuation
  (nonlinearity, friction, hysteresis) from joint position
  trajectories alone — no torque sensors — and pairs it with
  rigid-body simulation. On PAMY2, a tendon-driven PAM arm:
  goal-reaching, ball-in-a-cup, and table-tennis policies trained
  entirely in simulation deployed successfully — claimed first
  sim-to-real transfer for a 4-DOF muscle-actuated robot arm.
- *So what:* this is the template for our actuator layer. Our bench
  protocol (Phase 2 dataset) already collects the trajectories a
  GenAN-style model eats; the actuation model, not the policy, is
  where the sim-to-real gap lives.

### Tendon Force Modeling for Sim2Real Transfer
- **arXiv:2603.04351** (2026-03-04) — https://arxiv.org/abs/2603.04351
- Transformer model of servo-driven tendon forces, trained on a
  dedicated test-bench capturing forces under contact-rich
  interaction: predicts tendon force within 3% of maximum motor
  force, robot-agnostic. Integrated into GPU-accelerated
  force-driven simulation it cuts the sim-to-real gap on test
  trajectories by 41%, and RL controllers trained with it improve
  real fingertip pose tracking by 50% on tendon-driven fingers.
- *So what:* directly validates — and upgrades — the body plan
  map's first control experiment (§2.9: sim-vs-bench tension on one
  tendon-driven finger). Their test-bench design is the one to
  copy: capture forces *during contact*, not free-space only.

### Muscle-Aware Retargeting & Null-Space Exploration
- **arXiv:2611.10682** (2026-11-07) — https://arxiv.org/abs/2611.10682
- Whole-body musculoskeletal control from human mocap despite a
  ~700-dimensional redundant muscle action space: bounded
  muscle-aware retargeting of reference trajectories, then
  anatomically structured null-space exploration for the policy.
  Solves all 24 benchmark clips, half the samples of the baseline,
  joint-center error −44%.
- *So what:* redundancy is our problem too (antagonistic muscles,
  more actuators than joints). Null-space exploration — using
  redundancy for secondary objectives instead of fighting it — is
  the current best-shaped answer.

### MyoAcross — morphology-conditioned musculoskeletal policies
- **arXiv:2610.36535** (2026-10-27) — https://arxiv.org/abs/2610.36535
- Builds individualized musculoskeletal models from accessible
  inputs (body shape, monocular images, mocap) and trains a
  generalist policy conditioned on morphology: 99.24% completion
  across 31 held-out individual models vs 8.32% for a
  generic-model baseline; better agreement with measured ground
  reaction forces and EMG.
- *So what:* the body programme spans many morphologies and sizes.
  A morphology-conditioned policy that transfers across bodies
  without fine-tuning is the musculoskeletal field's version of the
  same answer — and evidence that conditioning on the body
  description beats retraining per body.

### Beyond Kinematics — simulation fidelity for muscle-driven learning
- **arXiv:2609.21909** (2026-09-18) — https://arxiv.org/abs/2609.21909
- Systematic comparison of SCONE/HyFyDy vs MuJoCo/MyoSim imitation
  pipelines against mocap + EMG: both reproduce kinematics, but
  HyFyDy's muscle activations align far better with measured EMG
  (pooled RMSE 0.164, r = 0.4) than MuJoCo's (0.344, r = 0.11).
  Neither yet brings physiological realism to GPU-parallel sim.
- *So what:* a warning label for our simulator choice: if the
  research question involves muscle activation patterns or
  metabolic cost, MuJoCo-class pipelines currently answer the
  wrong thing well. Kinematics-only questions are fine.

### MuJoCable — cable transmission fidelity inside MuJoCo
- **arXiv:2609.09612** (2026-09-09) — https://arxiv.org/abs/2609.09612
- MuJoCo plugin adding reduced-order, surface-routed cable
  transmission: routing over moving analytic/mesh surfaces,
  unilateral tension, directional Capstan friction propagation.
  Pulley benchmarks recover analytical transmission relations with
  Capstan-ratio error <0.5%; on an 18-joint tendon robot it reveals
  friction-driven load growth that MuJoCo's native tendon does not
  represent; hardware-validated on two tendon systems.
- *So what:* our braid conduit *is* a surface-routed cable with
  Capstan friction. This is the missing physics between "tendon as
  ideal constraint" and the hysteresis loops the tendons backlog
  (§2.4) wants published. See "adopt now" below.

### Do Rigid-Body Simulators Dream of Soft Robots?
- **arXiv:2606.22397** (2026-06-21) — https://arxiv.org/abs/2606.22397
- Continuum-mechanics-informed discretization that places a
  tendon-driven continuum robot natively inside MuJoCo, unifying
  tendon forces, contact, and dynamics; validated against a
  Cosserat-rod reference and hardware; imitation policies trained
  in sim deployed zero-shot to a physical 3-segment continuum
  robot on contact-rich tasks — claimed first such transfer for
  continuum robots.
- *So what:* evidence that MuJoCo can host soft/tendon bodies if
  the discretization is derived from continuum mechanics rather
  than approximated ad hoc — a route for tails, spines, and other
  continuum morphologies in the body plan.

---

## 3. Control of soft, pneumatic & DEA actuators

### DEA Modeling, Control and Self-sensing — Review
- **arXiv:2604.17199** (2026-04-19) — https://arxiv.org/abs/2604.17199
- Review of physics-based and phenomenological DEA models;
  control classified as open-loop feedforward, feedback,
  feedforward+feedback, and adaptive feedforward; physics-based
  and data-driven self-sensing (displacement reconstruction with
  no extra sensors); open problems summarised. The nonlinearity
  stack it organises: nonlinear elasticity, viscoelastic creep,
  hysteresis, vibrational dynamics.
- *So what:* the control companion to `docs/dea-deep-dive.md`.
  Adaptive feedforward + capacitive self-sensing is the recurring
  practical recipe; it also reinforces the sensing survey's gap
  finding that our sensor layer spec under-uses DEA self-sensing.

### Decoupling Torque and Stiffness in Antagonistic Artificial Muscles
- **arXiv:2511.09104** (2025-11-12) — https://arxiv.org/abs/2511.09104
- A unified real-time framework spanning pneumatic, electrohydraulic
  (HASEL), and DEA muscle families: separable Padé force model +
  two-state dynamic wrapper, cascaded inverse-dynamics control in
  co-contraction/bias coordinates, depth-adaptive stiffness
  scheduling. Controller runs <1 ms per tick; independent torque
  and stiffness tracking demonstrated through stiffness steps and
  contact transients (in simulation across soft-to-rigid
  environments).
- *So what:* one control framework for all three muscle families
  we care about, in the antagonistic-pair configuration our bodies
  use. The co-contraction/bias coordinate split is directly
  implementable on the Phase 2 bench.

### Physics-Embedded Neural ODEs for Antagonistic PAM Dynamics
- **arXiv:2602.23670** (2026-02-27) — https://arxiv.org/abs/2602.23670
- Hybrid model: parametric joint/pneumatic mechanics + a neural
  force term for antagonistic coupling and rate-dependent
  hysteresis. Trained on 29 co-contraction conditions, predicts
  196 held-out conditions at median R² = 0.89; its inverse gives
  feedforward pressure commands that remove 93–95% of payload
  displacement (vs 81–82% for a static model); identified stiffness
  within 3% of commanded.
- *So what:* the PAM counterpart to GenAN's lesson — embed the
  physics, learn only the residual (coupling + hysteresis). For
  braided McKibben sleeves, whose geometry we control, a
  physics-embedded model per braid angle is a concrete,
  bench-sized project.

### Portable High-Voltage Control Circuits for Untethered DEA Robots
- **arXiv:2502.06166** (2025-02-10) — https://arxiv.org/abs/2502.06166
- Control board switching up to 1.8 kV at 0–1 kHz using series
  low-voltage resistive components; 2.5 g per channel; with a
  commercial miniature HV converter it drives a 42 g untethered
  DEA crawling robot at 15 Hz with live onboard video.
- *So what:* the drive-electronics end of DEA control is getting
  small and cheap at miniature scale. Scaling channel count and
  voltage to body-scale DEA arrays remains open — but the
  per-channel mass figure (2.5 g) is the number to design against.

---

## 4. Simulation tooling (MuJoCo / Isaac / soft-body)

### MuJoCo Playground
- **arXiv:2502.08844** (2025-02-12) — https://arxiv.org/abs/2502.08844
- Open framework on MJX: pip-installable, trains policies in
  minutes on a single GPU, covers quadrupeds, humanoids, dexterous
  hands, arms; zero-shot sim-to-real from state and pixels.
- *So what:* the fastest on-ramp to the MuJoCo training stack the
  Nov 28 inventory already recommended as our simulation core.

### LocoMuJoCo
- **arXiv:2611.26293** (2026-11-19) — https://arxiv.org/abs/2611.26293
- Open (MIT) imitation/RL benchmark for whole-body control:
  MuJoCo CPU + MJX + MjWarp GPU backends under one API; 9 humanoid,
  3 (musculo-)skeletal, and 4 quadruped embodiments; curated mocap
  per humanoid plus AMASS/LAFAN1 retargeting; a companion repo for
  sim-to-real deployment.
- *So what:* the musculoskeletal embodiments make this the closest
  off-the-shelf benchmark to our bodies, and its retargeting
  pipeline addresses the "one body description for design, sim,
  and control" question from §2.9.

### SORS — Soft Over Rigid Simulator
- **arXiv:2512.15994** (2025-12-17) — https://arxiv.org/abs/2512.15994
- FEM-based, energy-formulated simulator for soft robots with
  modular material/actuation models and optimization-based contact;
  validated on cantilever deflection, a pressure-actuated soft arm,
  contact datasets, and control optimization of a soft leg.
- *So what:* the high-fidelity complement to MuJoCo: use rigid-body
  speed for policy training, FEM fidelity for checking soft-tissue
  behaviour the rigid model cannot represent.

### RAFL — Residual Acceleration Field Learning
- **arXiv:2603.22039** (2026-03-23) — https://arxiv.org/abs/2603.22039
- Learns an element-level corrective dynamics field on top of a
  base differentiable simulator from sparse marker observations;
  topology-agnostic, so it generalises across morphologies where
  global system identification shows negative transfer; supports
  continual refinement during morphology optimization.
- *So what:* when the body itself is a design variable — our whole
  programme — fitted global parameters absorb geometry effects and
  lie. A local residual field is the more honest correction, and
  it accumulates accuracy as hardware data arrives.

*Isaac note:* no Isaac Lab framework paper surfaced in this sweep's
arXiv results; Isaac remains the GPU-parallel locomotion-training
alternative to MJX, but the tendon/cable fidelity work above is all
landing on the MuJoCo side, which strengthens the inventory's
MuJoCo-first recommendation for tendon bodies specifically.

---

## 5. Onboard compute & inference

### TRIAGE — VLA inference on embedded boards
- **arXiv:2610.34519** (2026-10-25) — https://arxiv.org/abs/2610.34519
- Training-free VLA acceleration: per-token choice between KV-cache
  reuse and pruning, decided by a measured drift threshold. Within
  3 percentage points of full-recomputation success while cutting
  prefill latency up to 48% on a Jetson AGX Orin.
- *So what:* System-2 inference on-body is a latency budget problem
  before it is a model problem; token-level reuse/pruning is free
  performance on hardware we can actually buy.

### Where Is VLA Inference Time Spent?
- **arXiv:2611.06710** (2026-11-04) — https://arxiv.org/abs/2611.06710
- Measurement study of seven optimization families across seven
  VLAs and four GPU families, from H100 down to embedded Jetson
  Thor: CPU launch overhead, memory bandwidth, and kernel
  efficiency interact, and stacking optimizations changes each
  one's benefit. Derives stacking guidelines under latency budgets.
- *So what:* read before speccing body compute. It is the difference
  between "Thor-class board" as a guess and as a sized decision —
  and it ties directly into the power/thermal budget, since every
  inference watt is a watt the thermal system must reject.

### Online Hamilton-Jacobi Reachability in the Control Loop
- **arXiv:2611.04096** (2026-11-03) — https://arxiv.org/abs/2611.04096
- CUDA HJ-reachability solver fast enough to run *inside* the
  control loop, producing certified backward reachable tubes as a
  deterministic safety layer under black-box learned policies:
  112 Hz for a 3D benchmark on a workstation GPU; on an embedded
  Jetson AGX Thor, 66 Hz (3D) / 54 Hz (2D), 3.8–8.9× faster than
  the JAX reference on the same device.
- *So what:* a concrete, running answer to the body plan map's
  safety-layer question: learned layers propose, a reachability
  layer with formal guarantees disposes — at embedded rates, on
  embedded hardware, today. State-dimension limits (2D–4D solves)
  mean it guards reduced safety models, not the full body state.

---

## Top 5 to read in full

1. **GenAN (arXiv:2604.09487)** — the sim-to-real template for
   muscle actuation; closest published work to our Phase 2 bench.
2. **Tendon Force Modeling (arXiv:2603.04351)** — test-bench design
   and force-model numbers (3% error, −41% gap) to benchmark our
   own finger experiment against.
3. **MuJoCable (arXiv:2609.09612)** — the cable/friction physics our
   simulator stack is missing; implementation-level detail matters.
4. **ECHO (arXiv:2611.25778)** — in-context dynamics adaptation is
   the control idea most shaped like a wearing, changing body.
5. **DEA modeling/control/self-sensing review (arXiv:2604.17199)** —
   the map for the DEA control backlog; read before designing any
   DEA drive or sensing electronics.

## Most actionable adoption, now

**Put MuJoCo + a MuJoCable-style surface-routed cable model at the
centre of the Phase 1 finger-over-core simulation** — i.e. do the
body plan map's §2.9 first experiment with the conduit modelled as a
routed cable with Capstan friction and unilateral tension, not as
MuJoCo's native ideal tendon. It costs no hardware, it uses the
stack already recommended by the open-source inventory, and it
produces the sim-vs-bench tension discrepancy number that sizes the
sim-to-real problem for every tendon in the body. When bench data
exists, layer a GenAN-style learned actuator model on top — the
2026 literature says that is where the transfer is won.

---

*Method note: swept via the arXiv API on 2026-11-28 (browser search
was unavailable this session). 27 papers cited; every ID, date, and
quantitative claim above comes from the paper's arXiv abstract as
returned that day. Abstract-level claims — especially "first"
claims — are the authors', and are flagged as such where they
appear.*
