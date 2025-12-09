#!/usr/bin/env python3
#
# Summary
# - Input = series of points
# - Output = area of largest rectangle you can make

from collections.abc import Iterable
import sys

def get_points(input_file: str) -> Iterable[tuple[int, int]]:
    with open(input_file, 'r') as f:
        for line in f:
            x, y = line.strip().split(",")
            yield (int(x), int(y))

def calc_rect_size(corner1: tuple[int, int], corner2: tuple[int, int]) -> int:
    top_left = (
        min(corner1[0], corner2[0]),
        min(corner1[1], corner2[1]),
    )

    bottom_right = (
        max(corner1[0], corner2[0]),
        max(corner1[1], corner2[1]),
    )

    width = bottom_right[0] - top_left[0] + 1
    height = bottom_right[1] - top_left[1] + 1

    return width * height

def solution_part1(input_file: str) -> int:
    max_area: int = 0

    # @note There's got to be a smarter way to do this, it seems like a
    #       sufficient change in one axis, can compensate for a lack of change
    #       in another...
    for point in get_points(input_file):
        x, y = point

        for point2 in get_points(input_file):
            x2, y2 = point2

            area = calc_rect_size((x,y), (x2, y2))
            if area > max_area:
                max_area = area

    return max_area

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
