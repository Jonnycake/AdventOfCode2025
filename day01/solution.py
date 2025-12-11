#!/usr/bin/env python3
import sys
from typing import Generator

# Quick summary of the problem:
#  - Finding password to secret safe
#  - Input contains series of rotations (L for left, R for right)
#  - Password is number of times it hits 0 (after a rotation)
#  - Dial has 0 - 99 and starts at 50
#
# Part 2:
#  - We need to count the number of times we hit or pass 0
#  - Note: A single rotation may pass 0 multiple times

def get_rotations(input_file) -> Generator[int, None, None]:
    with open(input_file) as f:
        for line in f:
            if not line.strip():
                continue

            assert line[0] in ['L', 'R'], "Multiplier should be either left or right"

            # Return negatives for left, positives for right
            multiplier = -1 if line[0] == 'L' else 1

            yield int(line[1:]) * multiplier

def solution_part1(input_file: str) -> int|None:
    dial: int = 50 # dial starts at 50
    solution: int = 0

    for rotation in get_rotations(input_file):
        # If we add 100 and then mod it, we automatically handle left turns
        dial += rotation + 100
        dial %= 100

        if dial == 0:
            solution += 1

    return solution

def solution_part2(input_file: str) -> int|None:
    dial: int = 50 # dial starts at 50
    solution: int = 0

    for rotation in get_rotations(input_file):
        step = rotation // abs(rotation)
        total_rotations = rotation // step

        # Brute force...
        # Rotate single clicks, and then check for 0
        for _ in range(total_rotations):
            dial += step + 100
            dial %= 100

            if dial == 0:
                solution += 1

    return solution

def main():
    if len(sys.argv) < 2:
        print(f'Syntax: {sys.argv[0]} <input-file>')
        sys.exit(1)

    print(f'Part 1: {solution_part1(sys.argv[1])}')
    print(f'Part 2: {solution_part2(sys.argv[1])}')

if __name__ == '__main__':
    main()
