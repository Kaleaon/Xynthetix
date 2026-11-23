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
- [Body plan research map](docs/body-plan-research-map.md) —
  subsystem decomposition, open questions, first experiments, and
  scaling for complete synthetic bodies
- [Power & thermal budget](docs/power-thermal-budget.md) — heating a
  warm body, battery/runtime arithmetic, and cooling a soft insulated
  body, with a worked reference-body budget
- [Maypole braider prior art](docs/maypole-braider-prior-art.md) —
  survey of documented DIY / open braiding machines and the gaps
  Phase 1 fills
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
