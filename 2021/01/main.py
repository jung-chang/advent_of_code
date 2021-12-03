# https://adventofcode.com/2021/day/1

from utils import read_input_gen

file_path = "2021/01/input.txt"


def part_one():
    increment_count = 0
    last_number = None
    for line in read_input_gen(file_path):
        next_number = int(line)
        if last_number is None:
            last_number = next_number
            continue
        if next_number > last_number:
            increment_count += 1
        last_number = next_number
    return increment_count


def part_two():
    increment_count = 0
    num_list = []
    for num in read_input_gen(file_path):
        if len(num_list) < 4:
            num_list.append(int(num))
        if len(num_list) == 4:
            if sum(num_list[:3]) < sum(num_list[1:4]):
                increment_count += 1
            num_list.pop(0)
    return increment_count


def main():
    print(part_one())
    print(part_two())


if __name__ == "__main__":
    main()
