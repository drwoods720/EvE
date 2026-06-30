#!/usr/bin/env python3
"""
cell.py

Defines the :class:`Cell` dataclass, which represents a single
segmented cell region extracted from a segmentation mask.
"""

from dataclasses import dataclass, field
from .point import Point


@dataclass
class Cell:
    """
    Represent a single cell region within a segmentation mask.

    A :class:`Cell` groups all :class:`~.point.Point` instances
    that fall within its boundary, along with metadata describing
    the cell's identity and whether it lies on the edge of the
    sampled area.

    :ivar id: The cell's identifier. Corresponds to the integer label
        assigned to this cell in the segmentation mask.
    :vartype id: int

    :ivar points: The points located within the cell's area.
        Defaults to an empty list if none are provided.
    :vartype points: list[Point]

    :ivar clipping: Whether the cell is clipped (cut off) by the
        border of the sample area. Defaults to ``False``.
    :vartype clipping: bool
    """

    id: int
    points: list[Point] = field(default_factory=list)
    clipping: bool = False
