"""Reference braid geometry simulator (v0).

Implements the derived quantities defined in docs/braid-spec.md.
This is an ideal-helix geometry model: it assumes a circular core,
inextensible yarns, no inter-yarn friction, and no yarn flattening.
Read the Limitations section of the spec before trusting a number.
"""

from __future__ import annotations

import math
from dataclasses import dataclass

from .spec import BraidSpec


@dataclass(frozen=True)
class BraidResult:
    name: str
    braid_angle_deg: float          # as-built angle (machine-derived if possible, else target)
    angle_source: str               # "machine" or "target"
    cover_factor: float             # 0..1 fraction of core surface covered
    per_direction_cover: float      # 0..1 coverage of one yarn system
    yarn_per_metre_per_carrier_m: float  # metres of yarn consumed per metre of braid, per carrier
    total_yarn_m: float             # total yarn consumed for the finished length, all carriers
    picks_per_mm: float             # yarn crossovers per mm of braid length
    braid_mass_g: float | None      # None unless yarn tex was given
    axial_stiffness_index: float    # normalised cos^4 index, 0..1 — comparison only, NOT a modulus

    def summary(self) -> str:
        mass = f"{self.braid_mass_g:.1f} g" if self.braid_mass_g is not None else "n/a (no tex)"
        return (
            f"{self.name}\n"
            f"  braid angle (deg, from {self.angle_source}): {self.braid_angle_deg:.1f}\n"
            f"  cover factor: {self.cover_factor:.3f} "
            f"(per-direction {self.per_direction_cover:.3f})\n"
            f"  yarn use: {self.yarn_per_metre_per_carrier_m:.3f} m per metre per carrier; "
            f"{self.total_yarn_m:.1f} m total\n"
            f"  picks per mm: {self.picks_per_mm:.3f}\n"
            f"  finished braid mass: {mass}\n"
            f"  axial stiffness index (cos^4, comparison only): {self.axial_stiffness_index:.3f}"
        )


def angle_from_machine(carrier_rpm: float, takeup_mm_per_min: float, core_diameter_mm: float) -> float:
    """Braid angle (deg from axis) determined by machine speeds.

    tan(theta) = circumferential surface speed at the core / take-up speed,
    with surface speed = carrier rpm * pi * core diameter (mm/min).
    """
    surface_speed = carrier_rpm * math.pi * core_diameter_mm
    return math.degrees(math.atan2(surface_speed, takeup_mm_per_min))


def cover_factor(carriers: int, yarn_width_mm: float, core_diameter_mm: float, angle_deg: float) -> tuple[float, float]:
    """(total, per-direction) cover factor under the ideal-helix model.

    On the unwrapped cylinder, adjacent parallel yarns of one system are
    offset by pi*D/(N/2) circumferentially; their perpendicular spacing is
    that offset * cos(theta). Per-direction coverage f = yarn width /
    perpendicular spacing, capped at 1. Two systems overlap independently:
    K = 1 - (1 - f)^2.
    """
    theta = math.radians(angle_deg)
    per_system = carriers // 2
    spacing = (math.pi * core_diameter_mm / per_system) * math.cos(theta)
    f = min(1.0, yarn_width_mm / spacing)
    return 1.0 - (1.0 - f) ** 2, f


def simulate(spec: BraidSpec) -> BraidResult:
    machine = spec.machine
    if machine.carrier_rpm is not None and machine.takeup_mm_per_min is not None:
        angle = angle_from_machine(machine.carrier_rpm, machine.takeup_mm_per_min, spec.core.diameter_mm)
        angle_source = "machine"
    else:
        angle = spec.target.braid_angle_deg
        angle_source = "target"

    theta = math.radians(angle)
    total_cover, per_dir = cover_factor(spec.carriers, spec.yarn.width_mm, spec.core.diameter_mm, angle)

    yarn_per_metre = 1.0 / math.cos(theta)
    length_m = spec.target.length_mm / 1000.0
    total_yarn_m = yarn_per_metre * length_m * spec.carriers

    # Crossovers: each carrier crosses the opposite system once per
    # circumferential pass; picks scale with tan(theta) / (pi * D).
    picks_per_mm = (spec.carriers / 2) * math.tan(theta) / (math.pi * spec.core.diameter_mm)

    mass_g = None
    if spec.yarn.linear_density_tex is not None:
        # tex = grams per 1000 m of yarn
        mass_g = total_yarn_m * spec.yarn.linear_density_tex / 1000.0

    return BraidResult(
        name=spec.name,
        braid_angle_deg=angle,
        angle_source=angle_source,
        cover_factor=total_cover,
        per_direction_cover=per_dir,
        yarn_per_metre_per_carrier_m=yarn_per_metre,
        total_yarn_m=total_yarn_m,
        picks_per_mm=picks_per_mm,
        braid_mass_g=mass_g,
        axial_stiffness_index=math.cos(theta) ** 4,
    )


def mckibben_geometry(yarn_length_mm: float, turns: float, angle_deg: float) -> tuple[float, float]:
    """(length_mm, diameter_mm) of an ideal braided (McKibben) sleeve.

    Standard inextensible-yarn model: with yarn length b wound in n turns,
    L = b * cos(theta) and D = b * sin(theta) / (n * pi). Contraction of a
    muscle pressurised from rest angle theta0 to theta is
    1 - cos(theta)/cos(theta0). Friction and bladder elasticity are ignored.
    """
    theta = math.radians(angle_deg)
    length = yarn_length_mm * math.cos(theta)
    diameter = yarn_length_mm * math.sin(theta) / (turns * math.pi)
    return length, diameter
