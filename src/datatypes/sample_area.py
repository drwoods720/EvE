#!/usr/bin/env python3
"""
sample_area.py

Defines the :class:`SampleArea` dataclass, which represents the
rectangular bounds of the original sample area.
"""

from dataclasses import dataclass


@dataclass
class SampleArea:
    """
    Represent the bounds of the original sample area.

    Defines the rectangular region of the sample, used to determine
    which cells and points fall within bounds.

    :ivar xmax: The maximum x value inside the sample area.
    :vartype xmax: int

    :ivar xmin: The minimum x value inside the sample area.
    :vartype xmin: int

    :ivar ymax: The maximum y value inside the sample area.
    :vartype ymax: int

    :ivar ymin: The minimum y value inside the sample area.
    :vartype ymin: int
    """

    xmax: int
    xmin: int

    ymax: int
    ymin: int
