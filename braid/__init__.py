"""Xynthetix braid package: .braid spec loading + reference simulator (v0).

Standard library only. See docs/braid-spec.md for the format and for the
model limitations that apply to every number this package produces.
"""

from .spec import BraidSpec, SpecError, load_spec
from .geometry import BraidResult, simulate, mckibben_geometry

__all__ = [
    "BraidSpec",
    "SpecError",
    "load_spec",
    "BraidResult",
    "simulate",
    "mckibben_geometry",
]

__version__ = "0.1.0"
