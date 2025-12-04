#!/usr/bin/env python3
import sys

def load_diagram(input_file: str) -> list[list[str]]:
    diagram = []

    with open(input_file, 'r') as f:
        for line in f:
            diagram.append([a for a in line.strip()])

    return diagram

def can_access(diagram: list[list[str]], x: int, y: int, max_adjacent_papers: int = 3) -> bool:
    if diagram[y][x] != '@':
        return False

    adjacent = [
        # Top
        (x-1, y-1), (x, y-1), (x+1, y-1),

        # Sides
        (x+1, y),
        (x-1, y),

        # Bottom
        (x+1, y+1), (x, y+1), (x-1, y+1),
    ]

    adjacent_papers: int = 0
    for x,y in adjacent:
        if x < 0 or y < 0 or y >= len(diagram) or x >= len(diagram[y]):
            continue

        if diagram[y][x] == '@':
            adjacent_papers += 1

        if adjacent_papers > max_adjacent_papers:
            return False;

    return True

def print_diagram(diagram: list[list[str]]):
    for row in diagram:
        print("".join(row))
    print("\n")

def solution_part1(input_file: str) -> int:
    solution: int = 0

    diagram = load_diagram(input_file)
    solution_diagram: list[list[str]] = [
        [cell for cell in row]
            for row in diagram
    ]

    for y in range(len(diagram)):
        for x in range(len(diagram[y])):
            if diagram[y][x] != '@':
                continue

            if can_access(diagram, x, y):
                solution += 1
                solution_diagram[y][x] = '-'

    print_diagram(solution_diagram)
    return solution

def solution_part2(input_file: str) -> int:
    solution: int = 0

    diagram = load_diagram(input_file)

    height = len(diagram)
    width = len(diagram[0])

    papers_removed = None

    while papers_removed is None or papers_removed > 0:
        papers_removed = 0

        for offset in range(width // 2):
            top = offset
            bottom = height - offset - 1
            left = offset
            right = width - offset - 1

            # Top
            for x in range(left, right + 1):
                if diagram[top][x] != '@':
                    continue

                if can_access(diagram, x, top):
                    solution += 1
                    papers_removed += 1
                    diagram[top][x] = '-'

            # Right
            for y in range(top, bottom + 1):
                if diagram[y][right] != '@':
                    continue

                if can_access(diagram, right, y):
                    solution += 1
                    papers_removed += 1
                    diagram[y][right] = '-'


            # Bottom
            for x in range(right, left - 1, -1):
                if diagram[bottom][x] != '@':
                    continue

                if can_access(diagram, x, bottom):
                    solution += 1
                    papers_removed += 1
                    diagram[bottom][x] = '-'

            # Left
            for  y in range(bottom, top - 1, -1):
                if diagram[y][left] != '@':
                    continue

                if can_access(diagram, left, y):
                    solution += 1
                    papers_removed += 1
                    diagram[y][left] = '-'


    print_diagram(diagram)
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
