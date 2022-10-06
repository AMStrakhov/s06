"""
Description:

Write a function that accepts a list of tuples. Each tuple has two strings:
group and name. The function should return a dictionary, where keys are groups
and values are lists with names in alphabetical order.

Examples:
Input:
[("M212", "Alex"), ("M212", "Nikita"), ("M213", "Den"), ("M213", "Max"), ("M212", "Peter"), ("M213", "Darina")]

Return:
{"M212": ["Alex", "Nikita", "Peter"], "M213": ["Darina", "Den", "Max"]}

"""
from typing import Dict, List, Tuple


def group_students(unsorted: List[Tuple[str, str]]) -> Dict[str, List[str]]:
    """Write your solution here:"""
    ...


if __name__ == "__main__":
    values = [
        ("M212", "Alex"),
        ("M212", "Nikita"),
        ("M213", "Den"),
        ("M213", "Max"),
        ("M212", "Peter"),
        ("M213", "Darina"),
    ]
    print(group_students(values))
