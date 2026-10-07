# Braided Mesh Integration: Tendons, Tactile Sensing, and Embedded Systems

**Status:** Engineering design document — v1.0
**Date:** 2026-10-07
**Project:** Xynthetix synthetic body program — braided soft tissue over skeletal core

## 0. Overview

A braided synthetic body is not just structure. The braid must simultaneously
carry: structural load, tendon actuation, tactile sensing, power/data
distribution, and elastic return — in one integrated mesh. This document
distills the research into buildable design rules: what goes where, in what
order, and what must be designed in from day one versus what can be added
later.

## 1. Tendon systems

### 1.1 Biomimetic model

The reference design is the human flexor tendon–sheath–pulley system:

- **Annular pulleys (A2/A4 analogues):** bone-anchored, carry the
  anti-bowstringing load. These are the hard points — everything else hangs
  off their placement.
- **Cruciate pulleys:** collapse accordion-like on flexion; the joint zones
  of the braid program must be collapsible, not stiff.
- **Quantitative bound:** >1 mm tendon–bone standoff = bowstringing
  (abnormal). Guide height directly sets the moment arm — design it, don't
  inherit it.
- **Sheath:** synovial-sheath analogue (PTFE tube) + lubricated gliding
  surface. Friction is the enemy; the sheath is the defense.

### 1.2 Materials and tensioning

- **Tendon fiber:** braided UHMWPE (Dyneema / Spectra). Best modulus and
  linearity in comparative testing. Braided — not monofilament — for
  flexibility and handling.
- **Sheath:** PTFE tube. Proven low-friction build: PTFE-coated braided
  line in soft robotic gloves.
- **Pretension:** ~80 N ± 20 N, locked with crimp sleeves. Passive spring
  preload prevents slack on reversal.
- **Capstan friction:** tension multiplies at every bend. Budget total wrap
  angle like money, and keep relaxed-side tension low.
- **Creep — the long-term killer:** Dyneema creeps permanently above ~15%
  of minimum breaking load (SK78 ≈ 0.9%/yr, DM20 ≈ 0%/yr at 20% MBL).
  Spec low-creep grade AND provide spring take-up for re-tensioning.
  This is a maintenance item, not a fit-and-forget item.
- **Excursion:** excursion = Σ (moment arm × joint angle) over the routed
  path. Size actuator stroke from this, not from guesses.

### 1.3 Allonic reference

Allonic's Hand Mk2 demonstrates braided tendons and pulleys integrated in a
single automated production run — existence proof that co-braiding tendons
works. No public data on pulley geometry, tendon spec, tensioning, or
sensors. Treat as proof of possibility, not a recipe.

## 2. Tactile sensing

### 2.1 Sensing yarns

Established transduction mechanisms in yarn form:

- **Capacitive:** woven/knitted conductive yarns; auxetic helical yarns
  give very high strain sensitivity. Good for touch/proximity.
- **Piezoresistive:** coaxial stainless-steel / nanocomposite fibers,
  machine-knittable. Good for static pressure.
- **Piezoelectric (PVDF):** dynamic only — poor static response. Vibration
  and slip, not held pressure.
- **Fiber-optic (FBG):** ~14.5 pm/N demonstrated in finger sensors.
  Excellent repeatability, harder fan-out.
- **Magnetoresistive in braided yarns:** emerging, washable,
  braid-compatible. Watch this space.

Co-braiding functional yarns with structural yarns is established practice
(triboelectric e-textiles, conductor pre-wound with para-aramid before
braiding).

### 2.2 The golden rule

**Digitize near the skin, bus out.** Never run hundreds of analog lines
through a braid. Row–column matrix addressing plus daisy-chained serial bus
achieves >8,000 taxels/m² at >50 FPS with power and comms in a single cable
channel per limb. Local digitizer pockets must be designed into the braid
from day one.

ML super-resolution buys 10–60× localization beyond the physical taxel
pitch — resolution is partly software.

### 2.3 Durability (honest numbers)

- Hysteresis: 5.5–8.7% full-scale, typical.
- Drift: ~1.6%/hour — calibration is a runtime process, not a factory step.
- Cycle life: ~20k cycles in lab conditions.
- Silver-coated conductors fail by coating cracking/delamination under
  repeated flex. Prefer intrinsically conductive or encapsulated conductors.

## 3. Embedded power, data, elastics, cooling

- **Conductors:** braided copper-wire textiles survive >700% strain.
  Commercial woven power/data webbing exists. Route as axial inlays,
  encapsulate in TPU/silicone.
- **Elastic return:** dorsal elastic extensors and joint elastics are
  standard; elastane-core wrapped yarns take 200% strain. Passive return
  is textile-compatible — don't motorize what a rubber band does free.
- **Cooling:** embedded water jackets with active control exist, but
  co-braided *sealed* fluid channels are not established practice.
  Cooling is a later addition, not day one.

