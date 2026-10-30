# Xynthetix — Company Roadmap (Public)

**Status:** v1.0 — 2026-10-30
**Scope:** What Xynthetix is building, in what order, and why. This is the
public roadmap. Engineering detail lives in the linked specs; financial and
partnership planning is not published here.

## What we are

Xynthetix is an open-source robotics company working on braided synthetic
tissue: machines, software, and materials that weave structure, tendons,
sensing, and elastic return into a single continuous braid over a skeletal
core — instead of assembling a robot from bearings, screws, and cables and
then dressing it up as a body.

Everything we publish is open source and stays open source: hardware under
open hardware licences, software under permissive licences. That is not a
marketing position. The gap we are filling exists *because* the one
well-funded effort in this space (Allonic's proprietary 3D Tissue Braiding
platform) is closed: no published machine, no design software, no prices,
nothing an independent lab can build on. An open counterpart — a braider a
makerspace can build, a design tool anyone can run, and measured data anyone
can check — is the product.

## The wedge

Three linked gaps, verified against the public record in October 2026:

1. **No open-source maypole braiding machine** exists as a maintained,
   documented, replicable design. DIY builds exist as fragments (STL dumps,
   one-off project pages) with no BOM standard, firmware, or control model.
2. **No open design-to-braid pipeline.** Commercial tools (e.g. TexMind)
   model braid *geometry* for composites. Nothing open takes a design —
   carrier count, yarn, core geometry, braid angle — and produces both a
   physical prediction and a machine-ready carrier schedule / take-up
   profile.
3. **No open measured dataset for braided actuators.** Braided (McKibben)
   muscles are usually built with off-the-shelf sleeves of whatever angle
   the supplier stocks. The angle → stiffness / force / contraction map for
   sleeves braided *to spec* is not published anywhere we can find.

## Roadmap

### Phase 0 — Design-to-braid pipeline (digital twin)
An open braid specification (`.braid`, see `docs/braid-spec.md`), a
simulator that predicts braid angle, diameter, cover factor, yarn
consumption, and first-order stiffness from machine and material inputs,
and worked examples validated against physical hand-braided samples.

*Exit criterion:* the simulator predicts braid angle and diameter within
~10% on three physical samples. Hardware spend waits for this.

### Phase 1 — Desktop maypole braider
A makerspace-buildable braider, forked from the best-documented open DIY
architecture rather than designed from a blank page: printed carriers and
horn gears, a laser-cut track plate, stepper-driven take-up with
closed-loop speed control (take-up speed *is* braid-angle control),
documented per-carrier tension, an emergency stop, and a centre-tube feed
so braid can be laid directly over a skeletal core. Full CAD, BOM, and
firmware published so a second builder can replicate it unaided.

*Exit criterion:* one metre of repeatable braid over a 3D-printed finger
skeleton, with angle variance measured and published.

### Phase 2 — Braided actuator and tendon demos
- **Braided tendon conduit:** tendon sheaths braided directly over a
  printed hand/arm core, benchmarked for friction and cycle life against
  stock cable guides on a low-cost open robot arm.
- **Tuned McKibben muscles:** the published open-source low-cost McKibben
  recipe (LT-PAM, HardwareX 2026) replicated, then re-run with our own
  sleeves braided at 30° / 45° / 55°, logging contraction, force, and
  cycles-to-failure per angle. That dataset is a deliverable in itself.

*Month-12 target — the v1 open release:* (1) the design tool, (2) braider
CAD + build guide, (3) two demos with measured data, (4) a ROS 2 driver.

### Beyond year 1
Braided sleeves and actuator kits for labs and educators; sensing integrated
into the braid (see `docs/sensor-layer-spec.md` and
`docs/braided-mesh-integration.md`); and, on the far side of reliable
locomotion, full synthetic bodies. Bodies are the destination. The machine
and the pipeline are the company until the machine and the pipeline are
boring.

## Principles

- **Open by default.** If it is in this repo, it is published on purpose.
- **Measure, then claim.** Every performance number we publish ships with
  the test that produced it.
- **Simulate before spending.** Each phase has a written exit criterion;
  the next phase's budget unlocks when the current one passes.
- **Safety is a property of the physics.** Soft, back-drivable, braided
  actuation is safer around people than geared rigidity — we intend to
  prove that with data, not assert it.
