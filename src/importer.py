#!/usr/bin/env python3

from pathlib import Path

import src.datatypes as dt
import src.parsers as parsers

def import_samples(root_dir: str) -> None:
    root_path:Path = Path(root_dir)

    mask_filenames: list[Path] = list(root_path.rglob("*tif"))
    annotation_filenames: list[Path] = list(root_path.rglob("*.geojson"))

    for annotation_filename in annotation_filenames:
        filepath: str = str(annotation_filename.absolute())

        image_name: str = annotation_filename.name.split(".ome.tif")[0]

        try:
            sample_area: dt.SampleArea = parsers.sampleArea.Geojson(
                2
            ).parse(str(filepath))
        except ValueError as e:
            print(f"Error: {e} for file {filepath}")
            continue

        print(annotation_filename.name)
        for mask_filename in list(filter(lambda filename: filename.name.startswith(image_name), mask_filenames)):
            print(f"\t{mask_filename.name}")

        print()
