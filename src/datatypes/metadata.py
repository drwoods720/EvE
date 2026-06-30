#!/usr/bin/env python3
"""
metadata.py

Defines the :class:`Metadata` dataclass, which stores descriptive
information about a sample, including its source image, the model used
to segment it, associated file references, and the time it was imported.
"""

from dataclasses import dataclass
from pandas import Timestamp
import uuid


@dataclass
class Metadata:
    """
    Hold metadata describing a sample.

    Captures identifying information for a sample, including the
    original image, the segmentation model used, references to the
    associated ground truth and mask files, and a unique identifier
    with import timestamp.

    :ivar image_name: The filename of the sample image.
    :vartpye image_name: str

    :ivar model_name: The name of the model that generated
        the segmentation mask for this sample.
    :vartype model_name: str

    :ivar points_file: The name of the file containing the
        ground truth points for this sample.
    :vartype points_file: str

    :ivar mask_file: The name of the labeled segmentation mask file.
    :vartype mask_file: str

    :ivar uuid: A unique identifier assigned to this sample.
    :vartype uuid: str

    :ivar timestamp: The date and time this sample was imported
        into the program.
    :vartype timestamp: pandas.Timestamp
    """

    image_name: str = ""
    model_name: str = ""
    points_file: str = ""
    mask_file: str = ""
    uuid: str = str(uuid.uuid1())
    timestamp: Timestamp = Timestamp.now()
