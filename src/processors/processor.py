#!/usr/bin/env python3

from abc import ABC, abstractmethod

import src.datatypes as dt


class Process(ABC):
    @abstractmethod
    def run(self, data: dt.Sample) -> dt.Sample: ...
