# Open-Source Humanoid / Body Projects Inventory

**Status:** v1.0 — compiled 2026-11-28 (Saturday rotation: landscape & safety)
**Scope:** Open-source humanoid robots, hands, and the simulation/control/soft-body stacks a synthetic-body programme can actually reuse — plus the well-known closed platforms, labelled as closed so nobody mistakes them for open. Every licence below was read from the project's own `LICENSE` file or licence statement; every activity date is the repository's last push as returned by the GitHub API on 2026-11-28. Where a licence or a file could not be located, that is stated rather than guessed.

**How to read this:** The comparison table is the index. Each project then gets a short entry: what it is, licence, status, what transfers to Xynthetix, what does not. "Transfers" means usable under the stated licence at our scale and in a commercial company; a non-commercial (NC) licence or a copyleft licence is not a ban on learning from a project, but it is a ban on shipping its files in a product. Projects already inventoried elsewhere in this repo — braidpy (`docs/braidpy-evaluation.md`), LuxTac and Digit 360 (`docs/skin-systems-survey.md`) — are referenced, not redone.

## Comparison table

| Project | Licence | Status (last push, 2026-11-28) | What transfers to Xynthetix |
|---|---|---|---|
| Poppy Humanoid + Torso | Hardware CC BY-SA 4.0; software GPLv3 | Stale — Humanoid 2021-12-06, Torso 2022-03-24, pypot 2022-05-02 | 3D-printed humanoid CAD, URDF, Dynamixel control patterns |
| iCub | Software BSD-3-Clause; models CC BY-SA 4.0 | Active — icub-main 2026-11-25 | Full-humanoid URDF/SDF, whole-body control software, skin architecture precedent |
| Reachy 2 | Apache-2.0 | Active — SDK 2025-11-26, core 2026-04-07 | URDF, Gazebo models, ROS 2 controllers, bimanual mobile-manipulator layout |
| Reachy Mini | Apache-2.0 | Active — 2026-11-27 | Compact expressive head/neck SDK, conversation-app patterns |
| Berkeley Humanoid Lite | MIT | Active-ish — 2026-03-10 | Full open biped: CAD, URDF, low-level + RL control |
| Berkeley Humanoid (full-size) | Unverified — no licence file in description repo | Quiet — description 2024-08-23, Isaac assets 2024-10-12 | Isaac sim assets (licence unclear — verify before reuse) |
| ROBOTIS OP3 | Apache-2.0 | Quiet — 2025-02-26 | Small humanoid ROS stack, walking/gait code, Dynamixel patterns |
| Mini Cheetah | MIT | Quiet — 2023-10-18 | Legged locomotion control (MPC/WBIC) reference |
| ODRI Solo / Bolt | BSD-3-Clause | Quiet — Solo 2023-09-06, Bolt 2023-08-17 | Cheap torque-controlled quadruped/biped testbed design |
| K-Scale Stompy (+ kos, ksim, urdf2mjcf) | MIT | Active — kinfer 2026-10-17, urdf2mjcf 2025-09-26 | MuJoCo humanoid sim, robot firmware framework, URDF→MJCF converter |
| InMoov | Unverified — no licence file in repo; no licence text retrievable from project site | Slow — repo 2025-01-06; runtime MyRobotLab (Apache-2.0) active 2026-11-05 | Human-scale 3D-printable body shells; servo-driven hand/face precedent |
| LeRobot / SO-101 + SO-100 | Apache-2.0 | Very active — lerobot 2026-11-28, SO-ARM100 2026-11-20 | Cheap 3D-printed leader/follower arms; teleop + imitation-learning pipeline; the Phase 0 testbed |
| Yale OpenHand | Models CC BY-NC 3.0; ROS node MIT | Quiet — ROS node 2022-02-10 | Underactuated tendon-hand design patterns (research only — NC) |
| LEAP Hand | CC BY-NC 4.0 | Active-ish — API 2025-10-20, Sim 2024-05-18 | Dexterous 16-DOF hand CAD + Isaac Gym sim (research only — NC) |
| MuJoCo | Apache-2.0 | Very active — 2026-11-28 | Physics sim core for tendon/muscle bodies |
| Isaac Lab | Framework BSD-3-Clause; mimic ext. Apache-2.0; Isaac Sim proprietary | Very active — 2026-11-28 | GPU-parallel RL training; humanoid training workflows |
| ROS 2 control | Apache-2.0 | Very active — 2026-11-27 | Hardware-interface layer for real actuators |
| Drake | BSD-3-Clause | Very active — 2026-11-28 | Rigid-body dynamics, trajectory optimisation, manipulation planning |
| Pinocchio | BSD-2-Clause | Very active — 2026-11-26 | Fast rigid-body dynamics + derivatives for control |
| OpenSim | Apache-2.0 | Very active — 2026-11-27 | Musculoskeletal modelling (human muscle/tendon reference data) |
| Gazebo | Apache-2.0 | Very active — 2026-11-27 | Robot simulation with ROS 2 integration |
| Webots | Apache-2.0 | Very active — 2026-11-28 | Robot simulation, broad robot model library |
| SOFA | LGPL-2.1 | Very active — 2026-11-22 | Soft-tissue / deformable-body simulation |
| PyElastica | MIT | Active — 2026-11-13 | Cosserat-rod sim of slender soft structures (tendons, braids, tails) |
| Soft Robotics Toolkit (Harvard) | Unverified — design library, no single licence found; site not text-retrievable | Unknown | PneuNet / soft-actuator fabrication designs (verify per-design licence) |

