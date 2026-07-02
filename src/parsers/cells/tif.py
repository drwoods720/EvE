#!/usr/bin/env python3
"""
tif.py

Defines the :class:`Tif`, which reads a labeled TIFF
segmentation mask and parses it into a dictionary of
:class:`~.datatypes.Cell` objects.
"""

from typing import override

import skimage as ski
import numpy as np
import numpy.typing as npt
from PIL import Image

import src.datatypes as dt
from src.parsers.parser import Parser


class Tif(Parser[dict[int, dt.Cell]]):
    """
    Parse cell objects from a labeled TIFF mask.

    Reads a labeled segmentation mask from a TIFF file, where each
    distinct label value corosponds to a single cell region, and
    builds a :class:`~.datatypes.Cell` object for each one.
    """

    @override
    def parse(self, filepath: str) -> dict[int, dt.Cell]:
        """
        Generate cell objects from a labeled mask file.

        Reads a labeled TIFF mask at ``filepath`` and builds a
        :class:`~.datatypes.Cell` object for each distinct label
        found in the mask, keyed by its cell ID.

        :param filepath: The path to the TIFF file to parse.
        :type filepath: str

        :returns: A dictionary mapping each cell ID to its
            corresponding :class:`~.datatypes.Cell` object.
        :rtype: dict[int, ~.datatypes.Cell]
        """

        mask_image: npt.NDArray[np.uint16] = np.array(
            Image.open(filepath), dtype="uint16"
        )

        cell_regions = ski.measure.regionprops(mask_image)

        cells: dict[int, dt.Cell] = {}
        for region in cell_regions:
            cells[region.label] = dt.Cell(region.label)

        return cells
