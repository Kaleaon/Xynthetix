# arXiv Materials Update — November 2026

**Scope:** Materials-science papers from arXiv (2024–2026 prioritised;
older only where load-bearing) relevant to synthetic bodies, swept
2026-11-28. Every entry was opened at abstract level via the arXiv API;
numbers are the papers' own, from their abstracts. Each entry ends with
what it changes for Xynthetix, tied to the existing doc it touches.
Sibling sweeps cover actuators, design, sensing, and control.

## 1. Dielectric elastomers

### Automated DEA manufacturing — robotic spin-coat + CNT electrode stamping
- **arXiv:2608.00369** — *A Robotic System for Automated Manufacturing
  of Dielectric Elastomer Actuators* (2026-08-01).
  https://arxiv.org/abs/2608.00369
- Demonstrated: a robotic line fabricating 20 multilayer DEAs, each
  12 dielectric layers at 55.37 ± 2.04 µm mean thickness with 11
  alternating CNT electrodes applied by stamping; total process time
  cut 14.2%, operator removed from 56.1% of the process.
- **So what:** manufacturing repeatability is the quiet blocker behind
  the cartridge concept in `dea-deep-dive.md` — layer-thickness spread
  of ±2 µm at 55 µm is the kind of tolerance data a cartridge QA spec
  needs, and stamping CNT electrodes is a scalable alternative to the
  printed electrodes the deep dive favours.

### Self-driving lab for DEA lifetime — parameter scan doubles lifetime
- **arXiv:2602.20963** — *A Robotic Testing Platform for Pipelined
  Discovery of Resilient Soft Actuators* (2026-02-24).
  https://arxiv.org/abs/2602.20963
- Demonstrated: a multi-channel testing robot scanning Elastosil-based
  linear DEA lifetime across voltage, frequency, electrode material
  concentration, and connection filler; optimal combinations improved
  operational lifetime under boundary conditions by up to 100%. The
  scaled-up actuators ran a modular quadruped carrying >100% of its
  body weight (>700% of combined actuator weight).
- **So what:** direct support for the lifetime programme in
  `dea-deep-dive.md` §7 — lifetime is a *searchable* parameter surface,
  not a fixed material property, and the search can be automated on a
  bench Xynthetix could replicate cheaply.

### Low-voltage thin DEA — 220 V via 8 µm prestretched films
- **arXiv:2512.17940** — *Untethered thin dielectric elastomer actuated
  soft robot* (2025-12-12). https://arxiv.org/abs/2512.17940
- Demonstrated: thin DEA layers spin-coated at 50 µm then biaxially
  stretched to 8 µm, actuating at **220 V** at 86 Hz resonance;
  a 38 mm, 2.34 g fully untethered robot with onboard electronics,
  12.36 mm/s bare-actuator locomotion speed.
- **So what:** updates `dea-deep-dive.md`, which frames DEA drive as
  1–6 kV. Sub-kV DEA is real — but only at 8 µm film thickness and
  gram scale. The voltage problem is a thickness/manufacturing
  problem, which points the cartridge programme at thin-film process
  capability rather than new chemistry alone.

### Miniature HV control — 1.8 kV, 0–1 kHz, 2.5 g per channel
- **arXiv:2502.06166** — *Portable, High-Frequency, and High-Voltage
  Control Circuits for Untethered Miniature Robots Driven by
  Dielectric Elastomer Actuators* (2025-02-10).
  https://arxiv.org/abs/2502.06166
- Demonstrated: a control board using low-voltage resistive components
  in series to switch up to 1.8 kV at 0–1 kHz; 2.5 g per channel;
  drove a 42 g untethered crawling robot (cylindrical DEA, 15 Hz)
  with live onboard video.
- **So what:** the HV-electronics mass penalty assumed in
  `dea-deep-dive.md` and `power-thermal-budget.md` is shrinking —
  gram-scale per-channel HV switching exists, so distributed DEA
  drive in a body is an integration problem, not a mass blocker.

### UV-crosslinked silicone DEA — −55 °C, near-vacuum operation
- **arXiv:2603.04352** — *A Soft Robotic Demonstration in the
  Stratosphere* (2026-03-04). https://arxiv.org/abs/2603.04352
