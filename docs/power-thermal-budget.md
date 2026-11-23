# Power & Thermal Budget for a Warm Synthetic Body

**Status:** research note, 2026-11-23. Workstream: Skin, power &
thermal (see `docs/research-queue.md`). Every externally sourced
number carries a citation. Everything else is labelled **estimate**
and the arithmetic is shown so the assumptions can be argued with.

**The problem in one paragraph.** A synthetic body that is warm to
touch (skin surface 35–37 °C) in a normal room is a body that leaks
heat continuously, carries its entire energy supply on board, and
must also reject the waste heat of its own actuators and computer
through the same skin it is trying to keep warm. These three facts
fight each other. This note sizes each one.

**Reference body used throughout** (assumption, stated once):
height 1.75 m, mass 75 kg, indoor conditions 21 °C, still air.

---

## 1. Heating the surface to 35–37 °C

### 1.1 Surface area

The Du Bois formula, A = 0.202 · W^0.425 · H^0.725, gives ≈ 1.8 m²
for a 70 kg, 1.73 m person, and 1.8 m² is the standard "average
person" area used in thermal-comfort modelling
([EnergyPlus engineering reference](https://energyplus.readthedocs.io/en/latest/guides/engineering-reference/19.1-occupant-thermal-comfort.html)).
For our 75 kg / 1.75 m reference body the same family of formulas
gives ≈ 1.9 m² (arithmetic from the formula above; **estimate**).

### 1.2 The physics of the leak

Dry heat loss from a surface is q = h · A · ΔT, where the combined
convective + radiative coefficient in still indoor air is about
7.8–8 W/(m²·K): manikin measurements give a whole-body natural
convection coefficient of 3.3–3.4 W/(m²·K) and a radiative
coefficient of ≈ 4.5 W/(m²·K), and the two add because they act in
parallel ([heat-transfer coefficient summary of the de Dear manikin
work](https://www.heatjac.com/knowledge/what-is-a-heat-transfer-coefficient)).

Worked cases (A = 1.9 m², h = 7.8 W/(m²·K); all **estimates** from
the formula above):

| Case | Skin | Room | ΔT | Heat loss |
|---|---|---|---|---|
| Bare skin | 36 °C | 21 °C | 15 K | 7.8 × 1.9 × 15 ≈ **222 W** |
| Bare skin | 35 °C | 24 °C | 11 K | ≈ **163 W** |
| + 1 clo cover | 36 °C | 21 °C | 15 K | ≈ **101 W** |
| + 2 clo cover | 36 °C | 21 °C | 15 K | ≈ **65 W** |
| + 1 clo cover | 35 °C | 24 °C | 11 K | ≈ **74 W** |

The clo rows use series resistance: 1 clo = 0.155 m²·K/W of thermal
resistance ([layering/heat-balance explainer](https://campgearexperts.com/clothing/layering-system/)),
the bare-surface resistance is 1/h ≈ 0.128 m²·K/W, so with 1 clo
the total is 0.283 m²·K/W and q = A·ΔT/R = 1.9 × 15 / 0.283 ≈ 101 W.
"Cover" here means fur, hair, or clothing over the skin — anything
that traps still air above the heated surface cuts the bill roughly
in proportion to its clo value.

**Sanity anchor from human physiology.** The clo unit itself is
defined around a resting person producing heat at 58 W/m²
([ASTM F2371 text](http://file.yizimg.com/33331/2008051412103728.pdf)) —
about 100 W over a whole body — and thermal manikins in clothing
tests are routinely held at a mean skin temperature of 33 °C
against chamber air around 22.5 °C
([manikin study, TEKSTİL ve KONFEKSİYON](https://dergipark.org.tr/en/download/article-file/218059)).
So a bare, uninsulated 36 °C robot skin loses **roughly twice what
a resting human body produces in total**. A human gets away with
33 °C skin because a metabolism pays the bill for free; a synthetic
body pays it out of its battery. Insulation (fur/cover) and zoning
are not optional refinements — they are the difference between a
~220 W and a ~70–100 W continuous heating load.

### 1.3 What heated clothing teaches — and where it stops applying

A representative heated fleece jacket draws 15 W at 7.4 V, heating
six local zones (abdomen, back, neck, waist) to surface settings of
35–60 °C, and runs 3/6/10 h on its 16,000 mAh pack at high/medium/
low settings
([retail specification](https://www.homedepot.com/p/SKYSHALO-Heated-Fleece-Jacket-for-Men-Black-with-7-4V-16000mAh-Power-Bank-Pack-6-Zones-3-Temp-Levels-3h-6h-10h-2025-update-JRYLRKSWMNKXDM5N1001V9-251117/339876360)).
Two lessons transfer: (1) **zoning works** — heating only
contact-relevant areas is an order of magnitude cheaper than
heating everything; (2) carbon-fibre/film zone heaters are a
solved, cheap component. The limit: a heated jacket supplements a
~100 W human furnace underneath it and only warms patches. A
synthetic body has no furnace unless we build one — which is
exactly what §3's waste heat becomes if we plumb it instead of
dumping it.

### 1.4 Design consequences for heating

- **Heat from the inside out, insulate under the skin.** Put the
  heating layer at the skin and insulation *below* it (between
  heater and body interior), so heater output preferentially flows
  outward to the touch surface rather than cooking the interior.
- **Zone it.** Torso, hands, face, and other contact surfaces get
  full 35–37 °C service; covered or rarely touched areas can run
  cooler or follow the fur/cover strategy.
- **Fur is a heating technology.** Every clo of surface cover is
  worth roughly 50–60 W of continuous battery power in the
  reference conditions above (222 W bare → 101 W at 1 clo).

---

## 2. Batteries: what a body can carry

### 2.1 Cell level

A current high-energy 21700 cell, the Samsung INR21700-50E, stores
18.0 Wh (5,000 mAh × 3.6 V nominal) at 69 g — **261 Wh/kg** — with a
modest 9.8 A maximum continuous discharge
([CellBench cell data](https://www.cellbench.io/cells/samsung-50e);
[datasheet compilation](https://www.aboutenergy.io/voltt-battery-library/samsung-50e)).
High energy and high power trade against each other in the same
format: the same-capacity 50S variant raises continuous discharge
to 25 A at the same 18.0 Wh
([cell comparison data](https://www.ebikeengineering.com/articles/cell-selection-18650-vs-21700)).
Actuator peak currents, not just total energy, size the cell
choice.

### 2.2 Pack level — derate honestly

Cells are not packs. Housing, BMS, busbars, fusing, and thermal
hardware cost mass: EV experience puts pack-level specific energy
at roughly 140–180 Wh/kg against 260–300 Wh/kg cells, i.e. a pack
keeps only ~55–70 % of the cell-level figure
([cell-vs-pack analysis](https://autoedgeview.com/battery-news/ev-cell-pack-density-lab-myths-busted)).
A robot pack carries less crash armour than a car pack but adds
swap hardware and distributed mounting. **Planning figure used
below: 180 Wh/kg at pack level (estimate).** At that figure:

- 1 kWh of pack ≈ 5.6 kg
- 2.25 kWh of pack ≈ 12.5 kg (estimate)

### 2.3 What shipping humanoids actually carry

| Robot | Pack | Quoted runtime | Implied average draw |
|---|---|---|---|
| Unitree G1 (1.32 m, ~35 kg) | 13-series, 9,000 mAh quick-release pack; ≈ 420 Wh (estimate: 13 × 3.6 V × 9 Ah) | ~2 h | ≈ 210 W (estimate) |
| Figure 02 (1.68 m, 70 kg) | 2.25 kWh, integrated in torso | 5 h target | ≈ 450 W (estimate) |

Sources: the G1's 9,000 mAh quick-release battery and ~2 h runtime
are retail/official-channel specifications
([RobotShop G1 listing](https://www.RobotShop.com/products/unitree-g1-humanoid-robot-us)).
Figure states its 2.25 kWh pack is swappable "but it is not a
quick swap procedure", and that the company is "targeting a
5-hour run time" doing manipulation work
([IEEE Spectrum interview](https://spectrum.ieee.org/figure-new-humanoid-robot?utm_campaign=Data%20Points&utm_source=hs_email&utm_medium=email&_hsenc=p2ANqtz-_g-AQyzty5pKOXuo5OHZXA7NExYqieYD0OwnRzAjAYq53n4D7nKtfahu8bCfDJfP2Ds7eG)).
The implied average draws are simple division (energy ÷ runtime)
and are marked estimates — neither maker publishes a measured
average power.

Two architectures, two philosophies:

- **Small pack + true hot-swap (G1 pattern).** ~0.42 kWh, swapped
  in seconds; the robot never waits to charge, but a human (or a
  dock) must feed it packs every ~2 h.
- **Large integrated pack (Figure pattern).** 2.25 kWh buys a
  working shift between charges, at ~12.5 kg (estimate, §2.2) of
  battery carried in the torso — which also lowers the centre of
  mass — but "swappable" there means a service procedure, not a
  field swap.

A split architecture (estimate, our synthesis): a small
always-present reserve pack (keeps compute, sensing, and skin
warmth alive, ~100–200 Wh) plus a main swappable pack. The reserve
decouples "changing the battery" from "the body goes cold and
dead", which matters for a body whose warmth is a feature.

### 2.4 Runtime arithmetic

Runtime = usable energy ÷ average draw. Usable energy is taken as
80 % of nameplate (estimate — depth-of-discharge and ageing
margin). Runtimes in hours:

| Average draw | 0.42 kWh pack (0.34 usable) | 1 kWh pack (0.8 usable) | 2.25 kWh pack (1.8 usable) |
|---|---|---|---|
| 50 W | 6.7 h | 16 h | 36 h |
| 100 W | 3.4 h | 8 h | 18 h |
| 250 W | 1.3 h | 3.2 h | 7.2 h |
| 450 W | 0.75 h | 1.8 h | 4 h |

The 450 W row reproduces Figure's 5 h target only if the draw is a
bit lower or the usable fraction higher — the table is arithmetic,
not a claim about their robot.

---

## 3. The cooling problem: heat that has to leave through warm skin

### 3.1 Where the internal heat comes from

- **Actuators.** Motor winding heat scales with torque squared
  (Q̇ ∝ M², via I²R losses), and — critically — a motor holding a
  joint still against gravity converts *all* of its electrical
  input to heat while doing zero mechanical work
  ([Hochberg et al., evaporative cooling of humanoid
  actuators](https://www.ais.uni-bonn.de/humanoidsoccer/ws13/papers/HSR13_Hochberg.pdf)).
  Standing still is not thermally free.
- **Compute.** A Jetson AGX Orin-class module is configurable
  between 15 W and 60 W
  ([NVIDIA technical brief](https://www.nvidia.com/content/dam/en-zz/Solutions/gtcf21/jetson-orin/nvidia-jetson-agx-orin-technical-brief.pdf));
  essentially all of it becomes heat inside the body. The Device
  (2025) flexible-cooling work notes explicitly that the low
  thermal conductivity of the polymer materials used for humanoid
  artificial skin obstructs chip cooling
  ([Du et al., Device 2025](https://doi.org/10.1016/j.device.2024.100576)).
- **The skin itself is an insulator.** Unfilled silicone rubber has
  a thermal conductivity around 0.2 W/(m·K)
  ([silicone property summary](https://rysilicone.com/silicone-thermal-conductivity/)) —
  good for keeping heater output at the surface, bad for letting
  interior heat out. Filled grades reach 1–5 W/(m·K) at the cost of
  stiffness, so conductivity can be *placed* (conductive pads over
  heat sources, insulating silicone elsewhere) rather than uniform.

### 3.2 The surface bottleneck, quantified

Ultimately every watt must cross the outer surface with the same
h ≈ 7.8 W/(m²·K) from §1.2. If the skin must stay at or below
~37 °C for touch, the maximum rejectable heat is set by the room:

- Room 21 °C: 7.8 × 1.9 × (37 − 21) ≈ **237 W** (estimate)
- Room 30 °C: 7.8 × 1.9 × (37 − 30) ≈ **104 W** (estimate)
- Room 35 °C: ≈ **30 W** (estimate) — a warm day defeats passive
  rejection almost entirely.

This is the central thermal fact of a warm body: **in a cool room
the skin is a radiator with ~240 W of headroom and waste heat is a
resource that offsets the heating bill; in a hot room the same
body cannot shed even its idle heat passively.** Designs that
ignore the second case will thermal-throttle exactly when a human
body would be sweating — which points at the same solution (§3.3,
evaporative).

### 3.3 Approaches in the literature

1. **Liquid cooling loops to the joints.** Liquid-cooled motor
   jackets on the DRACO biped's viscoelastic actuators enabled
   2.5× higher continuous torque than conventional electric
   actuators
   ([arXiv:1906.03811](https://arxiv.org/pdf/1906.03811)).
   Liquid moves heat from where it is made to where it can be
   rejected — for us, to the skin, which is the radiator.
2. **Whole-body vascular networks.** A 2026 optimisation study of a
   coolant network spreading Unitree G1 actuator heat over the
   whole shell and a back radiator (1.36 kg of network, 60 °C shell
   limit — an industrial limit, too hot for a touch body) raised
   the sustainable work fraction from 0.14 (baseline) to 0.72 in
   simulation across hot-ambient tasks
   ([SSRN preprint](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=7674805)).
   The transferable result is the *spreading*: heat sharing only
   helps when the shared heat actually leaves through shell or
   radiator. Our shell limit is ~37 °C, not 60 °C, so our fluxes
   are lower — but our radiator is the entire skin, and in cool
   rooms the heat is wanted there anyway.
3. **Evaporative cooling (sweating).** Evaporating water removes
   ≈ 2,257 kJ/kg
   ([heat-balance explainer](https://campgearexperts.com/clothing/layering-system/)),
   so rejecting 100 W evaporatively costs 100 × 3600 / 2.257e6 ≈
   **0.16 kg of water per hour** (arithmetic; estimate). Hochberg
   et al. showed actuator evaporative cooling works with "relatively
   small amounts of water" under soccer-match loads (paper above).
   Sweating is the only approach whose capacity *grows* as the room
   approaches skin temperature — it does not depend on ΔT to air.
   It costs a water reservoir and a wettable skin.
4. **Flexible microfluidic cooling for chips.** Manifold +
   embedded-microfluidic cooling built for humanoid chips achieves
   a thermal resistance of 0.089 cm²·K/W while flexing, and imposes
   only ~5 % of the stress of conventional packaging
   ([Du et al., Device 2025](https://doi.org/10.1016/j.device.2024.100576)) —
   evidence that coolant can be routed through soft structures,
   not just rigid cold plates.
5. **Behavioural thermal management.** On NASA's Valkyrie,
   operators must pause work when torso/leg actuator temperatures
   reach unsafe levels; Jorgensen et al. formalised recovery as
   choosing body configurations that minimise future actuator
   temperatures ("thermal inverse kinematics")
   ([arXiv:1902.00187](https://arxiv.org/pdf/1902.00187v4)).
   Posture is a cooling control input: spreading load across
   joints, sitting, and leaning all cut I²R heating at the hot
   joints. Free in hardware, expensive in capability — a body that
   must keep sitting down to cool off is limited, but as a safety
   layer it costs nothing.

### 3.4 The synthesis we should design to

One coolant loop, three jobs: collect actuator and compute waste
heat, deliver it to the skin (paying most of the §1 heating bill in
cool rooms), and top up with zone heaters only where the loop
cannot reach or the room is cold. In hot rooms the same loop feeds
evaporative panels. The heating system and the cooling system are
the same system, run in different proportions — sizing them
separately double-pays the mass and power.

---

## 4. Worked budget: reference body, indoor social duty

Scenario (assumptions): reference body (§0), room 21 °C, standing /
sitting / light movement and conversation, skin service 35–37 °C
on contact zones, fur/cover ≈ 1 clo over most of the body, coolant
loop recovering actuator + compute waste heat to the skin.

| Line | Power | Basis |
|---|---|---|
| Compute (AGX Orin class, mid profile) | 30 W | Within the 15–60 W configurable range (NVIDIA brief, §3.1) |
| Sensors, control electronics, audio, misc | 15 W | **Estimate** |
| Actuation, average (posture + light movement) | 120 W | **Estimate**, bracketed by the implied ~210 W average of the smaller, more active G1 and ~450 W for Figure's work duty (§2.3) |
| Skin heating, gross need | ~100 W | §1.2, 1-clo case (estimate) |
| − waste heat recovered to skin | −60 W | **Estimate**: a fraction of actuation + compute losses routed via coolant loop; capped by what the loop can collect |
| Skin heating, net electrical | ~40 W | Arithmetic |
| Pumps + fans | 10 W | **Estimate** |
| Conversion / distribution losses | ~20 W | **Estimate**, ~10 % of throughput |
| **Total average draw** | **≈ 235 W** | Sum |

Runtime on the §2.4 basis (estimates):

- 2.25 kWh pack (1.8 kWh usable): 1.8 / 0.235 ≈ **7.7 h**
- 1 kWh pack (0.8 usable): ≈ **3.4 h**
- Sleep/standby variant (actuation ~5 W, compute idle ~10 W,
  heating dominant ~65 W with 2-clo-equivalent rest cover,
  total ≈ 85 W): 1.8 / 0.085 ≈ **21 h** (estimate)
- Hard-work variant (450 W total): 1.8 / 0.45 = **4 h** (estimate)

Battery sizing backwards: an 8 h day at 235 W needs 1.88 kWh
usable → 2.35 kWh nameplate → at 180 Wh/kg pack level ≈ **13 kg
of battery** (estimates). Every 10 W shaved off the average draw
is worth ~0.55 kg of battery on an 8 h day (arithmetic:
10 W × 8 h = 80 Wh usable → 100 Wh nameplate → 0.55 kg at
180 Wh/kg). Heating and cooling efficiency *is* body weight.

---

## 5. Open questions for the next passes

- Measured (not estimated) average actuation power for standing
  and slow walking at 75 kg scale — the 120 W line is the softest
  number in §4.
- Skin heater technology comparison: carbon film vs etched foil
  vs conductive textile, W/cm² and failure behaviour.
- Evaporative skin: reservoir sizing, hygiene, and whether a
  damp-to-touch surface is acceptable for a warm body (it reads
  as sweat; that may be a feature or a defect depending on the
  body).
- Battery placement vs the coolant loop: packs are also heat
  sources under high discharge and heat sinks when cold; the
  vascular-cooling study above already treats the battery as a
  node in the network.
- Hot-climate operation (>30 °C ambient) as a first-class design
  case, not an afterthought: §3.2 says passive rejection nearly
  vanishes there.

## Sources

1. EnergyPlus engineering reference — Du Bois area, comfort model:
   https://energyplus.readthedocs.io/en/latest/guides/engineering-reference/19.1-occupant-thermal-comfort.html
2. Heat-transfer coefficients (de Dear manikin data summary):
   https://www.heatjac.com/knowledge/what-is-a-heat-transfer-coefficient
3. Clo definition and heat-balance arithmetic:
   https://campgearexperts.com/clothing/layering-system/
4. ASTM F2371 — 58 W/m² resting heat production, clo definition:
   http://file.yizimg.com/33331/2008051412103728.pdf
5. Thermal manikin clothing study (skin held at 33 °C):
   https://dergipark.org.tr/en/download/article-file/218059
6. Heated fleece jacket specification (15 W, 6 zones, runtimes):
   https://www.homedepot.com/p/SKYSHALO-Heated-Fleece-Jacket-for-Men-Black-with-7-4V-16000mAh-Power-Bank-Pack-6-Zones-3-Temp-Levels-3h-6h-10h-2025-update-JRYLRKSWMNKXDM5N1001V9-251117/339876360
7. Samsung INR21700-50E cell data (18.0 Wh, 69 g, 261 Wh/kg):
   https://www.cellbench.io/cells/samsung-50e
8. Samsung 50E datasheet compilation:
   https://www.aboutenergy.io/voltt-battery-library/samsung-50e
9. 21700 cell comparison (50E vs 50S discharge ratings):
   https://www.ebikeengineering.com/articles/cell-selection-18650-vs-21700
10. Cell-level vs pack-level specific energy:
    https://autoedgeview.com/battery-news/ev-cell-pack-density-lab-myths-busted
11. Unitree G1 specifications (9,000 mAh quick-release, ~2 h):
    https://www.RobotShop.com/products/unitree-g1-humanoid-robot-us
12. Figure 02 battery interview (2.25 kWh, 5 h target, swap):
    https://spectrum.ieee.org/figure-new-humanoid-robot?utm_campaign=Data%20Points&utm_source=hs_email&utm_medium=email&_hsenc=p2ANqtz-_g-AQyzty5pKOXuo5OHZXA7NExYqieYD0OwnRzAjAYq53n4D7nKtfahu8bCfDJfP2Ds7eG
13. Hochberg et al. — evaporative cooling of humanoid actuators:
    https://www.ais.uni-bonn.de/humanoidsoccer/ws13/papers/HSR13_Hochberg.pdf
14. DRACO liquid-cooled actuators (2.5× continuous torque):
    https://arxiv.org/pdf/1906.03811
15. Jorgensen et al. — thermal recovery, NASA Valkyrie:
    https://arxiv.org/pdf/1902.00187v4
16. Whole-body vascular cooling network for a humanoid (G1 study):
    https://papers.ssrn.com/sol3/papers.cfm?abstract_id=7674805
17. Du et al. — flexible microfluidic chip cooling, Device 2025:
    https://doi.org/10.1016/j.device.2024.100576
18. NVIDIA Jetson AGX Orin technical brief (15–60 W):
    https://www.nvidia.com/content/dam/en-zz/Solutions/gtcf21/jetson-orin/nvidia-jetson-agx-orin-technical-brief.pdf
19. Silicone rubber thermal conductivity (~0.2 W/(m·K)):
    https://rysilicone.com/silicone-thermal-conductivity/
