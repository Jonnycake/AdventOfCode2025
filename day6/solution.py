#!/usr/bin/env python3
#
# Summary:
# - Input is a worksheet of problems in columns
# - Last row in each column is the operation to perform
# - Part 1 Output = sum of the result of all columns

import sys
import os
from typing import Generator


def get_operations(input_file: str) -> list[str]:
    ops = []
    with open(input_file, 'rb') as f:
        # We can find the length of each line using the first line
        first_line = f.readline()
        line_length = len(first_line)

        f.seek(-line_length, os.SEEK_END)

        ops = [v for v in filter(lambda v: v, f.readline().decode().strip('\n').split())]

    return ops


def get_numbers(input_file: str) -> Generator[list[int], None, None]:
    with open(input_file, 'r') as f:
        for line in f:
            try:
                yield [int(v) for v in filter(lambda v: v, line.split())]
            except ValueError:
                # We're at the end of the file
                return

def solution_part1(input_file: str) -> int:
    ops = get_operations(input_file)
    solution_parts: list[int] = []

    for num_list in get_numbers(input_file):
        if not solution_parts:
            solution_parts = num_list
            continue


        for i, num in enumerate(num_list):
            if ops[i] == '+':
                solution_parts[i] += num
            elif ops[i] == '*':
                solution_parts[i] *= num
            else:
                raise ValueError(f'An unexpected operation was requested: {ops[i]}')

    return sum(solution_parts)

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
