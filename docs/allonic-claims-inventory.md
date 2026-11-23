# Allonic — Public Technical Claims Inventory

**Status:** v1.0 — compiled 2026-11-23
**Scope:** What Allonic publicly *claims* about its 3D Tissue Braiding
platform, inventoried claim by claim, with sources. This is a claims
inventory, not a validation: nothing here has been independently
measured by us, and — as the notes below document — almost none of it
has been published with test data by anyone.

**Why this exists:** Allonic is the one well-funded effort in braided
synthetic tissue, and it is closed: no published machine design, no
design software, no prices (see `docs/company-roadmap.md`). The
benchmark an open counterpart has to meet is therefore, today, a set
of *claims*. This file pins those claims down — dated and sourced —
so they can be checked against later publications and against our own
measured results.

## How to read this

- Every entry gives the claim (Allonic's words, or a close paraphrase
  marked as such), the source, the source's date where shown, and the
  access date (2026-11-23 for all entries).
- Sections (a)–(c) are claims Allonic itself makes: on its own site,
  in its own award submissions, in interviews with its CEO, or in the
  funding-announcement release text that multiple outlets reproduced
  in near-identical form in February 2026.
- Section (d) is things said *about* Allonic by third parties that
  Allonic itself does not claim, including several widely repeated
  amplifications that the primary record does not support.
- Where a claim carries no numbers, that is stated. A separate
  "numbers audit" after section (c) collects every quantitative
  claim found — and lists the measurements that are absent.

## Sources read for this inventory

Allonic's own site (homepage and prototype page), Allonic's Formnext
Awards 2025 finalist submission (published by the organiser, Mesago),
a CEO interview (Pulse 2.0), the funding coverage Allonic links to
from its own homepage (Sifted), further funding coverage (Tech.eu,
EU-Startups, Robotics 24/7, ASSEMBLY, Robotics & Automation News),
an investor's public memo (Day One Capital), product/startup
directories (Humanoid Guide, RobotToday, Industrial Atlas, Deeplist,
DEPLOY registry), an event report (Startup Hungary), a Hungarian
Intellectual Property Office story, and commentary (Mike Kalil's
blog). Full URLs are given per claim below.

---

## (a) Claims about the machine / platform

**A1. One continuous, fully automated production process.**
"We weave structural fibers, tendons, joints, and other load-bearing
tissues directly over a skeletal core so we can manufacture robotic
bodies in a single, automated process" — instead of "assembling
hundreds of parts." (CEO Benedek Tasi.)
- Source: Pulse 2.0 interview, https://pulse2.com/allonic-profile-benedek-tasi-interview/
- Source date: 2026-09-01. Accessed: 2026-11-23.

**A2. Three-step process: scaffold, braid, connect actuators.**
Allonic's site describes the process as producing a skeletal
scaffold, braiding soft tissues around it, and connecting actuators,
with pulleys, guides, and tendons integrated and routed during
production rather than assembled afterwards. (Paraphrase of the
site, as summarised by RobotToday's profile, which is drawn from it.)
Tasi's version of the endpoint: "What you get out from the machinery
is basically a finished product that you will need to wire up to the
actuators." (Sifted.)
- Sources: https://robottoday.com/suppliers-discovery/allonic (no
  date shown; accessed 2026-11-23);
  https://sifted.eu/articles/openai-hugging-face-hungary-biggest-ever-pre-seed
  (February 2026; accessed 2026-11-23).

**A3. Design-to-production-code software, "similar to slicing in
3D printing."**
Users configure high-level robotic designs and the platform
translates them automatically into production code. This comparison
appears in the February 2026 release text and is repeated in nearly
every outlet's coverage. No software name, file format, screenshot,
or documentation has been published with the claim.
- Sources: https://www.robotics247.com/article/allonic-raises-7.2m-to-build-a-foundation-for-advanced-robotic-hardware
  (2026-02-12; accessed 2026-11-23);
  https://www.assemblymag.com/articles/99852-allonic-raises-72m-for-automated-platform-to-build-advanced-robot-parts
  (2026-02-25; accessed 2026-11-23).

