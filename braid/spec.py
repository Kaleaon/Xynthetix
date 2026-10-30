"""Loader and validator for .braid specification files (spec v0).

The loader is deliberately strict: unknown fields and out-of-range values
are errors, not warnings. Two implementations that accept the same file
must compute the same braid.
"""

from __future__ import annotations

import json
from dataclasses import dataclass, field
from pathlib import Path


class SpecError(ValueError):
    """Raised when a .braid file is missing, malformed, or out of range."""


_TOP_LEVEL = {"spec_version", "name", "carriers", "yarn", "core", "target", "machine"}


@dataclass(frozen=True)
class Yarn:
    material: str
    width_mm: float
    linear_density_tex: float | None = None
    modulus_gpa: float | None = None


@dataclass(frozen=True)
class Core:
    diameter_mm: float


@dataclass(frozen=True)
class Target:
    braid_angle_deg: float
    length_mm: float


@dataclass(frozen=True)
class Machine:
    carrier_rpm: float | None = None
    takeup_mm_per_min: float | None = None


@dataclass(frozen=True)
class BraidSpec:
    name: str
    carriers: int
    yarn: Yarn
    core: Core
    target: Target
    machine: Machine = field(default_factory=Machine)
    spec_version: int = 0


def _require(obj: dict, key: str, where: str):
    if key not in obj:
        raise SpecError(f"{where}: missing required field '{key}'")
    return obj[key]


def _positive(value, where: str) -> float:
    if not isinstance(value, (int, float)) or isinstance(value, bool) or value <= 0:
        raise SpecError(f"{where}: must be a positive number, got {value!r}")
    return float(value)


def _section(data: dict, key: str, required: bool = True) -> dict:
    value = data.get(key)
    if value is None:
        if required:
            raise SpecError(f"missing required section '{key}'")
        return {}
    if not isinstance(value, dict):
        raise SpecError(f"'{key}' must be an object")
    return value


def spec_from_dict(data: dict) -> BraidSpec:
    if not isinstance(data, dict):
        raise SpecError("spec must be a JSON object")

    unknown = set(data) - _TOP_LEVEL
    if unknown:
        raise SpecError(f"unknown top-level field(s): {sorted(unknown)}")

    version = _require(data, "spec_version", "spec")
    if version != 0:
        raise SpecError(f"unsupported spec_version {version!r}; this loader implements 0")

    name = _require(data, "name", "spec")
    if not isinstance(name, str) or not name.strip():
        raise SpecError("'name' must be a non-empty string")

    carriers = _require(data, "carriers", "spec")
    if not isinstance(carriers, int) or isinstance(carriers, bool):
        raise SpecError("'carriers' must be an integer")
    if carriers < 4 or carriers % 2 != 0:
        raise SpecError("'carriers' must be an even integer >= 4 (half run each way)")

    yarn_d = _section(data, "yarn")
    yarn = Yarn(
        material=str(_require(yarn_d, "material", "yarn")),
        width_mm=_positive(_require(yarn_d, "width_mm", "yarn"), "yarn.width_mm"),
        linear_density_tex=(
            _positive(yarn_d["linear_density_tex"], "yarn.linear_density_tex")
            if "linear_density_tex" in yarn_d
            else None
        ),
        modulus_gpa=(
            _positive(yarn_d["modulus_gpa"], "yarn.modulus_gpa")
            if "modulus_gpa" in yarn_d
            else None
        ),
    )

    core_d = _section(data, "core")
    core = Core(diameter_mm=_positive(_require(core_d, "diameter_mm", "core"), "core.diameter_mm"))

    target_d = _section(data, "target")
    angle = _positive(_require(target_d, "braid_angle_deg", "target"), "target.braid_angle_deg")
    if not (5.0 < angle < 85.0):
        raise SpecError(
            f"target.braid_angle_deg {angle} outside (5, 85); the v0 geometry model "
            "is not meaningful outside that range"
        )
    target = Target(
        braid_angle_deg=angle,
        length_mm=_positive(_require(target_d, "length_mm", "target"), "target.length_mm"),
    )

    machine_d = _section(data, "machine", required=False)
    machine = Machine(
        carrier_rpm=(
            _positive(machine_d["carrier_rpm"], "machine.carrier_rpm")
            if "carrier_rpm" in machine_d
            else None
        ),
        takeup_mm_per_min=(
            _positive(machine_d["takeup_mm_per_min"], "machine.takeup_mm_per_min")
            if "takeup_mm_per_min" in machine_d
            else None
        ),
    )

    return BraidSpec(
        name=name,
        carriers=carriers,
        yarn=yarn,
        core=core,
        target=target,
        machine=machine,
        spec_version=0,
    )


def load_spec(path: str | Path) -> BraidSpec:
    path = Path(path)
    try:
        raw = path.read_text(encoding="utf-8")
    except OSError as exc:
        raise SpecError(f"cannot read {path}: {exc}") from exc
    try:
        data = json.loads(raw)
    except json.JSONDecodeError as exc:
        raise SpecError(f"{path}: invalid JSON: {exc}") from exc
    return spec_from_dict(data)