## Humanoid bodies

**Poppy Humanoid + Poppy Torso (Inria / Flower Labs).** A 3D-printed humanoid (85 cm) and a torso variant built for research and teaching, driven by Dynamixel servos through the pypot Python library. Licence is split and stated in the project's own README table: hardware under CC BY-SA 4.0, software under GPLv3; the "Poppy" name itself is a protected trademark. Status is the inventory's clearest staleness signal: the Humanoid repo last pushed 2021-12-06, Torso 2022-03-24, pypot 2022-05-02. What transfers: the printed-body construction pattern, the URDF, and the Dynamixel control idioms — all share-alike or GPL, so usable in an open programme but not vendible as closed product. What does not transfer: the scale (a small teaching robot, not a load-bearing body), the servo architecture (position servos, not artificial muscle), and any use of the Poppy name.

**iCub (IIT / Robotology).** A 104 cm child-sized humanoid built as a cognitive-robotics platform, with whole-body control, tactile skin, and vision. The main software repository (`robotology/icub-main`) carries a BSD-3-Clause licence file, and it is actively maintained — last push 2026-11-25. The official URDF/SDF models (`robotology/icub-models`) are CC BY-SA 4.0, last pushed 2026-02-26. What transfers: a complete, permissively licensed full-humanoid software stack and a share-alike model set — the best reference in this inventory for how a whole humanoid's software is organised, and the iCub skin work is the direct precedent for the sensor-layer architecture already in `docs/sensor-layer-spec.md`. What does not transfer: the hardware itself is a research platform built with custom machined parts and torque sensors at a price and complexity far above a first build, and the child proportions do not scale to adult or Titan bodies.

**Reachy 2 (Pollen Robotics).** A bimanual mobile manipulator Pollen describes on its own site as "the first open-source humanoid robot designed for embodied AI." The Python SDK (`pollen-robotics/reachy2-sdk`, Apache-2.0, last push 2025-11-26) and the core workspace (`pollen-robotics/reachy2_core`, Apache-2.0, last push 2026-04-07) are public; the core repo's listing shows `reachy_description` (URDF), `reachy_gazebo`, `reachy_controllers`, and `reachy_bringup` directories. What transfers: the URDF, the Gazebo setup, and the ROS 2 controller layout — a working template for describing a two-armed body in simulation and on hardware, under the most permissive terms in this inventory. What does not transfer: Reachy 2 is a torso on a mobile base with Orbita actuators, not a walking biped, and no full CAD release was located in the public org listing — the openness claim rests on the software stack and description, so treat the hardware files as unverified until located.

