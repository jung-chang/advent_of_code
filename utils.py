import os
import pathlib


def read_input_gen(filename):
    with open(get_file_path(filename), "r") as file:
        for line in file:
            yield line.strip()


def read_input(filename):
    with open(get_file_path(filename), "r") as file:
        return [line.strip() for line in file]


def get_file_path(filename):
    return os.path.join(pathlib.Path(__file__).parent.resolve(), filename)
