# Maypole Braider Prior Art — DIY / Open-Source Survey

**Status:** Research note — 2026-11-23 (Monday rotation: braider hardware)
**Purpose:** Map what documented DIY / open maypole braiding machines
actually exist, what can be replicated from their documentation, and
where the gaps are that Xynthetix Phase 1 (see
[`company-roadmap.md`](company-roadmap.md)) would fill.

Every factual claim below is cited to a source that was opened and read
for this survey. Where a detail could not be verified from the source,
it is marked *not stated* rather than guessed.

## Summary

The roadmap's first wedge claim holds up: DIY maypole braiders exist,
but there is **no free, openly licensed, complete, replicable design**.
The single best-documented machine (Fraens, 12 carriers) is sold as a
paid download under a personal-use licence, so it can be studied but
not forked. The best free design documentation (kmatch98) covers the
horn-gear layout and an excellent carrier, but explicitly leaves the
take-up mechanism out of scope and ships no BOM, firmware, or licence.
The only parametric (OpenSCAD) design is unfinished — its author lists
the bobbin carriers as a to-do. Everything else is video fragments,
paid LEGO instructions, or industrial/academic machines that document
design parameters rather than a buildable desktop machine.

## Documented builds

### 1. Fraens — 3D printed braiding machine (12 carriers) ⭐ most complete

- Project page: https://hackaday.io/project/191583-3d-printed-braiding-machine/details
- Files (paid): https://cults3d.com/en/3d-model/tool/3d-printed-braiding-machine-fraens-2
- Coverage: https://hackaday.com/2023/06/21/3d-printed-machine-shows-how-braiding-is-done/

Verified from the project page and the Cults listing:

- **Carriers:** up to 12 spool carriers; fewer can be fitted. Hackaday's
  coverage describes the carriers running on a continuous track around
  the centre, passed between a series of six meshed gears.
- **Horn gears / track:** carriers are pushed along the track by horn
  gears and hand over from one gear to the next at the crossing points.
  All gears use involute tooth profiles to reduce friction. The base /
  track plate is laser-cut acrylic (milling or careful saw work is
  offered as an alternative).
- **Drive:** 24 V geared motor — one motor suffices for ≤6 carriers,
  two motors are needed at 12 carriers; a simple PWM controller runs
  both motors in synchronism. Motor-to-gear coupling is a 3D-printed
  clamping set.
- **Take-up:** a worm-gear-driven take-off unit, mechanically coupled
  to the drive. Take-off speed is set by swapping the gear ratio:
  slower take-off gives a closed (dense) braid, faster gives an open
  braid. This is open-loop — the ratio is fixed once the gears are
  chosen.
- **Carrier tension:** a spring tensioning mechanism keeps each rope
  taut as the carrier's distance to the braiding point varies, and a
  locking lever releases the spool incrementally so tension cannot
  unthread the spool. All rope deflection points use eyelets to cut
  friction.
- **Core feed:** a centre tube feeds a core material (thin cable,
  plastic core), and a finished braid can be re-braided over itself to
  make a thicker cord.
- **Build cost in effort:** ~60–100 hours of printing, ~1.5 kg of
  filament. The carrier springs are wound by the author on a lathe
  (a screwdriver-based winding method is suggested as a fallback).
- **What you get for the files:** all STLs, the complete model in
  STL/STEP, assembly and exploded drawings, a 1:1 track-plate cutting
  drawing, drawings of the metal parts to make, a parts list with
  supplier links, and an assembly video (~3.2 GB total).
- **Licence:** sold for US$39.36+ on Cults under the "CULTS PU"
  (personal use) licence. **This is not an open licence** — the design
  cannot legally be forked or republished. It is prior art to learn
  from, not a Phase 1 base.

### 2. kmatch98 — Braiding Machine: maypole braider and bobbins ⭐ best free documentation

- Project page: https://hackaday.io/project/181960-braiding-machine-maypole-braider-and-bobbins
- Instructions: https://hackaday.io/project/181960/instructions

Verified from the project and instructions pages:

- **What it is:** "basic guidelines on designing a 3D printed maypole
  style braiding machine" — a design guide plus full Fusion 360 and
  STEP files (machine and carrier), published free on Hackaday.io in
  October 2021. A licence for the files is *not stated* on the project
  page.
- **Architecture:** interconnected spur gears under the frame each
  drive one horn gear through a shaft on a bearing; because adjacent
  spur gears counter-rotate, adjacent horn gears always rotate in
  opposite directions. The horn gear's slot grabs a peg on the carrier;
  a foot ("shoe") on the carrier slides in the figure-8 track and
  steers it through the track intersections. A print-in-place hand
  crank version exists alongside the motorisable layout.
