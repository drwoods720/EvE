#!/usr/bin/env python3

from abc import ABC, abstractmethod
from pathlib import Path

import src.datatypes as dt


class Output(ABC):
    @abstractmethod
    def run(self, data: dt.Sample, output_directory: Path) -> None: ...
