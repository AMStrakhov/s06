from unittest import TestCase

from problem_03 import count_words


class TestProblem03(TestCase):
    def test_count_words(self) -> None:
        expected = {"et": 11, "ut": 6, "aut": 6, "qui": 6, "est": 5}
        self.assertDictEqual(expected, count_words())