- **Carrier count:** *not stated* as a machine total. The page shows a
  demonstration with three bobbin carriers attached; the design is a
  guide for sizing your own ring rather than a fixed-count machine.
- **Carrier (the real contribution):** commercial carriers use two
  springs; this design uses one. A weighted platform slides on a
  vertical bar and uses **gravity as the primary tensioner** as the
  carrier-to-fell-point distance changes. When tension rises far
  enough, the weight lifts a bracket that pulls a lever and retracts a
  release pin, letting the slotted bobbin spin and pay out yarn; the
  tension drop lets the pin re-engage. Release tension is set by the
  spring, the lever, and the threading path — a full 5-step threading
  diagram is published.
- **Take-up:** explicitly **out of scope**. The guide notes a take-up
  roller must be mechanically linked to the spur gears or
  electronically controlled, that take-up speed vs. gear speed sets
  the braid angle, and that the product should wrap multiple turns
  around two friction wheels to avoid slip — then leaves the design
  to the builder.
- **Gaps:** no BOM, no motor/firmware design, no measured tension or
  braid-quality data, no stated licence.

### 3. Caitlyn B — Maypole Machine (in work), Printables — only parametric design

- Listing: https://www.printables.com/cs/model/345705-maypole-machine-in-work

Verified from the listing:

- An in-progress maypole braider designed in **OpenSCAD**, parametric
  ("the OpenSCAD file scales to your imagination"), all parts designed
  to print without supports. Listed under a Creative Commons
  Attribution 4.0 licence, free.
- Published hardware needs are minimal so far: 10 mm bearings and
  assorted M5 (25 mm, 40 mm) and M3 (~30 mm) screws and nuts.
- Videos linked from the listing show it running with 1 strand per
  carrier and with 3 strands per carrier.
- **Unfinished by the author's own to-do list:** the bobbin carrier
  design is still a to-do, the OpenSCAD needs cleanup/modularising,
  and variants for small/large printers are planned. Carrier count is
  *not stated* (it is a parameter, not a fixed number).
- **Value:** this is the only openly licensed, parametric starting
  point for the horn-gear ring / track geometry — but the hardest
  subassembly (the carrier) does not exist yet in it.

### 4. Nico71 — LEGO Technic braiding machines (adjacent architecture)

- 5-reel machine: https://www.nico71.fr/lego-braiding-machine/comment-page-1/
- Earlier 9-strand machine: https://hackaday.com/2016/02/19/rope-braiding-machine-built-entirely-from-lego-technics/

Not horn-gear maypole machines — included because they solve the same
carrier-transfer problem a different way, and the lessons transfer:

- The documented 5-reel machine passes reels between two
  counter-rotating pallets with a cam-and-connecting-rod pusher;
  3 reels move and 2 are fixed at the centre. The author reports that
  earlier attempts with 3, 12, and 16 reels kept failing on the same
  point: **reels blocking during pallet-to-pallet transfer**. The fix
  was precise synchronisation — chains instead of gears, because gear
  backlash made face-to-face timing unreliable; a 40-tooth chain path
  gives 1/40-turn adjustment resolution.
- Tension is a rubber band on each reel pulley. Output is wound on a
  drum; maximum braiding speed is quoted as 0.60 cm/s (~35 cm/min).
  Power is a single LEGO motor (M, or L in the 2022 enhanced version).
- The 2016 machine covered by Hackaday used three groups of three
  planetary-mounted bobbins (9 strands) on a horizontally spinning
  drum, again single-motor, all synchronised by gears, shafts, chains
  and clutches, with a self-reversing take-up drum.
- **Replicability:** building instructions are a paid PDF (part lists
  are public via Rebrickable: 759 parts standard / 751 enhanced);
  a free photo-sequence build guide is also published. LEGO-only, so
  nothing here forks into a metal/printed machine directly — the
  transfer-timing lesson is the takeaway.

### 5. Fragmentary / video-only builds

- **3D Print World by Bob — 8-bobbin maypole braider (2026):** an
  episodic video series (design → print → test) for an 8-bobbin,
  8-gear machine with Ø34 × 76 mm bobbins for 2 mm cord, later adding
  an upper winder with feed rollers as the take-up. Documented only as
  social video episodes, e.g.
  https://www.facebook.com/reel/1030536373376366/ — no published
  files, BOM, or licence found. Useful as existence proof that 8 is a
  popular DIY carrier count; not replicable from the documentation.

## Design parameters from industrial / academic sources

These are not DIY builds, but they pin down the numbers every maypole
design — DIY or Phase 1 — has to respect.

