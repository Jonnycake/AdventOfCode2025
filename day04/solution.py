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

    papers_removed = None
    diagram = load_diagram(input_file)

    while papers_removed is None or papers_removed > 0:
        papers_removed = 0

        for y in range(len(diagram)):
            for x in range(len(diagram[y])):
                if diagram[y][x] != '@':
                    continue

                if can_access(diagram, x, y):
                    solution += 1
                    papers_removed += 1
                    diagram[y][x] = '-'

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