- Demonstrated: a Pt-catalysed UV crosslinking mechanism for silicone
  elastomers forming C–C bonds, with DEA performance characterised at
  −40 °C and 120 °C and near vacuum against acrylic and silicone
  state of the art; autonomous DEA grippers flown on two stratospheric
  balloon missions to 23.6 km, <0.05 atm, −55 °C.
- **So what:** widens the environmental envelope data behind
  `dea-deep-dive.md`'s materials table, and UV-cure processing is
  directly relevant to printing/casting skin and muscle layers in
  `skin-systems-survey.md`.

### ML discovery of soft high-k elastomers under data scarcity
- **arXiv:2601.18032** — *Multimodal Machine Learning for Soft High-k
  Elastomers under Data Scarcity* (2026-01-25).
  https://arxiv.org/abs/2601.18032
- Demonstrated: a curated dataset of acrylate dielectric elastomers
  from a decade of experiments, plus a multimodal ML framework using
  pretrained polymer embeddings for few-shot prediction of dielectric
  constant and Young's modulus together (dataset and code public).
- **So what:** the high-k/low-modulus trade-off is the core materials
  bottleneck named in `artificial-muscle-landscape.md`; this is a
  usable, open starting dataset for screening DEA dielectric
  candidates before any lab work.

## 2. Self-healing elastomers & tough soft materials

### Ultra-stretchable self-healable vitrimers — 80× stretch, 40 MJ/m³
- **arXiv:2503.03701** — *Ultra-stretchable and Self-Healable Vitrimers
  with Tuneable Damping and Mechanical Response* (2025-03-05).
  https://arxiv.org/abs/2503.03701
- Demonstrated: poly(methyl acrylate) vitrimers with dioxaborolane
  metathesis crosslinks — stretchability to ~80× original length,
  toughness ~40 MJ/m³, thermal stability to ~250 °C, loss factor
  tan δ 2–3 peak (>0.3 across 0.001–100 Hz), reprocessable by thermal
  and chemical routes, and room-temperature self-healing at low
  crosslink density. Properties tune via crosslinker amount and cure.
- **So what:** quantifies the dioxaborolane vitrimer chemistry that
  `skin-systems-survey.md` §5 mentions without numbers. 40 MJ/m³
  toughness with RT healing is the strongest skin-candidate data point
  in this sweep — but damping that high (tan δ >0.3 across five
  decades) means it is a *lossy* material: good for impact-tolerant
  skin, wrong for elastic energy return in muscle.

### Foldable bottlebrush networks — stiffness/extensibility decoupled
- **arXiv:2404.09330** — *A universal strategy for decoupling stiffness
  and extensibility of polymer networks* (2024-04-14).
  https://arxiv.org/abs/2404.09330
- Demonstrated: single-network elastomers from foldable bottlebrush
  strands holding Young's modulus near-constant at ~30 kPa while
  breaking strain rises 40-fold, 20% → 800%; shown across polymer
  species and topologies.
- **So what:** attacks the stiffness–extensibility trade-off that
  `artificial-muscle-landscape.md` treats as given for elastomers.
  A 30 kPa, 800%-strain network is skin/soft-tissue territory, and
  bottlebrush architecture is the same lever pulled for ultra-soft
  DEA dielectrics — relevant to both `skin-systems-survey.md` and
  `dea-deep-dive.md`.

### Dynamic-bond elastomers — network theory of damage & healing
- **arXiv:2401.11087** — *Network evolution controlling strain-induced
  damage and self-healing of elastomers with dynamic bonds*
  (2024-01-20). https://arxiv.org/abs/2401.11087
- Demonstrated (simulation): coarse-grained MD linking macroscopic
  hysteresis, stress relaxation, and self-healing of dynamic polymer
  networks to shortest-path structure in the network, with empirical
  rules for predicting behaviour under varied loading histories.
- **So what:** gives `skin-systems-survey.md`'s self-healing section a
  predictive frame instead of a catalogue — healing performance is a
  network-topology property, so candidate chemistries can be screened
  in simulation before synthesis.

### Hydroelastomers — swelling composites that don't soften
- **arXiv:2203.17131** — *Hydroelastomers: soft, tough, highly swelling
  composites* (2022-03-31, load-bearing).
  https://arxiv.org/abs/2203.17131
- Demonstrated: hydrogel particles embedded in a tough water-permeable
  elastomer matrix swell strongly with little softening, with fracture
  properties matching the best tough hydrogels; made from commercial
  materials, mouldable/extrudable, and the dispersed phase can be any
  hydrogel including stimuli-responsive ones.
