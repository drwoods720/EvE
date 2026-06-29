#!/usr/bin/env python3

import json
from typing import override, Any

import src.datatypes as dt
from src.parsers.parser import Parser

class Geojson(Parser[dt.SampleArea]):

    def parse_sample_area(self, json_data: list[Any]) -> dt.SampleArea:
        """
        Extracts the sample area data from geojson data.

        Parameters:
        json_data: The raw json data to parse.
        Returns: The sample area.
        """

        for annotation in json_data:
            try:
                if (
                        annotation["properties"]["classification"]["name"]
                        == "cell_segmentation_sample_area"
                ):
                    area_points = annotation["geometry"]["coordinates"][0]

                    padding: int = 2

                    tl = area_points[0]
                    br = area_points[2]
                    tr = area_points[3]

                    sample_area: dt.SampleArea = dt.SampleArea(
                        int(tr[0] - padding),
                        int(tl[0] + padding),
                        int(br[1] - padding),
                        int(tr[1] + padding),
                    )

                    return sample_area

            except KeyError:
                continue


    @override
    def parse(self, filepath: str) -> dt.SampleArea:
        """
        Read the sample area data from a geojson file.

        Parameters:
        filepath: Path to the geojson file.
        Returns: Sample area.
        """

        json_data: list[Any] = []
        with open(filepath, "r") as f:
            json_data = json.load(f)

        sample_area: dt.SampleArea = self.parse_sample_area(json_data)

        return sample_area
