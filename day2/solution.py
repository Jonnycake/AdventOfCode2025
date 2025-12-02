#!/usr/bin/env python3
import sys

from typing import Generator


def get_numbers(input_file: str) -> Generator[int, None, None]:
    with open(input_file, 'r') as f:
        for line in f:
            line = line.strip()
            ranges = line.split(",")
            for r in ranges:
                start, end = r.strip().split('-')
                for i in range(int(start), int(end) + 1):
                    yield i

def is_invalid(number_str: str, part_length: int):
    if part_length == 0:
        return False

    if len(number_str) % part_length != 0:
        return False

    num_parts = len(number_str) // part_length

    return number_str == number_str[:part_length] * num_parts

def part1(input_file: str) -> int:
    solution: int = 0

    for number in get_numbers(input_file):
        number_str = str(number)

        if len(number_str) % 2 != 0:
            continue

        if is_invalid(number_str, len(number_str) // 2):
            solution += number

    return solution

def part2(input_file: str) -> int:
    solution: int = 0

    for number in get_numbers(input_file):
        number_str = str(number)

        for part_length in range(1, len(number_str) // 2 + 1):
            if is_invalid(number_str, part_length):
                solution += number
                break

    return solution


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print(f'Syntax: {sys.argv[0]} <input-file>')
        sys.exit(1)

    print(f'Part 1: {part1(sys.argv[1])}')
    print(f'Part 2: {part2(sys.argv[1])}')
