import re
from dataclasses import dataclass
from random import randint

coords = "123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

@dataclass
class Board:
    height: int
    width: int
    mine_count: int

    def __post_init__(self):
        self.mines: set[tuple[int,int]] = set()
        self.marks: set[tuple[int,int]] = set()
        self.cleared: set[tuple[int,int]] = set()
        count = 0
        while count < self.mine_count:
            row, col = divmod(randint(0, self.height*self.width-1), self.width)
            if (row, col) not in self.mines:
                count = count + 1
                self.mines.add((row, col))

    def __repr__(self):
        lines: list[str] = []
        for y in range(self.height):
            line = ''
            for x in range(self.width):
                if (y,x) in self.marks:
                    line += "💣"
                elif (y,x) not in self.cleared:
                    line += "  "
                else:
                    line += "💣" if (y,x) in self.mines else "⏹️ "
            lines.append(line)
        return "\n".join(lines)
    
    def clear(self, row: int, col: int):
        self.cleared.add((row, col))
        return True

    def toggle_mark(self, row: int, col: int):
        if (row, col) in self.marks:
            self.marks.remove((row, col))
        else:
            self.marks.add((row, col))

class Game:
    def __init__(self, height: int, width: int, mine_count: int):
        self.board = Board(height, width, mine_count)

    def get_input(self):
        row, col, *mark = [coords.find(v.upper()) for v in re.split(r'\s+', input('row col [mark]: '))]
        return row, col, bool(mark)

    def play(self):
        while True:
            print(self.board)
            row, col, mark = self.get_input()
            if mark:
                self.board.toggle_mark(row, col)
            else:
                if not self.board.clear(row, col):
                    break

Game(10, 10, 5).play()