**A4. "Minutes instead of weeks."**
"Being able to go from idea to physical robot in minutes instead of
weeks fundamentally changes how we can think about robotics design."
(Tasi.) In Sifted's more specific version, producing "a finger or
manipulator or an arm" should take "a couple of minutes," production
itself included — "a magnitude of difference" versus hours or days.
No timed build, part size, or start/stop definition is published
with either version.
- Sources: https://www.eu-startups.com/2026/02/with-openai-backing-allonic-raises-e6-million-for-robotic-body-manufacturing-platform/
  (2026-02-10; accessed 2026-11-23);
  https://sifted.eu/articles/openai-hugging-face-hungary-biggest-ever-pre-seed
  (February 2026; accessed 2026-11-23).

**A5. Second-generation machinery: 5× faster, half the size, 3× the
yarn-count resolution.**
Allonic's website states its second-generation machinery is five
times faster and half the size of the first generation, with three
times the yarn-count resolution (as reported by RobotToday from the
site). At a February 2026 fireside chat the team gave the same
figures in weaker form: "5× faster and 3× more detailed" (Startup
Hungary's event report). No absolute values — no build rate, machine
footprint, or yarn count for either generation — have been
published; all three figures are relative to an unspecified
baseline.
- Sources: https://robottoday.com/suppliers-discovery/allonic
  (accessed 2026-11-23);
  https://www.startuphungary.io/past-events/first-monday-with-allonic
  (event 2026-02-09; accessed 2026-11-23).

**A6. Order-of-magnitude cost reduction; design to prototype in
hours.**
Allonic's own Formnext Awards submission (Start-up Award finalist,
2025) promises that with a Tissue Braider "you will: reduce the
production cost of robotic bodies by an order of magnitude" and
"get from a design idea to a complex mechanical prototype in a
matter of hours instead of weeks." Note the tension with A4: the
award submission says *hours* to a prototype; the February 2026
interviews say *minutes* to a finished part. No costed example —
no part, price, or comparison build — accompanies either figure.
- Source: Formnext Awards page, Mesago,
  https://formnext.mesago.com/frankfurt/en/expo/program/award/award.html
  (Formnext 2025, 18–21 November 2025; accessed 2026-11-23).

**A7. Uniqueness: "the only company in the world" doing this.**
The February 2026 release text states: "Allonic is the only company
in the world automating the production of robotics in this way."
Tasi's interview version: "Nobody is automating robotics
manufacturing in this way." No survey or comparison is offered in
support.
- Sources: https://roboticsandautomationnews.com/2026/02/12/allonic-raises-7-2-million-to-build-foundation-for-advanced-robotic-hardware/98908/
  (2026-02-12; accessed 2026-11-23);
  https://pulse2.com/allonic-profile-benedek-tasi-interview/
  (2026-09-01; accessed 2026-11-23).

**A8. "No need for assembly — just connect your actuators and
deploy."**
Allonic's Formnext submission describes "machinery that 'grows'
fibrous, durable functional tissues directly on a few
pre-manufactured parts, and outputs a fully functional robotic
body. No need for assembly – just connect your actuators and
deploy." Directory copy drawn from Allonic's site (Industrial
Atlas) states the same endpoint as: fully functional robotic bodies
"in a single automated process at any scale and complexity, with no
assembly required beyond wiring," and that Allonic "designs and
builds the machinery, the software that drives it and the robot
bodies themselves."
- Sources: https://formnext.mesago.com/frankfurt/en/expo/program/award/award.html
  (2025; accessed 2026-11-23);
  https://www.indatlas.com/startups/allonic/ (accessed 2026-11-23).

**A9. Technology unveiled May 2025; first industrial pilot
completed.**
Allonic states it first unveiled 3D Tissue Braiding in May 2025 and
has since completed a first pilot project in electronics
manufacturing. The pilot customer is not named in any source read;
Tasi says the pilot "demonstrated that rapid, on-demand production
of robotic end effectors significantly reduces downtime and
increases operational flexibility" — an outcome claim with no
published figures.
- Source: https://pulse2.com/allonic-profile-benedek-tasi-interview/
  (2026-09-01; accessed 2026-11-23); corroborated in all February
  2026 funding coverage cited above.

