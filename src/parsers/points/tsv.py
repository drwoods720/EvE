#!/usr/bin/env python3
"""
tsv.py

Defines the :class:`Tsv`, which reads a TSV file and
parses it into a list of :class:`~.datatypes.Point` objects.
"""

from typing import override

import pandas as pd

import src.datatypes as dt
from src.parsers.parser import Parser


class Tsv(Parser[list[dt.Point]]):
    """
    Parse point objects from a TSV file.

    Reads a TSV file containing manually placed point coordinates
    and builds a :class:`~.datatypes.Point` object for each row.
    """

    @override
    def parse(self, filepath: str) -> list[dt.Point]:
        """
        Generate point objects from a TSV file.

        Reads the TSV file at ``filepath`` and builds a
        :class:`~.datatypes.Point` object for each row it contains.

        :param filepath: The path to the TSV file to parse.
        :type filepath: str

        :returns: A list of point objects parsed from the file.
        :rtype: list[~.datatypes.Point]
        """

        points: list[dt.Point] = []

        dataframe: pd.DataFrame = pd.read_csv(filepath, sep="\t")

        for _, data in dataframe.iterrows():
            point_x: int = int(data["x"])
            point_y: int = int(data["y"])

            point = dt.Point(point_x, point_y)

            points.append(point)

        return points
