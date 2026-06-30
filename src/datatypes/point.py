#!/usr/bin/env python3
"""
point.py

Defines the :class:`Point` dataclass, which represents a single
manually placed point and its associated cell membership.
"""

from dataclasses import dataclass


@dataclass
class Point:
    """
    Represent a single manually placed point.

    A :class:`Point` records a coordinate location along with a
    reference to the cell region it falls within, if any.

    :ivar x: The x coordinate of the point.
    :vartype x: int

    :ivar y: The y coordinate of the point.
    :vartype y: int

    :ivar cell: The ID of the :class:`~.cell.Cell` the point
        is located in. A value of ``0`` indicates the point does not
        fall within any cell region.
    :vartype cell: int
    """

    x: int
    y: int
    cell: int = 0
