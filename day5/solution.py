#!/usr/bin/env python3
# Core idea:
# - Input file contains list of ingredient ranges
# - Input file also contains list of single ingrediets
# - Ingredients separated from ranges by newline
# - Part 1 output = how many are fresh (ingredients within ranges)
# - Part 2 output = how many total ingredient ids are fresh (ignore actual ingredients)

from collections.abc import Generator
import sys

def get_ranges(input_file: str) -> list[tuple[int, int]]:
    ranges: list[tuple[int, int]] = []

    with open(input_file, 'r') as f:
        for line in f:
            if not line.strip():
                break

            start, end = line.strip().split('-')
            ranges.append((int(start), int(end)))

    # Sort and merge them off-the-bat
    merged_ranges: list[tuple[int, int]] = []
    ranges = sorted(ranges, key=lambda v: v[0])

    max_end = 0
    for i, ingredient_range in enumerate(ranges):
        start, end = ingredient_range
        if max_end >= end:
            continue

        j = i + 1
        while j < len(ranges) and (end + 1) >= ranges[j][0]:
            end = max(ranges[j][1], end)
            j = j+1


        max_end = end
        merged_ranges.append((start, end))

    return merged_ranges

def get_ingredients(input_file: str) -> Generator[int, None, None]:
    at_ingredients = False
    with open(input_file, 'r') as f:
        for line in f:
            if not line.strip():
                at_ingredients = True
                continue

            if not at_ingredients:
                continue

            yield int(line.strip())

def solution_part1(input_file: str) -> int:
    ranges = get_ranges(input_file)

    fresh_ingredients: int = 0
    for ingredient in get_ingredients(input_file):
        for ingredient_range in ranges:
            if ingredient < ingredient_range[0]:
                break

            if ingredient <= ingredient_range[1]:
                fresh_ingredients += 1
                break

    return fresh_ingredients

def solution_part2(input_file: str) -> int:
    solution: int = 0
    for ingredient_range in get_ranges(input_file):
        solution += ingredient_range[1] - ingredient_range[0] + 1

    return solution

def main():
    if len(sys.argv) < 2:
        print(f'Syntax: {sys.argv[0]} <input-file>')
        sys.exit(1)

    print(f'Part 1: {solution_part1(sys.argv[1])}')
    print("\n\n\n")
    print(f'Part 2: {solution_part2(sys.argv[1])}')

if __name__ == '__main__':
    main()