- **Four slots per horn gear is the industrial norm.** A 2026
  rotary-tunnel-braider study uses a baseline of 96 horn gears × 4
  slots (max 192 carriers):
  https://link.springer.com/article/10.1007/s00170-026-17696-4
  A radial braider analysed in the dynamics literature runs 88 horn
  gears × 4 slots with 176 carriers:
  https://www.hindawi.com/journals/sv/2020/2747204/fig40/
  The Centexbel industrial installation runs 256 horn gears in four
  rings, each with 4 carrier slots plus one extra slot for a uniaxial
  (axial inlay) yarn, enabling triaxial braid:
  https://thread-etn.eu/circular-braiding-the-industrial-experience-with-centexbel/
- **Occupancy patterns are named and standard:** 1F1E (one slot full,
  one empty, alternating) is the usual half-loading; the Springer
  study also analyses 2F2E and 1F3E. With 4-slot gears, pattern
  repeats must be multiples of 2 or 4 slots.
- **Six-pocket drivers change the pattern:** US patent US5257571A
  describes drivers with six pockets carrying three carriers each,
  producing a 3-over/3-under braid instead of the conventional
  2-over/2-under from four-pocket drivers — i.e. horn-gear slot count
  is a braid-architecture choice, not just a capacity choice:
  https://patents.google.com/patent/US5257571A/en
- **Track geometry:** in the classical maypole layout the carrier
  tracks follow approximately the pitch lines of the horn gears and
  cross each other exactly where the gears mesh (US2788700A):
  https://patents.google.com/patent/US2788700A/en
- **Commercial scale reference:** Herzog's SE rope braiders offer
  12–32 carriers at horn-gear pitch sizes of 336 / 432 / 528 mm,
  running 40–60 horn-gear rpm — a useful sanity anchor: even
  industrial rope machines start at 12 carriers:
  https://herzog-online.com/cms/wp-content/uploads/2023/05/Datasheet-SE-1-32-432-1.pdf
- **Carrier counts in practice:** DIY documented builds cluster at
  3 (demonstrator), 5, 8, and 12 carriers. Standard biaxial braid
  needs an even count, half clockwise and half counter-clockwise —
  the same constraint the `.braid` spec already enforces
  (`carriers` must be a positive even integer ≥ 4). 8, 12, 16, and 24
  are the natural Phase 1 waypoints; 12 is the largest count with a
  fully documented DIY precedent.
- **Tension is the known hard problem, at every scale.** The Springer
  study notes that conventional passive spring/roller carriers show
  delayed response and nonlinear tension, and reports an actively
  controlled electronic carrier achieving a programmable
  ~250–520 cN tension range — roughly 40 cN wider than an established
  closed-loop carrier system. No DIY build in this survey publishes
  *any* measured per-carrier tension figure.

## Replicable vs fragmentary

| Project | Files | Docs | BOM | Licence | Replicable unaided? |
|---|---|---|---|---|---|
| Fraens 12-carrier | STL/STEP + drawings (paid) | Assembly video + drawings | Parts list w/ supplier links | CULTS PU (personal use) | Yes — but paid, and cannot be forked |
| kmatch98 | Fusion 360 + STEP (free) | Design guide + threading | None | Not stated | Mostly — except take-up, which is out of scope |
| Caitlyn B (Printables) | OpenSCAD + STL (free) | Listing notes + videos | Bearings/screws only | CC BY 4.0 | No — carriers unfinished |
| Nico71 LEGO | Paid PDF instructions | Photo sequence (free) | Rebrickable part lists | Paid / proprietary | Yes, in LEGO only |
| 3D Print World by Bob | None found | Video episodes only | None | None | No |

Software prior art is in better shape than hardware: braidpy models
horn-gear machines — tracks, collisions, carrier loading, animation —
and is covered in [`braidpy-evaluation.md`](braidpy-evaluation.md), so
Phase 1 track plans can be *verified in simulation* before cutting a
plate, something none of the hardware projects above had available.

## Gaps Phase 1 would fill

Against the Phase 1 exit criteria in the roadmap, the survey shows
these are all still open:

1. **An openly licensed complete machine.** The only complete design
   is personal-use licensed; the only CC-licensed design is
   unfinished. A complete braider under an open hardware licence
   would be the first.
2. **Closed-loop take-up.** Fraens sets braid angle with a fixed worm
   gear ratio; kmatch98 omits take-up entirely; the LEGO builds use
   mechanically slaved drums. Nobody in the DIY record does
   stepper-driven take-up with closed-loop speed control — yet
   take-up speed *is* braid-angle control.
