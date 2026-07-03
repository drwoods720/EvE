#!/usr/bin/env python3
"""
output.py

Defines the :class:`Output` abstract class, which establishes
the interface that all output generators must implement to turn
processed sample data into a finished output artifact, such as a
CSV report or a visualization, and write it to disk.
"""

from abc import ABC, abstractmethod
from pathlib import Path

import src.datatypes as dt


class Output(ABC):
    """
    Abstract base class for output generators.

    Subclasses of :class:`Output` are responsible for
    generating the resulting output artifact from processed data.
    Each concrete subclass must implement :meth:`run`.
    """

    @abstractmethod
    def run(self, data: dt.Sample, output_directory: Path) -> None: ...