**A10. Business model: platform first as a service, machines later.**
Per Tasi (Sifted), Allonic currently sees itself as an
infrastructure player: customers use its platform to design custom
robot bodies, which Allonic then delivers; longer term it is
"thinking of a business model where it sells the full platform to
customers to use in house." No machine price, part price, lead
time, or service terms have been published.
- Source: https://sifted.eu/articles/openai-hugging-face-hungary-biggest-ever-pre-seed
  (February 2026; accessed 2026-11-23).

---

## (b) Claims about materials / tissue properties

**B1. Strength from structure, not rigid material — the rope
principle.**
The process is "inspired by how ropes achieve strength through
structure rather than rigid parts" (release text, repeated by
Tech.eu and others). Day One Capital's memo repeats the analogy as
Allonic's design principle. No fibre property is derived from the
analogy anywhere in the public material.
- Sources: https://tech.eu/2026/02/10/openai-and-hugging-face-angels-back-highest-ever-hungarian-pre-seed-funding-round/
  (2026-02-10; accessed 2026-11-23);
  https://dayonecapital.substack.com/p/why-we-invested-in-allonic
  (2026-02-10; accessed 2026-11-23).

**B2. Hundreds of fine fibres anchored into a few bone-like
elements.**
"A robotic finger, for example, can be built from a small number of
bone-like elements, held together by hundreds of fine fibres that
wrap around and anchor into the structure itself, similar to
connective tissue in the human body." (Release text.) "Hundreds" is
the only fibre-count figure published; no total yarn count, fibre
material, or anchoring test is given.
- Source: https://www.eu-startups.com/2026/02/with-openai-backing-allonic-raises-e6-million-for-robotic-body-manufacturing-platform/
  (2026-02-10; accessed 2026-11-23).

**B3. Multiple materials integrated in a single structure.**
"Multiple materials can be integrated into a single structure,
enabling elastics, wiring and sensing elements to be embedded
directly into robotic bodies during production." (Release text;
Tasi's feature list says the same: "Integration of multiple
materials, including elastics, wiring, and sensing elements, in one
build.") The materials are named only by category — no polymer,
fibre, conductor, or sensor type is specified in any source read,
and no embedded-sensor demonstration with data has been published.
- Sources: https://www.eu-startups.com/2026/02/with-openai-backing-allonic-raises-e6-million-for-robotic-body-manufacturing-platform/
  (2026-02-10; accessed 2026-11-23);
  https://pulse2.com/allonic-profile-benedek-tasi-interview/
  (2026-09-01; accessed 2026-11-23).

**B4. Strong, compliant, safe — with no published measurements.**
The release text's result claim: "robotic bodies that are strong,
compliant, naturally safe, and dramatically simpler to
manufacture," with "fewer failure points" (because fixtures and
many traditional failure points are removed). Allonic's homepage
states the property version: "Naturally load-bearing and
impact-resistant, with compliance and control tuned for the task."
No tensile strength, stiffness, compliance range, impact test, or
failure-rate figure accompanies any of these claims in any source
read.
- Sources: https://roboticsandautomationnews.com/2026/02/12/allonic-raises-7-2-million-to-build-foundation-for-advanced-robotic-hardware/98908/
  (2026-02-12; accessed 2026-11-23);
  https://allonic.co/ (no date shown; accessed 2026-11-23).

**B5. "Hands that don't break. The smallest component is the bone."**
Allonic's homepage headline claim for its hands: "No tiny hinges,
bearings, or fragile mechanisms. The smallest component is the
bone." Its reliability framing on the same page: "Don't bother with
repairs, just swap as needed. At a fraction of the cost." No
breakage, cycle-life, or swap-cost data is published with these
claims.
- Source: https://allonic.co/ (no date shown; accessed 2026-11-23).

**B6. What is *not* claimed anywhere in the public record.**
Across all sources read for this inventory, Allonic has published
no: fibre or yarn material identification; braid angle or pattern
specification; tensile / stiffness / fatigue data for any braided
part; cycle-life testing; load or grip-force measurement for its
hand; or environmental / wash / abrasion behaviour. Every materials
claim in the public record is qualitative except the relative
"3× yarn-count resolution" machine figure in A5.

---

## (c) Claims about robots / bodies built with it

