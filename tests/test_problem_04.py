from typing import Dict, List, Tuple
from unittest import TestCase

from problem_04 import group_students


class TestProblem04(TestCase):
    _cases: List[Tuple[List, Dict, str]] = [
        (
            [("a", "A"), ("a", "B"), ("b", "A"), ("b", "B")],
            {"a": ["A", "B"], "b": ["A", "B"]},
            "Base case",
        ),
        (
            [("a", "B"), ("a", "A"), ("b", "B"), ("b", "A")],
            {"a": ["A", "B"], "b": ["A", "B"]},
            "Unsorted names",
        ),
        (
            [("a", "A"), ("b", "B"), ("b", "A"), ("a", "B")],
            {"a": ["A", "B"], "b": ["A", "B"]},
            "Unsorted groups",
        ),
        (
            [("a", "A"), ("a", "B")],
            {"a": ["A", "B"]},
            "One group",
        ),
    ]

    def test_count_words(self) -> None:
        for unsorted, expected, msg in self._cases:
            with self.subTest(msg):
                self.assertDictEqual(expected, group_students(unsorted))