## 4. The layer cake (deep → superficial)

1. **Deep:** structural braid + tendon sheaths and guide rings on the bone.
2. **Mid:** bus conductors (axial inlays) + dorsal elastic return system.
3. **Superficial:** sensor yarns.
4. **Outer:** protective braid / skin.

### Build sequence

1. Skeletal core.
2. Deep braid + tendon guides/sheaths.
3. Lay axial inlays: tendons threaded through sheaths, bus conductors,
   elastics.
4. Mid braid — locks the inlays in place.
5. Superficial sensor yarns.
6. Outer skin.
7. Pre-stretch, pretension, calibrate.

## 5. Tufted sensory layer (latch-hook / crochet concept)

Instead of (or alongside) co-braided sensor yarns: apply the sensing layer
*after* braiding, using textile tufting techniques — latch-hook or crochet
stitches worked through the braid interstices.

### 5.1 How it works

- **Latch-hook:** a latch hook pulls a short yarn segment through the braid,
  forming a loop/tuft anchored in the mesh. Each tuft is a tactile pile
  element — a taxel with physical height.
- **Crochet:** chain/slip stitches worked through the braid lay sensor yarn
  in precise surface paths — good for routing sensor buses and defining
  sensing zones.

### 5.2 Why it's strong

- **Reinforcement for free:** every stitch passes through the braid
  thickness — the sensory layer doubles as through-thickness binders, the
  anti-delamination strategy. Structure and sensing in one operation.
- **Serviceability:** a damaged tuft can be re-hooked. Co-braided sensors
  are entombed; tufted sensors are maintainable. This is the killer
  advantage — no other sensing approach offers field repair at the taxel
  level.
- **Manufacturing precedent:** carpet tufting machines are mature,
  high-speed, cheap technology. A modified tufting gun applies sensor tufts
  to a braided form. Precedent exists in research: "PileUp" (arXiv
  2511.21000) demonstrated tufted capacitive touch, compression sensing,
  and haptic zones in e-textiles.
- **Fur as sensor:** for furry morphologies, the tufted pile IS fur — and
  every tuft can be a sensor. The pelt becomes the tactile array. Stroke
  the fur and the body feels it, tuft by tuft.
- **Zoned density:** tuft spacing sets taxel pitch per region — dense on
  fingertips and erogenous zones, sparse on the back. The sensory map is
  literally hooked in by hand or by gun.

### 5.3 Design rules

- Tuft anchor must engage at least two braid yarns (no pull-through).
- Conductive tuft yarns terminate into the mid-layer bus at zone
  boundaries — crochet-stitched bus paths route them there.
- Pile height is a design parameter: longer pile = more pre-travel,
  softer initial touch, better shear sensing.
- Keep tufting after the mid-braid lock but before the outer skin, or
  integrate tufts AS the outer layer.

## 6. Day-one vs. later

**Day one (cannot retrofit):**
- Tendon guide architecture: paths, guide heights, liners, wrap-angle budget.
- Zone-varying braid program: stiff pulley-analogue zones vs. collapsible
  joint zones.
- Tension-maintenance provision + low-creep fiber spec.
- Co-braided power/serial-bus inlays with digitizer pockets.
- Sensor-yarn carrier paths (or tuft anchor zones, if tufted).
- Dorsal elastic return system.
- Through-thickness binder strategy (tufting doubles as this).

**Later (designed-for, added when ready):**
- Sensor calibration and drift compensation (software).
- Upgraded sensing modalities into pre-designed paths.
- Cooling channels.
- Lubricant-sheath upgrades, actuator-pack refinements.
- Cosmetic outer skins.

## 7. Failure modes to design against

- Tendon fraying at guide edges → radius all guides, specify liners.
- Tendon creep → low-creep fiber + re-tensioning provision.
- Sensor drift/hysteresis → runtime calibration, not factory calibration.
- Wire fatigue at flex points → axial inlays with service loops at joints.
- Coating delamination on conductors → prefer intrinsic conductors.
- Inter-layer delamination → through-thickness binders (tufting).

## Sources

- Allonic (allonic.co) — company site and Hand Mk2 video; press coverage
  (humanoid.guide, VoxelMatters).
- Maypole braiding mechanics — Herzog, Mayer & Cie., Wardwell machine
  documentation; Gurley et al., ASME J. Mech. Design 137 (2015).
- Fraens 3D-printed braiding machine V3.0 (printables.com/model/1367079).
- TexGen, University of Nottingham (open source).
- Tendon/sheath biomechanics — annular ligament literature; continuum
  robot surveys (MDPI); Intuitive Surgical capstan patents.
- E-textile sensing — PileUp (arXiv 2511.21000); triboelectric 3D-braided
  e-textile (Nat. Commun. 2020); magnetoresistive braided yarns
  (Commun. Eng. 2025); BYU high-density tactile bus paper.