**C1. The first braided hand: 16 actuators, 32 actuated degrees of
freedom.**
Allonic's own prototype page describes "our first braided hand" as:
"Fully biomimetic, for naturally human-like dexterity";
tendon-driven — "Lightweight, and remotely actuated"; "Synergistic
— mechanical intelligence embodied"; and, in full: "16 actuators.
32 actuated degrees of freedom. Life-sized, sleek, and completely
wireless." These are the only performance-adjacent numbers Allonic
itself publishes for any robot it has built. No weight, grip force,
payload, range-of-motion, or repeatability figure appears on the
page.
- Source: https://allonic.co/prototype (no date shown; accessed
  2026-11-23).

**C2. Current focus: manipulators. Whole body is a hope, not a
product.**
Tasi (Sifted): the company is "starting by focusing on manipulators
— hands, grippers, various end-effectors — and hopes to move into
arms and 'maybe expand to the whole body' as its tech develops";
it is "not just focusing on humanoids, but a wide range of form
factors." Allonic's Formnext submission names the target subsystems
as "moving mechanical structures such as fingers, arms, and legs."
Allonic's homepage tagline for the hand is: "Our hands are just
the beginning" (as reported by RobotToday). No arm, leg, torso, or
full body built by the platform has been shown or specified in any
source read.
- Sources: https://sifted.eu/articles/openai-hugging-face-hungary-biggest-ever-pre-seed
  (February 2026; accessed 2026-11-23);
  https://formnext.mesago.com/frankfurt/en/expo/program/award/award.html
  (2025; accessed 2026-11-23);
  https://robottoday.com/suppliers-discovery/allonic (accessed
  2026-11-23).

**C3. End effectors "swapped as easily as disposable gloves."**
Release text: at Allonic's production speed and costs, "robotic end
effectors can be swapped as easily as disposable gloves, making
customised hardware economically viable for the first time," and
manipulators "designed, produced and replaced on demand" reduce
downtime and eliminate "lengthy maintenance cycles." Day One
Capital's memo repeats the glove line. No swap time, interface
standard, or cost per swap is published.
- Sources: https://www.eu-startups.com/2026/02/with-openai-backing-allonic-raises-e6-million-for-robotic-body-manufacturing-platform/
  (2026-02-10; accessed 2026-11-23);
  https://dayonecapital.substack.com/p/why-we-invested-in-allonic
  (2026-02-10; accessed 2026-11-23).

**C4. Demand claims: pilot done, inbound interest, no named
customers.**
Allonic states it has completed its first pilot in electronics
manufacturing (A9) and is "seeing inbound interest from humanoid
robotics companies and several large U.S.-based technology players"
(Pulse 2.0; similar wording in all February 2026 coverage). Tasi
explicitly declines to name customers: "we're still early in
commercialization and can't share customer names yet." The DEPLOY
registry, which tracks independently sourced deployment evidence,
records no verified deployment and no verified price for the
platform, and classifies it as research-stage.
- Sources: https://pulse2.com/allonic-profile-benedek-tasi-interview/
  (2026-09-01; accessed 2026-11-23);
  https://registry.deploy.report/models/tissue-braiding-platform
  (last reviewed 2026-10-10; accessed 2026-11-23).

---

## Numbers audit — every quantitative claim found

| Claim | Value | Source |
|---|---|---|
| Idea → physical robot | "minutes instead of weeks" | Tasi, Feb 2026 (A4) |
| Produce a finger / manipulator / arm | "a couple of minutes" | Tasi via Sifted (A4) |
| Design → complex prototype | "hours instead of weeks" | Formnext submission (A6) |
| Production cost of robotic bodies | reduced "by an order of magnitude" | Formnext submission (A6) |
| Conventional build cost replaced | "weeks and thousands of dollars" → minutes | Release text, Feb 2026 |
| Gen-2 machine speed | 5× gen 1 | Allonic site via RobotToday (A5) |
| Gen-2 machine size | ½ gen 1 ("2× smaller") | Allonic site via RobotToday (A5) |
| Gen-2 yarn-count resolution | 3× gen 1 | Allonic site via RobotToday (A5) |
| Fibres per finger | "hundreds of fine fibres" | Release text (B2) |
| Parts replaced | "hundreds of individual parts" | Release text (A1) |
| Hand actuation | 16 actuators, 32 actuated DOF | Allonic prototype page (C1) |

