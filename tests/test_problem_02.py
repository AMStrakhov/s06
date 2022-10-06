from inspect import isgeneratorfunction
from typing import List, Tuple
from unittest import TestCase

from problem_02 import moving_average


class TestProblem02(TestCase):
    _cases: List[Tuple[int, List[float]]] = [
        (1, [0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 1.0, 2.0, -3.0, -2.0]),
        (3, [0.0, 0.5, 1.0, 2.0, 3.0, 4.0, 5.0, 4.0, 3.0, 0.0, -1.0]),
        (5, [0.0, 0.5, 1.0, 1.5, 2.0, 3.0, 4.0, 3.8, 3.6, 2.2, 0.8]),
    ]

    def test_moving_average(self) -> None:
        for n, expected in self._cases:
            with self.subTest(n):
                self.assertListEqual(expected, list(moving_average(n)))

    def test_is_generator(self) -> None:
        self.assertTrue(isgeneratorfunction(moving_average))
