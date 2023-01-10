# https://adventofcode.com/2021/day/3

from utils import read_input

file_path = "2021/04/input.txt"


class BingoCard:
    def __init__(self):
        self.marked = set()
        self.grid = []

    def addRow(self, row):
        self.grid.append(row)

    def addMark(self, value):
        for row in len(self.grid):
            for col in len(self.grid[row]):
                if self.grid[row][col] == value:
                    self.marked.add((row, col))

    def hasWon(self):
        diagonal_set1 = set((0,0),(1,1),(2,2),(3,3),(4,4))
        diagonal_set2 = set((0,4),(1,3),(2,2),(3,1),(4,0))
        if diagonal_set1.issubset(self.marked) or diagonal_set2.issubset(self.marked):
            return True
    
        for row, col in self.marked:
            pass

    def sumUnmarked(self):
        total = 0
        for row in len(self.grid):
            for col in len(self.grid[row]):
                if (row, col) in self.marked:
                    continue
                total += self.grid[row][col]
        return total


def part_one():
    marks = []
    bingo_cards = []
    for line in read_input(file_path):
        if not marks:
            marks = line
        elif not line:
            bingo_cards.append(BingoCard())
        else:
            row = [num for num in line.split(" ") if num]  # Removes empty values 1 vs 01
            assert len(row) == 5
            bingo_cards[-1].addRow(row)
    
    won = False
    for mark in marks:
        if won:
            break
        for card in bingo_cards:
            card.addMark(mark)
            if card.hasWon():
                won = True
                break
    
    return sum([card.sumUnmarked() for card in bingo_cards])

def main():
    print(part_one())


if __name__ == "__main__":
    main()