**Absent from the public record:** machine price; part price;
build envelope; absolute yarn/carrier counts; build time for a
named part with defined start/stop; any mechanical test result
(strength, stiffness, fatigue, grip force, payload); repeatability
or yield figures; pilot metrics. Every number above is either a
ratio against an unpublished baseline, a round magnitude ("hundreds",
"order of magnitude"), or a configuration count (actuators, DOF).

## Patents — negative finding

Allonic's own materials read for this inventory describe the process
as "proprietary"; none claims a patent. Searches of public patent
sources (Google Patents, WIPO PatentScope, and general web search)
by company name and by the founders' names, performed 2026-11-23,
located **no publicly readable patent application or grant naming
Allonic or its founders**. This is not proof that no filing exists —
applications are typically published ~18 months after filing, and
national filings may not be indexed under the names searched — but
as of the access date there is no patent document a reader can
inspect to learn how the platform works. (The Hungarian Intellectual
Property Office's Allonic story likewise cites no patent number for
the company: https://sztnh.gov.hu/en/home/hipo-130?tab=1, accessed
2026-11-23.)

---

## (d) Said about Allonic — not claimed by Allonic

**D1. "Backed by OpenAI."**
Headline framing in EU-Startups ("With OpenAI backing, Allonic
raises €6 million…") and much social coverage presents OpenAI as a
backer. The underlying fact, stated consistently in the funding
reports themselves, is narrower: *individual angel investors from*
OpenAI and Hugging Face (plus ETH Zurich and Northwestern
University) participated personally. Tasi's own wording is "more
than a dozen angel investors from U.S. and European technology
companies." No source read reports an investment by OpenAI or
Hugging Face as companies.
- Sources: https://www.eu-startups.com/2026/02/with-openai-backing-allonic-raises-e6-million-for-robotic-body-manufacturing-platform/
  (2026-02-10; accessed 2026-11-23);
  https://tech.eu/2026/02/10/openai-and-hugging-face-angels-back-highest-ever-hungarian-pre-seed-funding-round/
  (2026-02-10; accessed 2026-11-23).

**D2. Meta and NASA as investors.**
Social-media news posts about the round (e.g. Rowan Cheung's
Threads/TikTok posts, March 2026) add Meta and NASA to the investor
list. Neither organisation appears in any funding report, investor
list, or Allonic statement read for this inventory.
- Source: https://www.threads.com/@rowancheung/post/DV_ekAijCMX
  (2026-03-17; accessed via search record 2026-11-23).

**D3. "Patented technique."**
The same social coverage describes 3D Tissue Braiding as Allonic's
"patented technique." Allonic's own materials say "proprietary,"
and no patent document was located (see Patents, above). The
patent claim currently rests on social posts, not on any filing a
reader can check.
- Source: https://www.threads.com/@rowancheung/post/DV_ekAijCMX
  (2026-03-17; accessed via search record 2026-11-23).

**D4. "The ASML of robotics."**
"We envision a future where Allonic becomes the true ASML of
robotics" is Day One Capital's investment thesis about its own
portfolio company — an investor's aspiration, not an Allonic claim
and not a market fact.
- Source: https://dayonecapital.substack.com/p/why-we-invested-in-allonic
  (2026-02-10; accessed 2026-11-23).

**D5. Westworld comparisons.**
Framing Allonic as real-life *Westworld* host fabrication is
commentary, not company language — e.g. Mike Kalil's essay "When
Real-World Tech Catches Up to Westworld," which itself attributes
to Allonic only the narrower claims inventoried above.
- Source: https://mikekalil.com/blog/westworld-irl/ (accessed
  2026-11-23).

