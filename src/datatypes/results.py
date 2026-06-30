#!/usr/bin/env python3
"""
results.py

Defines the :class:`Results` dataclass, which stores the outcome
of processing calculations, including raw counts and derived scoring
metrics.
"""

from dataclasses import dataclass


@dataclass
class Results:
    """
    Hold the results of processing calculations.

    Aggregates the raw classification counts produced during
    evaluation along with the derived precision, recall, and F1
    scores computed from them.

    :ivar true_positive: The number of true positives.
    :vartype true_positive: int

    :ivar false_positive: The number of false positives.
    :vartype false_positive: int

    :ivar false_negative: The number of false negatives.
    :vartype false_positive: int

    :ivar precision: The final precision score.
    :vartype precision: float

    :ivar recall: The final recall score.
    :vartype recall: float

    :ivar f1: The final combined precision and recall score
        (F1 score).
    :vartype f1: float
    """

    true_positive: int = 0
    false_positive: int = 0
    false_negative: int = 0

    precision: float = 0.0
    recall: float = 0.0
    f1: float = 0.0
