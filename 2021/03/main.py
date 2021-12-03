# https://adventofcode.com/2021/day/3

from utils import read_input

file_path = "2021/03/input.txt"


def part_one():
    gamma_rate = ""  # Most common bit at each position
    values = read_input(file_path)
    for index, _ in enumerate(values[0]):
        index_values = [value[index] for value in values]
        gamma_rate += max(index_values, key=index_values.count)
    epsilon_rate = "".join(["1" if i == "0" else "0" for i in gamma_rate])
    return int(gamma_rate, 2) * int(epsilon_rate, 2)


def part_two():
    oxygen_rating = ""
    scubber_rating = ""

    def most_common(index, values, tiebreaker):
        index_values = [value[index] for value in values]
        if index_values.count("1") == index_values.count("0"):
            return tiebreaker
        return "1" if index_values.count("1") > index_values.count("0") else "0"

    def least_common(index, values, tiebreaker):
        index_values = [value[index] for value in values]
        if index_values.count("1") == index_values.count("0"):
            return tiebreaker
        return "1" if index_values.count("1") < index_values.count("0") else "0"

    values = read_input(file_path)
    for index, _ in enumerate(values[0]):
        common_bit = most_common(index, values, tiebreaker="1")
        values = [value for value in values if value[index] == common_bit]
        if len(values) == 1:
            oxygen_rating = values[0]
            break

    values = read_input(file_path)
    for index, _ in enumerate(values[0]):
        common_bit = least_common(index, values, tiebreaker="0")
        values = [value for value in values if value[index] == common_bit]
        if len(values) == 1:
            scubber_rating = values[0]
            break
    return int(oxygen_rating, 2) * int(scubber_rating, 2)


def main():
    print(part_one())
    print(part_two())


if __name__ == "__main__":
    main()
