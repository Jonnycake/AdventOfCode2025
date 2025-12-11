#!/usr/bin/env python3
#
# Summary
# - Input = location of junciton boxes
# - Junction boxes only get connected to their closest neighbor
# - Output = product of the size of 3 largest circuits
#
# @note
# Definitely struggled on this one
#  - First issue was not not really understanding what I was looking for
#    I took it as "top N closest neighbors" so A-B C-D E-F instead of
#    A-B A-C C-D E-F
#  - Then it took a while to notice that the order that connections were
#    made could result in disconnected circuits which should be connected
#
# I got the answer in the end, but it wsa rough and the code is nasty
#
# I'll be coming back to this to clean up the logic and get part 2 figured
# out sometime in the next couple weeks

import sys

SIZE = 1000

X = 0
Y = 1
Z = 2

def calc_distance(p1: tuple[int, int, int], p2: tuple[int, int, int]):
    dx = p2[X] - p1[X]
    dy = p2[Y] - p1[Y]
    dz = p2[Z] - p1[Z]

    return dx**2 + dy**2 + dz**2

def get_box_locations(input_file: str) -> list[tuple[int, int, int]]:
    box_locations: list[tuple[int, int, int]] = []

    with open(input_file, 'r') as f:
        for line in f:
            x, y, z = [int(v) for v in line.strip().split(",")]

            box_locations.append((x, y, z))

    return box_locations

def solution_part1(input_file: str) -> int:
    solution: int = 1
    box_locations = get_box_locations(input_file)

    calculated = set()
    distances = []
    for box in box_locations:
        for box2 in box_locations:
            if box == box2:
                continue

            if (box, box2) in calculated or (box2, box) in calculated:
                continue

            distances.append(((box, box2), calc_distance(box, box2)))
            calculated.add((box, box2))

    distances.sort(key=lambda v: v[1])

    circuits = []
    for distance in distances[:SIZE]:
        box, box2 = distance[0]

        full_circuit = set([box, box2])

        for i, circuit in enumerate(circuits):
            if box not in circuit and box2 not in circuit:
                continue

            full_circuit |= circuit
            circuits[i] = full_circuit

        circuits.append(full_circuit)

    unique_circuits = []
    for circuit in circuits:
        if circuit in unique_circuits:
            continue
        unique_circuits.append(circuit)

    unique_circuits.sort(key=len, reverse=True)
    for circuit in unique_circuits[:3]:
        solution *= len(circuit)

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