**Reachy Mini (Pollen Robotics).** A small expressive desktop robot (head, neck, antennas) aimed at embodied-AI interaction. Its SDK (`pollen-robotics/reachy_mini`) is Apache-2.0 and actively developed — last push 2026-11-27, 1,693 stars — with docs, examples, tests, and a conversation app in the same organisation. What transfers: the compact expressive-head pattern, the SDK structure, and the conversation-app approach, all permissively licensed. What does not transfer: it is a head, not a body — no locomotion, manipulation, or load-bearing content.

**Berkeley Humanoid Lite (UC Berkeley, Hybrid Robotics Lab).** A small open biped built explicitly as a research platform, with code, CAD-derived assets, and a low-level controller in separate repos, all MIT-licensed. The main codebase (`HybridRobotics/berkeley-humanoid-lite`) last pushed 2026-03-10 and carries 2,083 stars. What transfers: the closest thing in this inventory to a complete open biped — morphology, actuation layout, and RL-based locomotion control under MIT terms. What does not transfer: it is a small, light research biped; its joint torques and structural margins do not read across to a 100 kg body, and the MIT licence still requires the copyright notice to travel with reuse.

**Berkeley Humanoid (full-size).** The lab's larger humanoid has Isaac simulation assets (`HybridRobotics/isaac_berkeley_humanoid`, last push 2024-10-12) and a description repo (`HybridRobotics/berkeley_humanoid_description`, last push 2024-08-23) — but the description repo has no licence file at all, and the Isaac repo's licence field is unasserted. What transfers: nothing yet, safely — the assets are visible but their terms are not stated. This is a verify-before-touch item, not a resource.

**ROBOTIS OP3 (ROBOTIS).** A small (51 cm) open humanoid platform with ROS packages (`ROBOTIS-GIT/ROBOTIS-OP3`, Apache-2.0, last push 2025-02-26), plus demo, tools, and message repos in the same organisation. What transfers: a compact, permissively licensed ROS humanoid stack — walking, balance, and Dynamixel control at a scale cheap enough to build and break. What does not transfer: the scale and the servo architecture, same limitation as Poppy.

**Mini Cheetah (MIT Biomimetic Robotics Lab).** The quadruped whose MIT-licensed control software (`mit-biomimetics/Cheetah-Software`) is public, last pushed 2023-10-18. It is a quadruped, not a humanoid, and it earns its place here because its model-predictive locomotion control is the reference implementation most open humanoid projects descend from. What transfers: the locomotion control approach and the proprioceptive-actuator idiom (high-torque-density motors with low gearing, torque sensed from current). What does not transfer: four legs, no hands, no torso, and a three-year-old snapshot — treat it as a textbook, not a dependency.

**ODRI Solo / Bolt (Open Dynamic Robot Initiative, MPI / NYU / LAAS lineage).** Open quadruped (Solo) and biped (Bolt) testbeds built around cheap brushless motors and 3D-printed parts. Both driver repos are BSD-3-Clause; Solo last pushed 2023-09-06, Bolt 2023-08-17. What transfers: the cheapest credible torque-controlled legged testbed design in the open world — a natural stepping stone between the SO-101 arm and a full biped. What does not transfer: small scale, no upper body, and a quiet project — expect to maintain any fork ourselves.

**K-Scale Stompy (K-Scale Labs).** A humanoid programme whose code is public and MIT-licensed across many repos: the master repo (`kscalelabs/kscale`, MIT, 2025-09-04), the firmware framework (`kscalelabs/kos`, MIT, 2025-05-26), the MuJoCo sim (`kscalelabs/ksim-legacy`, MIT, 2025-01-02), a URDF-to-MJCF converter (`kscalelabs/urdf2mjcf`, MIT, 2025-09-26), and the inference tool `kinfer` (pushed 2026-10-17). What transfers: the sim stack, the firmware framework, and the URDF→MJCF converter are immediately reusable, permissively licensed, and actively developed. What does not transfer: the hardware question is open — K-Scale sells Stompy as a product, and its own site was unreachable from this VM (connection failed, 2026-11-28), so whether the CAD is open is unverified. Do not assume the robot is open because its code is.

