# https://adventofcode.com/2021/day/2

from utils import read_input

file_path = "2021/02/input.txt"


def part_one():
    directions = {"forward": 0, "up": 0, "down": 0}
    for line in read_input(file_path):
        direction, value = line.split(" ")
        directions[direction] += int(value)
    return directions["forward"] * (directions["down"] - directions["up"])


def part_two():
    aim = 0
    horizontal = 0
    depth = 0
    for line in read_input(file_path):
        direction, value = line.split(" ")
        value = int(value)
        if direction == "down":
            aim += value
        if direction == "up":
            aim -= value
        if direction == "forward":
            horizontal += value
            depth += aim * value
    return horizontal * depth


def main():
    print(part_one())
    print(part_two())


if __name__ == "__main__":
    main()
