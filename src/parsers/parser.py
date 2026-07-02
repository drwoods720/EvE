#!/usr/bin/env python3
"""
parsers.py

Defines the :class:`Parser` abstract class, a generic interface
for parsing a file at a given path into some parsed result type.
"""

from abc import ABC, abstractmethod
from typing import Generic, TypeVar

R = TypeVar("R")  #: The type of the parsed result returned by :meth:`Parser.parse`.


class Parser(ABC, Generic[R]):
    """
    Abstract base class for file parsers.

    Generic over the return type :data:`R`, the type of the parsed
    result. Subclasses define how a file at a given path is read and
    parsed into an instance of :data:`R`. Each concrete subclass
    must implement :meth:`parse`.
    """

    @abstractmethod
    def parse(self, filepath: str) -> R:
        """
        Parse the file at the given path.

        :param filepath: The path to the file to parse.
        :type filepath: str

        :returns: The parsed result.
        :rtype: R
        """

        ...