- **So what:** a tissue-analogue route the body-plan work has not yet
  catalogued — swelling compartments inside a tough skin is close to
  how real soft tissue is organised, and relevant to the tissue
  discussion in `body-plan-research-map.md`.

### Microtubular graphene PNIPAM — 400% faster, ~4000% stronger actuation
- **arXiv:2303.13878** — *Overcoming water diffusion limitations in
  hydrogels via microtubular graphene networks for soft actuators*
  (2023-03-24). https://arxiv.org/abs/2303.13878
- Demonstrated: a bioinspired microtube graphene network at only 5.4%
  porosity in PNIPAM raises actuation dynamics by up to ~400% and
  actuation stress by ~4000% without losing mechanical stability;
  supports untethered light-controlled and electrically powered
  actuation.
- **So what:** hydrogel actuation's speed limit is transport, not
  chemistry — the same lesson as braided fluid channels. Relevant to
  `artificial-muscle-landscape.md`'s treatment of hydrogel muscles
  as inherently slow: with engineered transport paths, they are less
  slow than the survey implies (still not prime movers).

## 3. Conductive elastomers & liquid-metal composites

### Ag-shell liquid metal — printable, >75 dB EMI shielding at 200% strain
- **arXiv:2501.17808** — *Replacing the Gallium Oxide Shell with
  Conductive Ag: Toward a Printable and Recyclable Composite for
  Highly Stretchable Electronics, Electromagnetic Shielding, and
  Thermal Interfaces* (2025-01-29). https://arxiv.org/abs/2501.17808
- Demonstrated: galvanic replacement swaps the insulating Ga₂O₃/GaOOH
  shell on LM droplets for conductive Ag; the Ag-coated particles in
  SIS form a digitally printable composite with EMI shielding >75 dB
  (X-band) maintained at 200% strain, usable as a thermal interface
  material, and recyclable in a biodegradable solvent.
- **So what:** the oxide shell is the known weakness of LM conductors
  in `sensing-proprioception-survey.md`; this is a direct fix with a
  printing process attached — candidate material for braided-body
  wiring and sensor electrodes in `conductive-yarn-tactile-sensing.md`.

### Aligned Ni + LM thermal composite — 7.5 W/m·K, ultrasoft, insulating laterally
- **arXiv:2611.33381** — *Magnetically Guided Sequential Multi-Filler
  Alignment Enables Anisotropic Heat Pathways in Stretchable
  Composites for Soft Electronics* (2026-11-24).
  https://arxiv.org/abs/2611.33381
- Demonstrated: magnetically aligned Ni microparticle scaffold
  infiltrated with an LM/Ni mixture gives through-plane thermal
  conductivity of 7.5 W/(m·K) at ~160 kPa modulus, with lateral
  electrical conductivity below 10⁻¹² S/m.
- **So what:** the strongest thermal-interface number in this sweep
  for `power-thermal-budget.md` — 7.5 W/m·K in a material softer than
  most skin candidates changes the skin-as-radiator arithmetic, and
  the anisotropy (conduct heat out, insulate sideways) is exactly
  what a warm body wants between muscle and skin.

### LM textile coil — full-body wireless charging garment, 100+ wash/stretch cycles
- **arXiv:2412.01134** — *Friction jointing of distributed rigid
  capacitors to stretchable liquid metal coil for full-body wireless
  charging clothing* (2024-12-02). https://arxiv.org/abs/2412.01134
- Demonstrated: friction-capsule jointing of rigid capacitors into an
  LM-filled textile tube coil — 3.1× stretch tolerance (31.8 N) and
  3.5× bending tolerance (25.9 N) vs adhesive jointing; garment
  prototype survived >100 stretch/wash cycles.
- **So what:** two transfers — a proven jointing method for putting
  rigid electronics into soft textile runs (the exact problem in
  `braided-mesh-integration.md`), and evidence that full-body textile
  power distribution survives washing, relevant to
  `power-thermal-budget.md`'s power architecture.

### DissolvPCB — recyclable EGaIn circuit boards
- **arXiv:2507.22193** — *DissolvPCB: Fully Recyclable 3D-Printed
  Electronics with Liquid Metal Conductors and PVA Substrates*
  (2025-07-29). https://arxiv.org/abs/2507.22193
