#!/usr/bin/env python3
"""
sample.py

Defines the :class:`Sample` dataclass, which bundles together all
the data required to process a single sample: its metadata, detected
cell regions, manually placed points, segmentation mask, sample area,
and resulting evaluation scores.
"""

import numpy as np
import numpy.typing as npt

from dataclasses import dataclass, field

from src.datatypes import Cell, Metadata, Point, Results, SampleArea


@dataclass
class Sample:
    """
    Contain all the data needed to process one sample.

    A :class:`Sample` ties together a sample's :class:`~.metadata.Metadata`,
    its detected :class:`~.cell.Cell` regions, the manually placed
    :class:`~.point.Point` instances used for ground truth comparison,
    the labeled segmentation mask to be assessed, the bounds of the
    sampled area, and the resulting evaluation :class:`~.results.Results`.

    :ivar metadata: Information describing the current sample.
    :vartype metadata: Metadata

    :ivar cells: A mapping of cell ID to the corresponding
        :class:`~.cell.Cell` region for every cell detected in the
        sample.
    :vartype cells: dict[int, Cell]

    :ivar points: The list of manually placed points within the
        sample.
    :vartype points: list[Point]

    :ivar mask: The labeled cell segmentation mask to assess, where
        each cell region is identified by its integer label.
    :vartype mask: numpy.typing.NDArray[numpy.uint16]

    :ivar sample_area: The area of the sample used to determine
        which cells and points are in bounds.
    :vartype sample_area: SampleArea

    :ivar original_image: The original image the mask was generated
        from. Optional; defaults to ``None`` if not available.
    :vartype original_image: numpy.typing.NDArray[numpy.uint16], optional

    :ivar results: The results of processing this sample, including
        true/false positive counts and precision, recall, and F1
        scores. Defaults to an empty :class:`~.results.Results`
        instance.
    :vartype results: Results
    """

    metadata: Metadata
    cells: dict[int, Cell]
    points: list[Point]
    mask: npt.NDArray[np.uint16]
    sample_area: SampleArea
    original_image: npt.NDArray[np.uint16] | None = None
    results: Results = field(default_factory=Results)

    # Sets the original_image value to an all black image the same shape as the mask if none is provided.
    def __post_init__(self) -> None:
        if self.original_image is None:
            self.original_image = np.zeros_like(self.mask)
