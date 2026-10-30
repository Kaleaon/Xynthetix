"""Tests for the braid spec loader and geometry simulator (v0).

Run: python -m unittest discover -s tests -v   (from the repo root)
"""

import math
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from braid import SpecError, load_spec, mckibben_geometry, simulate
from braid.geometry import angle_from_machine, cover_factor
from braid.spec import spec_from_dict

EXAMPLES = Path(__file__).resolve().parent.parent / "examples"

BASE = {
    "spec_version": 0,
    "name": "test",
    "carriers": 16,
    "yarn": {"material": "PET", "width_mm": 1.0},
    "core": {"diameter_mm": 10.0},
    "target": {"braid_angle_deg": 45.0, "length_mm": 1000.0},
}


class TestLoader(unittest.TestCase):
    def test_examples_load(self):
        for path in sorted(EXAMPLES.glob("*.braid.json")):
            spec = load_spec(path)
            self.assertEqual(spec.spec_version, 0)

    def test_odd_carriers_rejected(self):
        bad = dict(BASE, carriers=15)
        with self.assertRaises(SpecError):
            spec_from_dict(bad)

    def test_unknown_field_rejected(self):
        bad = dict(BASE, bogus=1)
        with self.assertRaises(SpecError):
            spec_from_dict(bad)

    def test_wrong_version_rejected(self):
        bad = dict(BASE, spec_version=99)
        with self.assertRaises(SpecError):
            spec_from_dict(bad)

    def test_angle_out_of_range_rejected(self):
        bad = dict(BASE, target={"braid_angle_deg": 89.0, "length_mm": 10.0})
        with self.assertRaises(SpecError):
            spec_from_dict(bad)


class TestGeometry(unittest.TestCase):
    def test_machine_angle_45(self):
        # surface speed == takeup speed -> 45 degrees
        angle = angle_from_machine(carrier_rpm=10.0, takeup_mm_per_min=10.0 * math.pi * 10.0,
                                   core_diameter_mm=10.0)
        self.assertAlmostEqual(angle, 45.0, places=6)

    def test_machine_overrides_target(self):
        spec = spec_from_dict(dict(BASE, machine={"carrier_rpm": 12.0, "takeup_mm_per_min": 377.0}))
        result = simulate(spec)
        self.assertEqual(result.angle_source, "machine")
        self.assertAlmostEqual(result.braid_angle_deg, 45.0, delta=0.2)

    def test_yarn_consumption_at_45(self):
        result = simulate(spec_from_dict(BASE))
        self.assertAlmostEqual(result.yarn_per_metre_per_carrier_m, math.sqrt(2), places=6)

    def test_cover_factor_bounds_and_monotonic(self):
        k30, _ = cover_factor(16, 1.0, 10.0, 30.0)
        k60, _ = cover_factor(16, 1.0, 10.0, 60.0)
        for k in (k30, k60):
            self.assertGreaterEqual(k, 0.0)
            self.assertLessEqual(k, 1.0)
        # coverage rises with angle in the practical range (yarns pack axially)
        self.assertGreater(k60, k30)

    def test_cover_factor_full_at_wide_yarn(self):
        k, f = cover_factor(16, 50.0, 10.0, 45.0)
        self.assertEqual(f, 1.0)
        self.assertEqual(k, 1.0)

    def test_stiffness_index_falls_with_angle(self):
        low = simulate(spec_from_dict(dict(BASE, target={"braid_angle_deg": 25.0, "length_mm": 100.0})))
        high = simulate(spec_from_dict(dict(BASE, target={"braid_angle_deg": 65.0, "length_mm": 100.0})))
        self.assertGreater(low.axial_stiffness_index, high.axial_stiffness_index)

    def test_mass_uses_tex(self):
        spec = spec_from_dict(dict(BASE, yarn={"material": "PET", "width_mm": 1.0,
                                               "linear_density_tex": 100.0}))
        result = simulate(spec)
        expected = result.total_yarn_m * 100.0 / 1000.0
        self.assertAlmostEqual(result.braid_mass_g, expected)

    def test_mckibben_zero_force_angle(self):
        # Volume of the ideal sleeve peaks where dV/d(theta) = 0:
        # tan^2(theta) = 2, theta ~= 54.7356 deg — the classic result.
        b, n = 300.0, 3.0
        def volume(theta):
            length, diameter = mckibben_geometry(b, n, theta)
            return math.pi * (diameter / 2) ** 2 * length
        theta_star = math.degrees(math.atan(math.sqrt(2)))
        self.assertGreater(volume(theta_star), volume(theta_star - 10))
        self.assertGreater(volume(theta_star), volume(theta_star + 10))

    def test_mckibben_length_falls_as_angle_rises(self):
        # L = b cos(theta): as a muscle pressurises and its braid angle
        # rises toward the zero-force angle, its length contracts.
        length_50, _ = mckibben_geometry(300.0, 3.0, 50.0)
        length_30, _ = mckibben_geometry(300.0, 3.0, 30.0)
        self.assertLess(length_50, length_30)


if __name__ == "__main__":
    unittest.main()