**InMoov (Gaël Langevin; runtime by MyRobotLab).** A human-scale, 3D-printable humanoid built from printed parts and hobby servos — the largest open body shell in this inventory by a wide margin, and the only one sized like a person. Its licence could not be verified: the `MyRobotLab/InMoov` repo has no licence file, and neither the project homepage nor its STL page yielded licence text to a text fetch on 2026-11-28. The runtime it depends on, MyRobotLab, is Apache-2.0 and active (last push 2026-11-05); the InMoov repo itself last pushed 2025-01-06. What transfers: the printed-shell construction approach and the servo-driven hand/face precedent — if the licence is confirmed. What does not transfer until then: the files themselves, in a commercial programme. Licence verification is a named gap below.

**MIT DRC stack (openhumanoids/oh-distro).** The integrated humanoid control, planning, and perception system built by MIT and Edinburgh for the DARPA Robotics Challenge. Its licence file states BSD-3-Clause. Last push 2018-03-06. What transfers: the whole-body control and planning architecture as a design reference. What does not transfer: it is eight years stale, built on a ROS 1 / Drake-era stack, and nobody maintains it — read it, do not depend on it.

**NimbRo-OP2X (University of Bonn, NimbRo).** An adult-size open humanoid soccer platform; the 2017 hardware release repo (`NimbRo/nimbro-op2`) last pushed 2018-09-26 and carries no licence field. Included to record that it exists and is stale; nothing here is verified reusable.

## Testbed arms

**LeRobot, SO-101, and SO-100 (Hugging Face / TheRobotStudio).** LeRobot (`huggingface/lerobot`) is the end-to-end learning-for-robotics framework — Apache-2.0, 29,133 stars, pushed the same day this inventory was compiled (2026-11-28). The SO-101 is the current low-cost leader/follower arm pair: the official docs page points builders at the SO-ARM100 repository for the bill of materials and the 3D-print instructions, and notes the follower arm uses six STS3215 bus servos. That hardware repo (`TheRobotStudio/SO-ARM100`) is Apache-2.0, pushed 2026-11-20, with 8,246 stars. What transfers: everything — this is the Phase 0 testbed already named in `docs/company-roadmap.md`: cheap printed arms, a teleoperation pipeline, and an imitation-learning stack, all permissively licensed and under furious active development. What does not transfer: the arms are small (a few hundred grams of payload class), servo-driven, and tendon-free — they teach teleop, data collection, and learned control, not artificial muscle. That is the right job for them.

## Hands

**Yale OpenHand (Yale GRAB Lab).** Underactuated, tendon-driven hands designed to be printed and built cheaply, with a long publication record behind them. The project page carries a Creative Commons Attribution-NonCommercial 3.0 licence badge for the models — non-commercial — while the ROS control package (`grablab/openhand_node`) is MIT-licensed but quiet (last push 2022-02-10). What transfers: the underactuated tendon-hand design pattern, which is directly relevant to a tendon-driven body programme — as a studied reference. What does not transfer into a product: the models themselves, under the NC terms.

**LEAP Hand (CMU / Stanford lineage, Shaw & Pathak).** A 16-DOF dexterous hand with a 3D-printable design, an Isaac Gym simulation repo, and a control API. Its licence file is Creative Commons Attribution-NonCommercial 4.0 — non-commercial, read from the file itself. The API repo last pushed 2025-10-20; the sim repo 2024-05-18. What transfers: the dexterous-hand kinematics, the grasp data, and the sim setup — as research references. What does not transfer into a product: the CAD and code, under the NC terms. This is the recurring pattern in open hands: the best dexterous designs are NC, and the permissive ones are simpler.

**DASH hand — not verified.** A soft dexterous anthropomorphic hand appears in the literature, but a GitHub repository search for it returned no matching public repo on 2026-11-28. It is omitted rather than described from memory. If a public release is located later, it belongs in the next revision of this inventory.

## Simulation and control

