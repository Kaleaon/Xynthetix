# Xynthetix

Open-source engineering for synthetic bodies.

Xynthetix is the open hardware and software arm of Xynthetix LLC. We design
and build the machines, simulations, and tooling for braided synthetic tissue,
soft robotics, and everything on the road to real bodies.

Everything in this repository is open source and stays open source.

## Projects

- **Braiding machines** — maypole braider designs and an accurate braiding
  simulator, working toward Allonic-style 3D tissue braiding for synthetic
  soft tissue. (In progress.)
- **`.braid` spec + simulator** — an open design-to-braid file format and
  its reference simulator (`braid/`), with worked examples (`examples/`)
  and tests (`tests/`). Spec: [docs/braid-spec.md](docs/braid-spec.md).
  Run it: `python -m braid examples/tube-sleeve.braid.json`
- **Roadmap** — the public company roadmap and phase exit criteria:
  [docs/company-roadmap.md](docs/company-roadmap.md).

## Docs

- [Company roadmap](docs/company-roadmap.md)
- [Artificial muscle landscape](docs/artificial-muscle-landscape.md) —
  sourced survey of DEA, McKibben, TCP, HASEL, SMA and motor/SEA
  actuation for full synthetic bodies, incl. the large-joint problem
- [DEA deep dive](docs/dea-deep-dive.md) — dielectric elastomer
  actuators in depth: geometries, materials, HV drive, lifetime, and
  the honest large-joint gap
- [Sensing & proprioception survey](docs/sensing-proprioception-survey.md) —
  tactile skins, textile/braided sensing, muscle self-sensing, and
  gaps found in our own sensor layer spec
- [Conductive yarn options for tactile sensing](docs/conductive-yarn-tactile-sensing.md) —
  silver-coated nylon vs stainless thread vs PEDOT:PSS yarns: resistance
  per metre, gauge factor and drift, wash behaviour (bleach kills silver),
  and a buying order for first tactile experiments
- [Body plan research map](docs/body-plan-research-map.md) —
  subsystem decomposition, open questions, first experiments, and
  scaling for complete synthetic bodies
- [Skeleton materials comparison](docs/skeleton-materials-comparison.md) —
  printed polymers, carbon tube, aluminium, steel, titanium —
  stiffness/weight/cost/repairability with a worked femur example:
  metals tie on specific stiffness, carbon is 3.4× lighter, printed
  polymer cannot be a human-scale femur
- [Power & thermal budget](docs/power-thermal-budget.md) — heating a
  warm body, battery/runtime arithmetic, and cooling a soft insulated
  body, with a worked reference-body budget
- [Skin systems survey](docs/skin-systems-survey.md) — cast silicone
  vs 3D-printed elastomers, fur/hair attachment, and thickness vs
  tactile transparency, with a worked skin mass budget and the
  sensitivity-vs-thickness experiment still to run
- [Maypole braider prior art](docs/maypole-braider-prior-art.md) —
  survey of documented DIY / open braiding machines and the gaps
  Phase 1 fills
- [Allonic claims inventory](docs/allonic-claims-inventory.md) —
  every public technical claim by the closed 3D Tissue Braiding
  platform, dated and sourced, with a numbers audit
- [Open-source humanoid / body projects inventory](docs/open-source-humanoid-inventory.md) —
  25 open humanoid, hand, and simulation/control projects with
  licences read from their own files, activity status, what transfers
  to Xynthetix, and the closed platforms labelled as closed
- [Braid geometry validation](docs/braid-geometry-validation.md) —
  simulator predictions checked against published maypole geometry
  relations, with worked numbers and flagged corrections
- [Yarn shortlist for first sleeves](docs/yarn-shortlist-first-sleeves.md) —
  PET, nylon 6,6, UHMWPE, aramid and Vectran compared from datasheets
  for braided sleeves and tendons, with worked break forces, a buying
  order, and the handling traps for each fibre
- [`.braid` specification v0](docs/braid-spec.md)
- [braidpy evaluation](docs/braidpy-evaluation.md) — prior art for
  horn-gear machine modelling, and our adoption decision
- [Braided mesh integration](docs/braided-mesh-integration.md) — tendons,
  tactile sensing, embedded systems
- [Sensor layer spec](docs/sensor-layer-spec.md) — low-voltage tactile +
  thermal sensing

## License

MIT. See [LICENSE](LICENSE).

## Contributing

Issues and pull requests are welcome. Keep it open, keep it kind.