- Demonstrated: FDM-printed PVA substrates with EGaIn conductors;
  immersion in water dissolves the substrate, recovers the LM as a
  bead and the components for reuse; three functional prototypes
  built and recycled, with an LCA against milled FR-4.
- **So what:** repairability is a stated Xynthetix principle
  (`company-roadmap.md`); a body whose electronics are designed for
  disassembly-by-dissolution is a concrete pattern for the replaceable
  module philosophy in `dea-deep-dive.md`.

## 4. Fibres & yarns

### Double-drawn CNT fibres — 3.30 N/tex tenacity, 354 W/m·K
- **arXiv:2204.04468** — *Simultaneously Enhanced Tenacity, Rupture
  Work, and Thermal Conductivity of Carbon Nanotubes Fibers by
  Increasing the Effective Tube Contribution* (2022-04-09,
  load-bearing). https://arxiv.org/abs/2204.04468
- Demonstrated: a double-drawing process on continuously grown CNT
  fibres reaching specific strength ~3.30 N/tex, work of rupture
  ~70 J/g, and thermal conductivity ~354 W/m·K from low-crystallinity
  commercial starting material — reported as more versatile than
  comparable carbon fibre, Zylon, Dyneema, and Kevlar.
- **So what:** `yarn-shortlist-first-sleeves.md` contains no CNT fibre
  entry at all. On the paper's numbers a CNT yarn is simultaneously a
  top-tier tendon fibre and a heat pipe — a candidate for the tendon
  shortlist and for thermal paths in `power-thermal-budget.md`. Cost
  and braidability at maypole scale remain the open questions.

### CNT fibre structure–property ML — what actually drives strength
- **arXiv:2502.07400** — *Explainable Multimodal Machine Learning for
  Revealing Structure-Property Relationships in Carbon Nanotube
  Fibers* (2025-02-11). https://arxiv.org/abs/2502.07400
- Demonstrated: explainable multimodal ML over CNT fibre fabrication
  data showing small, uniformly distributed aggregates drive fracture
  strength, while long effective CNT length drives electrical
  conductivity, with identified thresholds for optimisation.
- **So what:** if CNT yarn enters the programme (above), this is the
  screening method for incoming material — pairs with the
  data-driven approach of arXiv:2601.18032 for dielectrics.

### TCP actuator mechanics — a predictive model for coiled nylon
- **arXiv:2404.00802** — *The mechanics and physics of twisted and
  coiled polymer actuators* (2024-03-31).
  https://arxiv.org/abs/2404.00802
- Demonstrated: a microstructure + Kirchhoff-rod model that predicts
  TCP equilibrium shape, passive/active longitudinal stiffness, and
  stimulated contraction under load, validated against torsional
  actuation experiments on twisted/annealed nylon.
- **So what:** TCP is rated qualitatively in
  `artificial-muscle-landscape.md`; this gives the design equations
  to size a coiled-nylon trim actuator instead of guessing, and the
  stored-energy framing transfers to braided-sleeve mechanics.

### Textile pneumatic pouches — fabrication parameters, measured
- **arXiv:2411.00295** — *Sealing the Deal: Effects of Fabrication
  Parameters on the Performance of Textile Pneumatic Haptic
  Actuators* (2024-11-01). https://arxiv.org/abs/2411.00295
- Demonstrated: heat-press temperature/time/pressure optima for
  TPU-coated nylon pouches; textile actuators 96.4% thinner and 57.2%
  lighter than elastomeric equivalents at 95.3% of their blocked force
  (36.1 N max), with more stable cyclic behaviour.
- **So what:** fabrication data for the woven/braided actuator path in
  `braided-mesh-integration.md` — sealed-textile construction is an
  alternative to braided sleeves for low-profile pneumatic muscles,
  and the heat-sealing parameters are directly reusable.

### Spider silk cyclic recovery — a design target for synthetic fibres
- **arXiv:2602.00147** — *Plasticity, hysteresis, and recovery
  mechanisms in spider silk fibers* (2026-01-29).
  https://arxiv.org/abs/2602.00147
- Demonstrated: a microscopically motivated two-network model of
  dragline silk under cyclic loading — bond dissociation at yield,
  entropic chain deformation, and recovery that *increases* stiffness
  in subsequent cycles — validated against Argiope bruennichi data.