**MuJoCo (Google DeepMind).** The general-purpose physics simulator, Apache-2.0, very active (last push 2026-11-28, 18,555 stars). It is the default simulator for tendon-driven and muscle-driven bodies in the literature, and it is the engine under K-Scale's sim and much of LeRobot's evaluation. What transfers: the whole simulation core — adopt it as the programme's primary simulator. What does not transfer: MuJoCo is rigid-body with soft-contact approximations; it does not simulate braided sleeves, deformable skin, or DEA stacks. That is what SOFA and PyElastica are for (below).

**Isaac Lab (NVIDIA).** The GPU-parallel robot-learning framework — the framework itself is BSD-3-Clause and the `isaaclab_mimic` extension is Apache-2.0, per the project's own README; it is very active (last push 2026-11-28, 8,743 stars). The README also states plainly that workflows using Isaac Sim include components under proprietary licensing terms, and Isaac Sim itself is proprietary NVIDIA software. What transfers: the RL training framework and its humanoid workflows, under permissive terms. What does not transfer: Isaac Sim's renderer and proprietary components — the programme can train in Isaac Lab but must not treat Isaac Sim as an open dependency, and any pipeline built on it needs a proprietary-software exit plan.

**ROS 2 control (ros-controls).** The generic hardware-interface framework for ROS 2, Apache-2.0, active (last push 2026-11-27). What transfers: the controller-manager / hardware-interface pattern — this is how a real actuator (DEA driver, tendon motor, braided sleeve) should present itself to the rest of the stack. Adopt it as the hardware-abstraction layer.

**Drake (MIT / Toyota Research Institute lineage).** Model-based design, trajectory optimisation, and manipulation planning, BSD-3-Clause (read from its licence file), very active (last push 2026-11-28). What transfers: whole-body trajectory optimisation and the rigid-body dynamics tooling behind it — the planning layer above Pinocchio. What does not transfer: Drake is a large, heavyweight dependency with a steep learning curve; adopt it for planning studies, not as a runtime requirement for the first body.

**Pinocchio (Stack of Tasks / LAAS-CNRS).** Fast rigid-body dynamics algorithms and their analytical derivatives, BSD-2-Clause, very active (last push 2026-11-26, 3,891 stars). What transfers: the dynamics core for model-based control — small, fast, permissively licensed, and the natural companion to ROS 2 control. Adopt it alongside MuJoCo.

**OpenSim (Stanford / SimTK).** Musculoskeletal modelling — muscles, tendons, and joints simulated as a biomechanical system — Apache-2.0, active (last push 2026-11-27). What transfers: the reference data and modelling conventions for how biological muscle and tendon actually behave, which is the ground truth any artificial-muscle body is measured against. What does not transfer: OpenSim models biology, not robots; its muscle models are not actuator controllers.

**Gazebo (Open Source Robotics Foundation).** The classic robot simulator, Apache-2.0, active (last push 2026-11-27), with deep ROS 2 integration. What transfers: simulation with ROS 2, URDF/SDF models, and the Reachy 2 Gazebo setup as a worked example. What does not transfer: Gazebo's physics is rigid-body; for learned locomotion at scale, Isaac Lab or MuJoCo are the current defaults.

**Webots (Cyberbotics).** A general robot simulator, Apache-2.0, very active (last push 2026-11-28, 4,783 stars), with a broad library of robot models. What transfers: a fast, permissive simulator for early controller prototyping. What does not transfer: same rigid-body limitation as Gazebo, and a smaller humanoid community than MuJoCo's.

## Soft-body and braided simulation

**SOFA (INRIA and partners).** A real-time multi-physics simulation framework with an emphasis on deformable and medical simulation, LGPL-2.1, very active (last push 2026-11-22, 1,309 stars). What transfers: the only mature open framework for simulating soft tissue, deformable skin, and compliant structures — the natural home for a braided-sleeve or soft-skin simulation. What does not transfer freely: LGPL-2.1 is file-level copyleft with dynamic-linking obligations; use it as a linked library with the licence terms honoured, and keep it out of any closed firmware image.

