import os
from pathlib import Path
from unittest import TestCase

from problem_01 import convert_file


class TestProblem01(TestCase):
    test_fp_out: Path = (
        Path(__file__).resolve().parent.parent
        / "assets"
        / "problem_01_test_output.txt"
    )
    test_assets_path: Path = Path(__file__).resolve().parent / "assets"

    def test_convert_file(self) -> None:
        for n in (0, 10, -66):
            with self.subTest(n):
                convert_file(n, filepath_output=self.test_fp_out)
                self._compare_files(n)

    def _compare_files(self, n: int) -> None:
        expected_fp = self.test_assets_path / f"problem_01_expected_{n}.txt"
        with open(expected_fp) as expected, open(self.test_fp_out) as actual:
            for exp, act in zip(expected, actual):
                self.assertEqual(exp, act)

    @classmethod
    def tearDownClass(cls) -> None:
        os.remove(cls.test_fp_out)
