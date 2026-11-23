# Xynthetix — Research Queue & Log

**Started:** 2026-11-23, at Joe's direction: research daily, add to this
repo daily. One substantive, sourced addition per day — a doc, a spec
extension, a simulator improvement with tests, or a worked example.
No filler, no personal information, everything here stays open source.

## How a daily run works

1. Check disk first: keep at least 55 GB free on the VM. Research is
   text/code only — no large downloads.
2. Take the next unchecked item in the rotation below (or the top of
   the backlog if the rotation item is blocked, and note why).
3. Research from primary sources where possible (papers, vendor docs,
   upstream repos, standards). Cite every factual claim with a URL.
4. Add ONE substantive file/change under `docs/`, `braid/`,
   `examples/`, or `tests/`. Update this log.
5. If code changed, run `python -m pytest tests/ -q` (or the stdlib
   test runner) and record the result in the log entry.
6. Commit locally with a clear message. Push to
   `github.com/Kaleaon/Xynthetix` via the GitHub PAT / Git Database API
   route documented for this workspace; if a push cannot land, say so
   in the log entry — never claim a push that did not verify.

## Weekly rotation

- **Mon — Braider hardware:** open / DIY maypole braider prior art,
  horn gears, track plates, carriers, tensioning, take-up control.
- **Tue — Design-to-braid pipeline:** braid geometry, `.braid` spec,
  braidpy and other upstream tools, TexMind-style modelling, carrier
  scheduling and take-up profiles.
- **Wed — Braided actuators:** McKibben / LT-PAM measured data,
  angle → force / contraction / cycle-life, replication notes.
- **Thu — Materials:** yarns and fibres for sleeves and tendons,
  friction, abrasion, elastic return, supplier specs.
- **Fri — Sensing in the braid:** conductive yarns, tactile / thermal
  sensing, wiring and readout for the sensor layer spec.
- **Sat — Landscape:** Allonic and other competitors (technical,
  public facts only), relevant standards and safety, open-source
  projects to learn from or interoperate with. No financial or
  partnership planning in this public repo.
- **Sun — Simulator & code:** extend the `braid/` simulator, add
  tests / examples, validate predictions against published data.

## Backlog (seeded 2026-11-23)

- [ ] Survey of documented DIY / open maypole braiders: carrier
      counts, track/horn-gear designs, BOMs, what is actually replicable.
- [ ] Braid angle geometry check: simulator predictions vs published
      maypole geometry relations, with worked numbers.
- [ ] LT-PAM (HardwareX 2026) replication data sheet: pressures,
      contraction, force, materials, cost — sourced.
- [ ] Yarn shortlist for first sleeves: PET, nylon, UHMWPE, aramid —
      friction / abrasion / elasticity comparison from datasheets.
- [ ] Conductive yarn options for tactile sensing: resistance per
      metre, wash / flex behaviour, sourcing.
- [ ] Allonic 3D Tissue Braiding: public technical claims inventory,
      dated and sourced, no speculation presented as fact.
- [ ] Carrier schedule output: can the simulator emit a machine-ready
      carrier / take-up schedule? Design note first, code second.
- [ ] Sensor layer: readout electronics options (voltage divider vs
      constant-current, multiplexing) costed from public listings.

## Log

- **2026-11-23 (Mon)** — Queue created; first run started:
  DIY / open maypole braider prior-art survey.