**PyElastica (Gazzola Lab, EPFL lineage).** A Python implementation of Elastica — simulation of assemblies of slender, one-dimensional structures (rods) — MIT-licensed, active (last push 2026-11-13, 368 stars). What transfers: Cosserat-rod simulation of tendons, braided sleeves treated as rod assemblies, tails, and flexible spines — the most directly relevant soft-body tool in this inventory for the braiding workstream, under the most permissive terms. Adopt it for the tendon/braid simulation studies.

**Soft Robotics Toolkit (Harvard).** A web-hosted library of open soft-robot designs (PneuNets, soft grippers, fabrication guides) at softroboticstoolkit.com. Its licence could not be verified: the site returned only a 373-byte stub to a text fetch on 2026-11-28, and no GitHub organisation exists under that name. What transfers: the fabrication designs, once a per-design licence is confirmed. What does not transfer until then: any of it, into a product.

**somogym (GrauleM).** A toolkit for developing and evaluating controllers and RL for soft robots (64 stars, last push 2022-09-01). No licence file exists in the repo, so its terms are unverified. Noted here for completeness; not recommended as a dependency.

## Already covered elsewhere in this repo (reference only)

- **braidpy** — MPL-2.0, evaluated in `docs/braidpy-evaluation.md`; the braiding workstream's modelling library.
- **LuxTac** — flexible optical taxel skin, CC BY-NC-SA 4.0; **Digit 360** — Meta FAIR tactile finger sensor, CC BY-NC 4.0 — both inventoried in `docs/skin-systems-survey.md`. Both are non-commercial: usable as research references, not shippable in a product.

## Closed platforms — explicitly not open

**Unitree (H1, G1, Go2, and the rest).** The robots are proprietary products. What *is* open, and worth using, is the surrounding software: the SDK (`unitreerobotics/unitree_sdk2`, BSD-3-Clause, last push 2026-11-19), the simulation models (`unitreerobotics/unitree_model`, BSD-3-Clause, last push 2026-06-01 — URDFs for the humanoids, usable in MuJoCo and Isaac Lab), and an older CAD release (`unitreerobotics/unitree_cad`, MPL-2.0, last push 2022-07-16, stale). The distinction matters: Xynthetix can simulate against Unitree's open models and learn from its open SDKs, but it cannot build, modify, or sell a Unitree robot, and it should not design its programme around hardware it does not control.

**IHMC Nadia.** IHMC's humanoid is a research platform described on its own site (ihmc.us/nadia); no public source repository or open hardware release was located. Papers, not code. Treat as closed.

**Tesla Optimus, Figure, 1X, Boston Dynamics Atlas.** No open-source hardware or software release for any of these platforms was located in the searches run for this inventory (GitHub organisation and repository searches, 2026-11-28). They are treated here as closed. This is a negative search result, not a licence statement — if any of them publishes an open release, this section needs revising, and the revision should cite the release itself.

## Gaps

1. **No open DEA-driven humanoid exists.** Every open humanoid in this inventory is servo-driven (Poppy, Reachy, OP3, Berkeley Lite, Stompy) or torque-motor-driven (Mini Cheetah, ODRI). The DEA-forward programme has no open reference body to learn from — the muscle work in `docs/dea-deep-dive.md` stands alone.
2. **No open braided-muscle body exists.** Braiding appears in this inventory only as a simulation tool (PyElastica) and a library (braidpy). No public project braids actuators into a body.
3. **No open large-scale humanoid exists.** The largest open bodies are human-scale (InMoov, iCub at child scale); nothing open approaches the 2+ m Titan scale in `docs/body-plan-research-map.md`. Scaling laws there are our own work.
4. **Open hands are split by licence.** The dexterous hands (LEAP, Yale OpenHand) are non-commercial; the permissively licensed hands are simpler. A commercial programme needs its own hand design or a licence negotiation — it cannot just take LEAP.
5. **Licences unverified:** InMoov (no licence file, no retrievable site statement), Berkeley Humanoid full-size (no licence file), Soft Robotics Toolkit (per-design terms unconfirmed), somogym (no licence file), DASH hand (no public repo located), K-Scale Stompy hardware (site unreachable from this VM).
6. **No open safety-standard implementation.** Nothing in this inventory implements ISO 13482 or neighbouring personal-robot safety testing in code — that backlog item (`docs/research-queue.md`) is still open.

