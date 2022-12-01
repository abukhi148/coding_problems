from aocd.models import Puzzle
from aocd import submit
from itertools import combinations
import math

puzzle = Puzzle(year=2020, day=1)
nums = list(map(int, puzzle.input_data.splitlines()))


def part_a(nums):
   for c in combinations(nums, 2):
        if sum(c) == 2020:
            return math.prod(c)


def part_b(nums):
    for c in combinations(nums, 3):
        if sum(c) == 2020:
            return math.prod(c)


submit(part_b(nums), year=2020, day=1)