- **So what:** tendons in a body are cyclically loaded for years; this
  is the reference behaviour (hysteresis with recovery and
  self-stiffening, not progressive damage) that synthetic tendon
  fibres in `yarn-shortlist-first-sleeves.md` should be benchmarked
  against.

## 5. Thermal materials

### Hybrid liquid + composite-PCM cooling for battery pouches
- **arXiv:2601.18959** — *3D-Printed Hybrid Liquid-CPCM Cooling
  Modules for High-Performance Thermal Management of Lithium-Ion
  Pouch Cells* (2026-01-26). https://arxiv.org/abs/2601.18959
- Demonstrated: a 3D-printed carbon-fibre-nylon module combining
  serpentine liquid cooling with hexagonally partitioned,
  nanocarbon-enhanced composite phase-change material — sealed CPCM
  encapsulation (no leakage path), short conduction paths for fast
  latent-heat uptake, liquid loop preventing CPCM saturation.
- **So what:** `power-thermal-budget.md` contains no phase-change
  buffering at all. A body battery is a pouch-cell pack worn against
  soft tissue; CPCM buffering sized to load peaks is a concrete
  addition to the thermal architecture, and the printed-module
  approach matches the programme's fabrication level.

(See also arXiv:2611.33381 in §3 — the aligned Ni/LM composite is this
sweep's other thermal headline: 7.5 W/m·K through-plane in an
ultrasoft, laterally insulating sheet.)

## Top 5 papers to read in full

1. **arXiv:2503.03701** (vitrimers) — the skin candidate with the best
   combined stretch/toughness/healing numbers; full text needed for
   healing efficiency % and cycle data the abstract omits.
2. **arXiv:2602.20963** (DEA lifetime self-driving lab) — the method
   most directly copyable for our own actuator lifetime programme.
3. **arXiv:2611.33381** (aligned Ni/LM thermal composite) — if the
   7.5 W/m·K at 160 kPa holds in full text, it rewrites the thermal
   interface assumptions in the power/thermal budget.
4. **arXiv:2204.04468** (double-drawn CNT fibres) — decides whether
   CNT yarn belongs on the tendon shortlist at all.
5. **arXiv:2512.17940** (220 V thin DEA) — the low-voltage DEA data
   point; full text needed for force/strain at that voltage, which
   the abstract does not state.

## Claims in our existing docs that this sweep updates

- **`dea-deep-dive.md` — "the drive is 1–6 kV."** Updated by
  arXiv:2512.17940 (220 V actuation in 8 µm films) and
  arXiv:2502.06166 (1.8 kV switching on a 2.5 g board). The kV framing
  stands for body-scale devices, but the low-voltage floor is much
  lower than the doc implies, and HV electronics mass is no longer a
  first-order blocker.
- **`dea-deep-dive.md` §7 — lifetime as a materials property.**
  arXiv:2602.20963 shows lifetime doubling from parameter search
  alone (voltage/frequency/electrode concentration/filler) on a
  single elastomer — lifetime should be treated as an optimisation
  target with an automated bench, not only a material selection.
- **`power-thermal-budget.md` — no phase-change material anywhere.**
  arXiv:2601.18959 demonstrates printed CPCM + liquid hybrid cooling
  for exactly the pouch-cell format a body battery uses. Gap, now
  with a sourced candidate design.
- **`yarn-shortlist-first-sleeves.md` — no CNT fibre.**
  arXiv:2204.04468 reports CNT fibre at ~3.30 N/tex tenacity and
  ~354 W/m·K thermal conductivity, ahead of the shortlist's polymer
  fibres on both axes. The shortlist needs a CNT entry with cost and
  braidability caveats, or an explicit reason for exclusion.
- **`skin-systems-survey.md` §5 — vitrimer self-healing unquantified.**
  arXiv:2503.03701 supplies the numbers (~80× stretch, ~40 MJ/m³
  toughness, RT healing at low crosslink density) — and a caution the
  survey lacks: that damping level (tan δ >0.3 over five frequency
  decades) disqualifies the same chemistry from elastic-return roles.
- **No contradiction found** to the central conclusions of
  `artificial-muscle-landscape.md` (DEA not yet a large-joint prime
  mover; lifetime as the discriminator) — this sweep's DEA papers
  reinforce both, at smaller scales than the doc's load cases.