3. **Documented per-carrier tension.** Every builder identifies
   tension as the #1 problem; none publishes a tension value, a
   tension spec, or a calibration procedure. The `.braid` spec's
   planned v1 tension field has no DIY data to draw on — Phase 1
   would be generating it.
4. **A standard BOM.** Only the paid Fraens package has a full parts
   list with suppliers. There is no open BOM standard for a desktop
   braider.
5. **Firmware / control model.** All documented DIY drives are a
   motor + PWM knob (or a hand crank, or a LEGO motor). No published
   firmware, no carrier schedule output, no emergency stop in any
   DIY documentation surveyed.
6. **Braiding over a core as the primary use case.** Fraens has a
   centre tube (for cable/plastic cores); no DIY design targets
   braiding directly over a skeletal core, and none publishes
   angle-variance measurements for braid laid over anything.

## Shortlist — what Phase 1 should learn from

1. **kmatch98's carrier and gear layout — the fork base.**
   Free Fusion 360 + STEP files, the clearest written explanation of
   horn-gear/spur-gear/track interaction in the DIY record, and the
   most thoughtful carrier: gravity primary tension + single-spring
   pin release is simpler than the commercial two-spring pattern and
   is documented down to the threading path. Phase 1 work would be
   everything around it: licence clarification from the author,
   take-up, motorisation, BOM, tension measurement.
2. **Fraens' machine — the architecture reference (study, don't fork).**
   The only proven complete desktop maypole: involute horn gears,
   laser-cut acrylic track plate, worm-gear take-off, centre tube,
   spring carrier with locking lever, and honest build numbers
   (60–100 print hours, 1.5 kg filament, 2 motors at 12 carriers).
   Its personal-use licence bars forking, but its layout decisions —
   especially gear-ratio take-up as the thing to replace with
   closed-loop control — define the bar Phase 1 has to clear.
3. **Caitlyn B's OpenSCAD model — the parametric foundation.**
   The only openly licensed (CC BY 4.0), parameter-driven geometry.
   If Phase 1 wants one design that scales across 8/12/16/24 carriers
   instead of four fixed plates, a parametric horn-gear/track
   generator is how — this is the seed, with kmatch98's carrier
   supplying the subassembly it lacks.

## Sources

All opened and read 2026-11-23:

1. Fraens, *3D printed Braiding machine* — Hackaday.io project details:
   https://hackaday.io/project/191583-3d-printed-braiding-machine/details
2. Fraens, *3D printed braiding machine* — Cults listing (price,
   licence, file manifest):
   https://cults3d.com/en/3d-model/tool/3d-printed-braiding-machine-fraens-2
3. Hackaday, *3D Printed Machine Shows How Braiding Is Done* (2023):
   https://hackaday.com/2023/06/21/3d-printed-machine-shows-how-braiding-is-done/
4. kmatch98, *Braiding Machine — Maypole Braider and bobbins* —
   Hackaday.io project:
   https://hackaday.io/project/181960-braiding-machine-maypole-braider-and-bobbins
5. kmatch98, instructions (carrier, threading, take-up notes):
   https://hackaday.io/project/181960/instructions
6. Caitlyn B, *Maypole Machine (in work)* — Printables:
   https://www.printables.com/cs/model/345705-maypole-machine-in-work
7. Nico71, *Lego Braiding Machine (5 reels)*:
   https://www.nico71.fr/lego-braiding-machine/comment-page-1/
8. Hackaday, *Rope Braiding Machine Built Entirely From LEGO
   Technics* (2016):
   https://hackaday.com/2016/02/19/rope-braiding-machine-built-entirely-from-lego-technics/
9. *3D rotary tunnel braiding system with active control*, Int. J.
   Adv. Manuf. Technol. (2026):
   https://link.springer.com/article/10.1007/s00170-026-17696-4
10. *Investigation of Nonlinear Characteristics of a Gear
    Transmission System in a Braiding Machine* (2020):
    https://www.hindawi.com/journals/sv/2020/2747204/fig40/
11. Centexbel, *Circular Braiding: The Industrial Experience*:
    https://thread-etn.eu/circular-braiding-the-industrial-experience-with-centexbel/
12. US5257571A, *Maypole braider having a three under and three over
    braiding path*: https://patents.google.com/patent/US5257571A/en
13. US2788700A, *Braiding machine*:
    https://patents.google.com/patent/US2788700A/en
14. Herzog, *SE 1/32-432 rope braiding machine datasheet*:
    https://herzog-online.com/cms/wp-content/uploads/2023/05/Datasheet-SE-1-32-432-1.pdf
15. 3D Print World by Bob, *Maypole Braider Episode 1* (video series):
    https://www.facebook.com/reel/1030536373376366/