## Interoperability recommendations for Xynthetix

1. **Simulation core: MuJoCo + Pinocchio.** Both permissive (Apache-2.0, BSD-2), both very active, and both already the defaults in the projects this inventory's humanoids descend from. Use MuJoCo for physics and Pinocchio for model-based control maths.
2. **Hardware layer: ROS 2 control.** Apache-2.0, active, and the standard way a real actuator presents itself to ROS 2. Every actuator driver we write — DEA, tendon motor, braided sleeve — should expose a ROS 2 control hardware interface.
3. **Learning and training: Isaac Lab for RL, LeRobot for imitation.** Isaac Lab (BSD-3 framework) for GPU-parallel locomotion training; LeRobot (Apache-2.0) for teleop data and imitation on the physical testbed.
4. **Physical testbed: SO-101 arms now, ODRI legs next.** The SO-101 pair is the cheapest permissively licensed teleop rig available and is already the Phase 0 plan. When legs are needed, ODRI's Solo/Bolt is the cheapest torque-controlled legged design — BSD-3, printable, and proven.
5. **Humanoid reference: iCub's software organisation, Berkeley Lite's morphology.** Read iCub-main for how a whole humanoid stack is structured; read Berkeley Humanoid Lite for the smallest complete open biped. Take the organisation, not the scale.
6. **Soft-body simulation: PyElastica first, SOFA second.** PyElastica (MIT) for tendon/braid/tail rod simulation; SOFA (LGPL-2.1) when deformable skin or tissue-level simulation is needed, with the LGPL linking terms honoured.
7. **Humanoid description: copy Reachy 2's layout.** `reachy2_core` shows the clean pattern — `reachy_description` (URDF), `reachy_gazebo`, `reachy_controllers`, `reachy_bringup` — and it is Apache-2.0. Mirror that directory layout for our own body description when it exists.
8. **Do not build the product on NC-licensed parts.** LEAP Hand, Yale OpenHand models, LuxTac, and Digit 360 are research references only. Any hand, skin, or sensor that ships in a product must be our own design or permissively licensed.
9. **Do not depend on Unitree hardware or Isaac Sim.** Use Unitree's open models for simulation benchmarking and Isaac Lab for training, but keep both behind interfaces we own — the hardware is proprietary and the simulator is proprietary.
10. **Close the licence gaps before reusing the unverified five.** InMoov, Berkeley full-size assets, Soft Robotics Toolkit designs, somogym, and Stompy hardware each need a licence confirmation (or a decision to reimplement) before any file enters this repo.

## Sources

All sources were opened and read on 2026-11-28. Licence statements come from each repository's `LICENSE` file (via the GitHub licence API or the raw file) or from the project site as noted; activity dates are the `pushed_at` values returned by the GitHub API on the same date.

