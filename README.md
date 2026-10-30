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
