# Xynthetix — Research Queue & Log

**Started:** 2026-11-23, at Joe's direction: research daily, add to this
repo daily. One substantive, sourced addition per day — a doc, a spec
extension, a simulator improvement with tests, or a worked example.
No filler, no personal information, everything here stays open source.

**Scope (expanded 2026-11-23, Joe's correction):** the whole synthetic
body programme, not just braiding. Braiding is one workstream among
many. The destination is complete synthetic bodies; every workstream
below feeds that destination:

1. **Artificial muscles** — dielectric elastomer actuators (DEA),
   McKibben / pneumatic, twisted & coiled polymer (TCP), HASEL and
   other electrohydraulic actuators, shape-memory alloy/polymer,
   hydraulic & series-elastic actuation, tendon drive systems.
2. **The 3D body plan** — skeleton and joint design, body proportions
   and scaling across sizes, hands/feet, spine, head and face
   mechanisms, tails and non-human morphologies, structural materials,
   weight budgets, CAD / simulation tooling for body design.
3. **Braiding & woven tissue** — maypole braiders, the `.braid` spec
   and simulator, braided sleeves / tendons / actuators, materials.
4. **Skin & surface** — silicone and elastomer skins, fur and hair
   systems, surface temperature (warm-to-touch bodies), self-healing
   and repairable surfaces, dermal displays.
5. **Power & thermal** — batteries and energy density, runtime
   budgets, heating to body temperature, cooling under load,
   charging, power distribution in a soft body.
6. **Sensing & proprioception** — tactile sensing, joint position and
   force sensing, thermal sensing, sensor skins, readout electronics.
7. **Control & compute** — tendon/muscle control, ROS 2, embedded
   compute for bodies, learned control / foundation models for
   humanoid robots, simulation (MuJoCo, Isaac, etc.).
8. **Landscape & safety** — competitors and prior art (technical,
   public facts only), standards, safety testing, open-source
   projects to learn from or interoperate with. No financial or
   partnership planning in this public repo.

## How a daily run works

1. Check disk first: keep at least 55 GB free on the VM. Research is
   text/code only — no large downloads.
2. Take today's workstream from the rotation below and the top
   unchecked backlog item in that workstream (or note why it is
   blocked and take the next one).
3. Research from primary sources where possible (papers, vendor docs,
   upstream repos, standards). Cite every factual claim with a URL.
4. Add ONE substantive file/change under `docs/`, `braid/`,
   `examples/`, or `tests/`. Update this log.
5. If code changed, run `python -m pytest tests/ -q` (or the stdlib
   test runner) and record the result in the log entry.
6. Commit locally with a clear message. Push to
   `github.com/Kaleaon/Xynthetix` with the workspace's incremental
   Git Database API pusher; if a push cannot land, say so in the log
   entry — never claim a push that did not verify.

## Weekly rotation

- **Mon — Artificial muscles:** DEA first (the programme is
  DEA-forward), then the wider actuator landscape in turn.
- **Tue — 3D body plan:** skeleton, joints, proportions, morphology.
- **Wed — Braiding & woven tissue:** braider hardware, pipeline,
  braided actuators, yarns and fibres.
- **Thu — Skin, power & thermal:** surfaces, warmth, batteries,
  runtime, cooling — the body as a physical system.
- **Fri — Sensing & control:** tactile/proprioception, readout,
  tendon/muscle control, compute, learned control.
- **Sat — Landscape & safety:** competitors, prior art, standards,
  open-source projects (technical, public facts only).
- **Sun — Build & verify:** code, simulator, CAD/tooling notes,
  validation of earlier claims against new sources, queue grooming.
  Rotate the workstream Sunday serves, in the order above.

## Backlog

### Artificial muscles
- [ ] Artificial muscle landscape survey: DEA, McKibben, TCP,
      HASEL/electrohydraulic, SMA, hydraulic — force, strain, voltage/
      pressure, bandwidth, cycle life, cost, maturity, all sourced.
- [ ] DEA deep dive: stack/roll geometries, dielectric materials,
      drive voltages and electronics, failure modes, published force
      at human-muscle scale; what a replaceable DEA cartridge implies.
- [ ] Knee-extensor problem: what actuator classes can actually
      deliver large-joint torque at 100 kg body scale — sourced
      numbers, not vibes.
- [ ] TCP / coiled nylon: fabrication, strain/force data, thermal
      efficiency and cooling limits.
- [ ] HASEL actuators: published performance, drive electronics,
      self-sensing claims, replicability.
- [ ] Tendon drive: cable materials (UHMWPE etc.), routing friction,
      motor placement (proximal mass strategy), series elasticity.
- [ ] LT-PAM (HardwareX 2026) replication data sheet: pressures,
      contraction, force, materials, cost — sourced.

### 3D body plan
- [ ] Synthetic body plan map: subsystems, interfaces, and the open
      questions per subsystem — the research map for this whole queue.
- [ ] Skeleton materials comparison: printed polymers, carbon tube,
      aluminium, composites — stiffness/weight/cost/repairability.
- [ ] Joint design survey: bearing joints vs ligament/printed
      compliant joints (incl. the UTokyo Yoshimura TPU work), range
      of motion, backdrivability, wear.
- [ ] Scaling laws: how mass, torque, and power scale from ~1.4 m to
      ~2.7 m bodies; where designs break.
- [ ] Hands: tendon-driven hand prior art (open-source hands),
      DOF vs complexity, grasp data.
- [ ] Spine & torso: articulated spine designs, compliance, load
      paths with proximal motor mass.
- [ ] Head & face: expressive face mechanisms, eyes, jaw, ears —
      actuation options and published builds.
- [ ] Tails & extra morphologies: active tail actuation, balance
      role, structural attachment.

### Braiding & woven tissue
- [x] Survey of documented DIY / open maypole braiders: carrier
      counts, track/horn-gear designs, BOMs, what is actually replicable.
      → `docs/maypole-braider-prior-art.md` (2026-11-23).
- [ ] Braid angle geometry check: simulator predictions vs published
      maypole geometry relations, with worked numbers.
- [ ] Yarn shortlist for first sleeves: PET, nylon, UHMWPE, aramid —
      friction / abrasion / elasticity comparison from datasheets.
- [ ] Carrier schedule output: can the simulator emit a machine-ready
      carrier / take-up schedule? Design note first, code second.

### Skin, power & thermal
- [ ] Skin systems survey: silicone casting, 3D-printed elastomers,
      fur/hair attachment, thickness vs tactile transparency.
- [ ] Warm body budget: heating a human-scale surface to 35–37 °C —
      published power numbers, insulation strategies, control.
- [ ] Battery survey for bodies: cell energy density, safe placement
      in a soft body, hot-swap / split battery architectures, runtime
      estimates at realistic loads.
- [ ] Cooling actuators & electronics in an insulated soft body.

### Sensing & control
- [ ] Conductive yarn options for tactile sensing: resistance per
      metre, wash / flex behaviour, sourcing.
- [ ] Sensor layer: readout electronics options (voltage divider vs
      constant-current, multiplexing) costed from public listings.
- [ ] Proprioception options: encoders, stretch sensors, muscle
      self-sensing (DEA/HASEL capacitance), fusion approaches.
- [ ] Learned control for tendon-driven bodies: sim-to-real state of
      the art, MuJoCo/Isaac tooling, open datasets.

### Landscape & safety
- [ ] Allonic 3D Tissue Braiding: public technical claims inventory,
      dated and sourced, no speculation presented as fact.
- [ ] Open-source humanoid / body projects inventory: what exists,
      licences, what to interoperate with.
- [ ] Safety standards landscape for personal robots: ISO 13482 and
      neighbours, what they require, testing approaches.

## Log

- **2026-11-23 (Mon)** — Queue created; first run started:
  DIY / open maypole braider prior-art survey.
- **2026-11-23 (Mon)** — Added `docs/maypole-braider-prior-art.md`:
  survey of 5 documented DIY builds (Fraens 12-carrier, kmatch98,
  Caitlyn B OpenSCAD, Nico71 LEGO, one video-only build) plus
  industrial/academic design parameters (4-slot horn gears, 1F1E
  occupancy, tension data), replicability table, Phase 1 gap list,
  and a 3-architecture shortlist. 15 sources, all opened and cited.
  Headline finding: the only complete desktop design is paid /
  personal-use licensed; no openly licensed complete braider exists.
- **2026-11-23 (Mon, scope correction)** — Joe: the queue was too
  braider-narrow. Scope expanded to the full body programme —
  artificial muscles, the 3D body plan, skin/power/thermal, sensing
  & control, landscape — rotation and backlog rewritten. Artificial
  muscle landscape survey started the same day.
