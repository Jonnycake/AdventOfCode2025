#!/usr/bin/env python3
#
# Summary:
# - Input is a worksheet of problems in columns
# - Last row in each column is the operation to perform
# - Part 1 Output = sum of the result of all columns
#
# Part 2:
# - The numbers are read as columns
# - Top row is most significant digit of equation
# - Bottom row is least significant digit of equation
# Example:
# --------
#   24
#   15
#    3
#   *
#  ^----- means 453 * 21

import sys
import os
from typing import Generator


def get_operations(input_file: str) -> list[str]:
    ops = []

    # Open in binary mode so we can seek from the end
    with open(input_file, 'rb') as f:
        # We can find the length of each line using the first line
        first_line = f.readline()
        line_length = len(first_line)

        f.seek(-line_length, os.SEEK_END)

        ops = [v for v in filter(lambda v: v, f.readline().decode().strip('\n').split())]

    return ops


# Generates numbers by row
def get_numbers(input_file: str) -> Generator[list[int], None, None]:
    with open(input_file, 'r') as f:
        for line in f:
            try:
                yield [int(v) for v in filter(lambda v: v, line.split())]
            except ValueError:
                # We're at the end of the file
                return

# Generate the numbers by column intead
def get_numbers_by_column(input_file: str) -> Generator[list[int], None, None]:
    file_size = os.path.getsize(input_file)
    with open(input_file, 'r') as f:
        # We can determine how far to skip for each column by getting line length
        line_length = len(f.readline())
        num_digits = (file_size // line_length) - 1

        col = 0
        while col < line_length:
            found_digits = True
            digits = []
            while found_digits:
                digits.append(0)
                digit_col = len(digits) - 1
                found_digits = False
                for digit_line in range(num_digits):
                    f.seek(line_length * digit_line + col)
                    digit = f.read(1)

                    if digit not in [' ', '\n']:
                        digits[digit_col] = digits[digit_col] * 10 + int(digit.strip())
                        found_digits = True

                col += 1

            # Get rid of final digit (0)
            digits.pop()

            yield digits

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
    ops = get_operations(input_file)
    solution: int = 0

    for i, num_list in enumerate(get_numbers_by_column(input_file)):
        solution_part: int|None = None
        for num in num_list:
            if solution_part is None:
                solution_part = num
                continue

            if ops[i] == '+':
                solution_part += num
            elif ops[i] == '*':
                solution_part *= num
            else:
                raise ValueError(f'An unexpected operation was requested: {ops[i]}')


        if solution_part is None:
            continue

        solution += int(solution_part)

    return solution

def main():
    if len(sys.argv) < 2:
        print(f'Syntax: {sys.argv[0]} <input-file>')
        sys.exit(1)

    print(f'Part 1: {solution_part1(sys.argv[1])}')
    print(f'Part 2: {solution_part2(sys.argv[1])}')

if __name__ == '__main__':
    main()
