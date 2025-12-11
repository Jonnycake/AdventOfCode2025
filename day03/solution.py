#!/usr/bin/env python3
#
# Quick Summary:
# - The input is a series of power banks
# - Each number in the bank represents joltage of battery
# - Goal is to find highest number with 2 batteries from bank
#   - Left most battery = 10s place
#   - Right most battery = 1s place
# - Solution is sum of all bank max joltage
# - Note: You must have 2 numbers directly from bank (i.e. can't use last digit for left most)
#
# Part 2:
# - Use 12 digits instead of 2

from collections.abc import Generator
import sys

def get_banks(input_file) -> Generator[list[int], None, None]:
    with open(input_file, 'r') as f:
        for line in f:
            yield [
                int(v)
                for v in line.strip()
            ]

def find_max_joltage(bank: list[int], num_batteries: int) -> int | None:
    if len(bank) < num_batteries:
        return None

    max_joltage: int = 0

    # We need to reserve  batteries to the right so we only look at the starting
    #  slice of the list
    numbers_left: int = num_batteries
    window_left: int = 0
    window_right: int = len(bank) - numbers_left + 1
    window = bank[window_left:window_right]

    while numbers_left > 0:
        window_max_idx = 0
        window_max_joltage = 0

        for idx, joltage in enumerate(window):
            if joltage > window_max_joltage:
                window_max_joltage = joltage
                window_max_idx = idx

        window_left += window_max_idx + 1

        numbers_left -= 1
        max_joltage += window_max_joltage * 10**numbers_left

        window_right: int = len(bank) - numbers_left + 1
        window = bank[window_left:window_right]

    return max_joltage
def solution_part1(input_file: str) -> int:
    solution: int =  0

    for bank in get_banks(input_file):
        solution += find_max_joltage(
            bank,
            num_batteries=2
        ) or 0

    return solution

def solution_part2(input_file: str) -> int:
    solution: int = 0

    for bank in get_banks(input_file):
        solution += find_max_joltage(
            bank,
            num_batteries=12
        ) or 0

    return solution

def main():
    if len(sys.argv) < 2:
        print(f'Syntax: {sys.argv[0]} <input-file>')
        sys.exit(1)

    print(f'Part 1: {solution_part1(sys.argv[1])}')
    print(f'Part 2: {solution_part2(sys.argv[1])}')

if __name__ == '__main__':
    main()
