#!/usr/bin/env python3
#
# Summary:
# - Ray starts below the S
# - Ray splits in 2 anytime it hits a ^
# - Solution = how many times it split
#
# Part 2:
# - Only a single particle goes through
# - Time splits any time it hits a splitter
# - Solution = how many active timelines there are

import sys
import os
from typing import Generator


def get_positions(input_file: str) -> tuple[tuple[int, int], set[tuple[int, int]], int]:
    start = (0, 0)
    splitters: set[tuple[int, int]] = set()
    max_splitter_depth: int = -1

    with open(input_file, 'r') as f:
        for y, line in enumerate(f):
            for x, char in enumerate(line):
                if char == 'S':
                    start = (x, y)
                elif char == '^':
                    splitters.add((x, y))

                    if y > max_splitter_depth:
                        max_splitter_depth = y

    return start, splitters, max_splitter_depth

def solution_part1(input_file: str) -> int:
    solution: int = 0

    start, splitters, max_splitter_depth = get_positions(input_file)

    max_y: int = -1
    rays = set([
        (start[0], start[1] + 1),
    ])

    while max_y < max_splitter_depth and len(rays):
        new_rays = set([])
        for ray in rays:
            x, y = ray
            y += 1

            if (x,y) in splitters:
                new_rays.add((x - 1, y))
                new_rays.add((x + 1, y))
                solution += 1
            else:
                new_rays.add((x, y))

            if y > max_y:
                max_y = y

        rays = new_rays

    return solution

def solution_part2(input_file: str) -> int:
    solution: int = 0

    return solution

def main():
    if len(sys.argv) < 2:
        print(f'Syntax: {sys.argv[0]} <input-file>')
        sys.exit(1)

    print(f'Part 1: {solution_part1(sys.argv[1])}')
    print(f'Part 2: {solution_part2(sys.argv[1])}')

if __name__ == '__main__':
    main()