- https://github.com/poppy-project/poppy-humanoid (README licence table: hardware CC BY-SA 4.0, software GPLv3; trademark note)
- https://github.com/poppy-project/poppy-torso
- https://github.com/poppy-project/pypot (GPL-3.0)
- https://github.com/robotology/icub-main (BSD-3-Clause licence file)
- https://github.com/robotology/icub-models (CC BY-SA 4.0)
- https://github.com/pollen-robotics/reachy2-sdk (Apache-2.0)
- https://github.com/pollen-robotics/reachy2_core (Apache-2.0; repo listing shows reachy_description, reachy_gazebo, reachy_controllers)
- https://www.pollen-robotics.com/reachy-2/ ("Reachy 2: open-source humanoid robot for embodied AI")
- https://github.com/pollen-robotics/reachy_mini (Apache-2.0)
- https://github.com/HybridRobotics/berkeley-humanoid-lite (MIT)
- https://github.com/HybridRobotics/berkeley_humanoid_description (no licence file)
- https://github.com/HybridRobotics/isaac_berkeley_humanoid (licence unasserted)
- https://github.com/ROBOTIS-GIT/ROBOTIS-OP3 (Apache-2.0)
- https://github.com/mit-biomimetics/Cheetah-Software (MIT)
- https://github.com/open-dynamic-robot-initiative/solo (BSD-3-Clause)
- https://github.com/open-dynamic-robot-initiative/bolt (BSD-3-Clause)
- https://github.com/NimbRo/nimbro-op2 (no licence field)
- https://github.com/openhumanoids/oh-distro (BSD-3-Clause licence file)
- https://github.com/kscalelabs/kscale (MIT)
- https://github.com/kscalelabs/kos (MIT)
- https://github.com/kscalelabs/ksim-legacy (MIT)
- https://github.com/kscalelabs/urdf2mjcf (MIT)
- https://github.com/MyRobotLab/InMoov (no licence file)
- https://github.com/MyRobotLab/myrobotlab (Apache-2.0)
- https://inmoov.fr/ (homepage and STL page fetched; no licence text retrievable, 2026-11-28)
- https://github.com/huggingface/lerobot (Apache-2.0)
- https://huggingface.co/docs/lerobot/so101 (SO-101 docs; points to SO-ARM100 for BOM and print instructions; follower uses 6× STS3215)
- https://github.com/TheRobotStudio/SO-ARM100 (Apache-2.0)
- https://www.eng.yale.edu/grablab/openhand/ (CC BY-NC 3.0 licence badge)
- https://github.com/grablab/openhand_node (MIT)
- https://github.com/leap-hand/LEAP_Hand_API (CC BY-NC 4.0 licence file)
- https://github.com/leap-hand/LEAP_Hand_Sim
- https://github.com/google-deepmind/mujoco (Apache-2.0)
- https://github.com/isaac-sim/IsaacLab (README licence section: framework BSD-3, mimic Apache-2.0, Isaac Sim proprietary)
- https://github.com/ros-controls/ros2_control (Apache-2.0)
- https://github.com/RobotLocomotion/drake (BSD-3-Clause licence file)
- https://github.com/stack-of-tasks/pinocchio (BSD-2-Clause)
- https://github.com/opensim-org/opensim-core (Apache-2.0)
- https://github.com/gazebosim/gz-sim (Apache-2.0)
- https://github.com/cyberbotics/webots (Apache-2.0)
- https://github.com/sofa-framework/sofa (LGPL-2.1)
- https://github.com/GazzolaLab/PyElastica (MIT)
- https://softroboticstoolkit.com/ (site returned a 373-byte stub to a text fetch, 2026-11-28; licence unverified)
- https://github.com/GrauleM/somogym (no licence file)
- https://github.com/unitreerobotics/unitree_sdk2 (BSD-3-Clause)
- https://github.com/unitreerobotics/unitree_model (BSD-3-Clause)
- https://github.com/unitreerobotics/unitree_cad (MPL-2.0)
- https://ihmc.us/nadia/ (IHMC Nadia project page; no public source release located)
- Repo-internal references: `docs/braidpy-evaluation.md`, `docs/skin-systems-survey.md` (LuxTac CC BY-NC-SA 4.0; Digit 360 CC BY-NC 4.0), `docs/company-roadmap.md` (SO-101 testbed), `docs/body-plan-research-map.md`, `docs/dea-deep-dive.md`, `docs/sensor-layer-spec.md`, `docs/research-queue.md`

**Verification notes (honest gaps):** browser search was unusable in this session (E2BIG on every call), so all verification is GitHub API + curl page fetches. K-Scale's own site (k-scale.dev) was unreachable from this VM (connection failed). The DASH hand was searched on GitHub (repository search, two queries) with no matching public repo found and is therefore omitted. Tesla Optimus, Figure, 1X, and Boston Dynamics Atlas are listed as closed on a negative GitHub search, not on a per-company licence statement — if any publishes an open release, that section needs a cited revision. InMoov's licence remains unverified after two separate fetches of inmoov.fr; the commonly repeated CC BY-NC-SA attribution for its files was not confirmed from a primary source this run and is not asserted here.
