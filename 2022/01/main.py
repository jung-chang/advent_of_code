# https://adventofcode.com/2022/day/1

file_path = "input.txt"

import os
import pathlib
import heapq


def read_input_gen(filename):
    with open(get_file_path(filename), "r") as file:
        for line in file:
            yield line.strip()


def read_input(filename):
    with open(get_file_path(filename), "r") as file:
        return [line.strip() for line in file]


def get_file_path(filename):
    return os.path.join(pathlib.Path(__file__).parent.resolve(), filename)


def part_one():
    max_calories = 0
    current_calories = 0
    for num in read_input_gen(file_path):
        if len(num):
            current_calories += int(num)
        else:
            max_calories = max(current_calories, max_calories)
            current_calories = 0
    return max_calories


def part_two():
    heap = []
    current_calories = 0
    for num in read_input_gen(file_path):
        if len(num):
            current_calories += int(num)
        else:
            heapq.heappush(heap, -1 * current_calories)
            current_calories = 0
    return -1 * sum(heapq.nsmallest(3, heap))


def main():
    print(part_one())
    print(part_two())


if __name__ == "__main__":
    main()