**D6. Hand MK2 specification table (3 kg strength, 0.45 kg weight,
15 DOF).**
Humanoid Guide's product listing for an "Allonic Hand MK2" gives
specifications — strength 3 kg, weight 0.45 kg, 15 degrees of
freedom, no tactile/force sensors, availability "prototype." These
figures are directory data, not Allonic publications: RobotToday
explicitly notes that "no official degree-of-freedom count, weight
or payload figures have been published," and the 15 DOF figure
conflicts with the 32 actuated DOF on Allonic's own prototype page
(C1). The "MK2" name itself appears in directories; Allonic's own
page calls its hand "our first braided hand."
- Sources: https://humanoid.guide/product/allonic-hand-mk2/
  (accessed 2026-11-23);
  https://robottoday.com/suppliers-discovery/allonic (accessed
  2026-11-23).

**D7. "No weak points," "uniform stress distribution."**
Deeplist's profile asserts the approach "delivers high load-bearing
strength, uniform stress distribution, and no weak points at
junctions or material interfaces." Allonic's published wording
claims fewer failure points (B4); the absolute "no weak points"
formulation is the directory's, and no test data supports either
version in the public record.
- Source: https://deeplist.tech/allonic (accessed 2026-11-23).

**D8. Founding-year disagreement.**
Directories disagree about when Allonic was founded: 2021
(EU-Startups, PitchBook) versus 2025 (several later profiles).
Nothing read on Allonic's own site states a founding year. The
disagreement is noted here because secondary sources repeat both
dates as fact.
- Sources: https://www.eu-startups.com/2026/02/with-openai-backing-allonic-raises-e6-million-for-robotic-body-manufacturing-platform/
  (2026-02-10; accessed 2026-11-23);
  https://deeplist.tech/allonic (accessed 2026-11-23).

---

## What an open counterpart must measure and publish to be comparable

Allonic's public record is claims without data. An open platform
does not beat that by making bigger claims; it beats it by
publishing the measurements Allonic has not. Concretely, to be
comparable — claim by claim — an open counterpart needs:

1. **Machine specification, absolute not relative.** Carrier count,
   yarn capacity per carrier, build envelope, take-up range and
   resolution, machine footprint and cost — the absolutes behind
   A5's ratios, plus full CAD, BOM, and firmware so the machine
   itself can be replicated and its numbers checked.
2. **The design-to-braid pipeline, inspectable.** The `.braid`-style
   design file, the generated carrier schedule / take-up profile,
   and the simulator's prediction for each build, published next to
   the physical result — the open equivalent of A3's "slicing"
   claim, with the code available to run.
3. **Timed builds with defined start/stop.** Wall-clock time from
   design file to finished part for named reference parts (a finger,
   a hand), including scaffold production and actuator connection —
   the measurement A4's "minutes instead of weeks" and A6's "hours"
   currently lack.
4. **Costed builds.** Per-part cost (materials, machine time,
   labour) for the same reference parts, against a costed
   conventional-assembly comparison — the measurement behind
   "order of magnitude" (A6) and "a fraction of the cost" (B5, C3).
5. **Mechanical data for braided tissue.** Tensile strength and
   stiffness as a function of braid angle, yarn, and cover factor;
   fatigue / cycles-to-failure per configuration; failure modes
   photographed and described. This is the dataset B1–B4 gesture at
   and no one has published.
6. **Hand benchmarks.** Degrees of freedom with range of motion per
   joint, grip force, payload, tendon force, repeatability, and
   cycle life for a complete braided hand — the numbers missing
   from C1, published for a build others can replicate.
7. **Embedded-function evidence.** For any claim of embedded wiring
   or sensing (B3): what was embedded, its measured performance
   (continuity, sensor accuracy, drift after N cycles), and how it
   fails.
8. **Pilot/deployment evidence with metrics.** Named application,
   task, uptime, swap/replacement events and times — the substance
   behind A9/C4's pilot and downtime claims.
9. **Second-builder replication.** At least one build of the machine
   and one reference part by someone outside the originating team,
   from the published files alone. A claim of "no assembly required"
   (A8) means little until a stranger has assembled nothing and
   succeeded.

Until items 1–6 exist for Allonic's platform in public, the honest
summary of its record is: a plausible process, demonstrated hands,
one completed pilot — and performance claims that are, as of
2026-11-23, entirely unaccompanied by published measurement.

---

*Compiled for the Xynthetix research queue (landscape workstream),
2026-11-23. Update policy: add new claims as dated addenda; do not
silently edit earlier entries — Allonic's claims changing over time
is itself data.*
