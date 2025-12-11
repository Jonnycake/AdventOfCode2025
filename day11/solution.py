#!/usr/bin/env python3
#
# Summary:
# - Input = node and their potential next nodes (separated by :)
# - Solution = How many paths you can take from you to out
#
# We can do this recursively (will likely be easiest):
# 1. Find nodes that go to out
# 2. Put them through the recursive search
# 3. Add their results

import sys

def get_connections(input_file: str) -> dict[str,list[str]]:
    connections: dict[str,list[str]] = {}
    with open(input_file, 'r') as f:
        for line in f:
            node = line.split(':')[0]
            attached_nodes = line.split(':')[1].strip().split(" ")

            connections[node] = attached_nodes

    return connections


_path_memo = {}
def count_paths_to(target: str, connections: dict[str, list[str]]) -> int:
    if target in _path_memo:
        return _path_memo[target]

    num_paths: int = 0

    for node, attached_nodes in connections.items():
        if target not in attached_nodes:
            continue

        if node == 'you':
            num_paths += 1
            continue

        if target in attached_nodes:
            num_paths += count_paths_to(node, connections)

    _path_memo[target] = num_paths

    return num_paths

def solution_part1(input_file: str) -> int:
    connections = get_connections(input_file)

    return count_paths_to('out', connections)

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
