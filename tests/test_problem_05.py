from typing import List, Tuple
from unittest import TestCase

from problem_05 import slice_file


class TestProblem05(TestCase):
    _cases: List[Tuple[Tuple[int, int], List[str]]] = [
        ((1, 3), ["OK", "OK", "OK", "OK", "OK"]),
        ((1, 6), ["OK", "OK", "OK"]),
        ((12, 1), ["12", "OK", "14"]),
        ((50, 1), []),
    ]

    def test_slice_file(self) -> None:
        for args, expected in self._cases:
            with self.subTest(args):
                self.assertListEqual(expected, slice_file(*args))
