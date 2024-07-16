import re
from dataclasses import dataclass
from random import randint

coords = "123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
digits = ["⏹️ ", "1️⃣ ", "2️⃣ ", "3️⃣ ", "4️⃣ ","5️⃣ ", "6️⃣ ", "7️⃣ ", "8️⃣ "]

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
        lines: list[str] = [' ' + ' '.join(coords[:self.width])]
        for y in range(self.height):
            line = coords[y]
            for x in range(self.width):
                if (y,x) in self.marks:
                    line += "💣"
                elif (y,x) not in self.cleared:
                    line += "  "
                else:
                    line += "💣" if (y,x) in self.mines else digits[self.neighbouring_mines(y, x)]
            lines.append(line)
        lines.append("")
        lines.append(f"Remaining: {self.remaining}")
        return "\n".join(lines)

    def neighbouring_mines(self, row: int, col: int) -> int:
        return sum([
            (row - 1,col - 1) in self.mines,
            (row - 1,col + 0) in self.mines,
            (row - 1,col + 1) in self.mines,
            (row + 0,col - 1) in self.mines,
            (row + 0,col + 1) in self.mines,
            (row + 1,col - 1) in self.mines,
            (row + 1,col + 0) in self.mines,
            (row + 1,col + 1) in self.mines,
        ])

    def fill(self, row: int, col: int):
        if (row, col) in self.cleared:
            return
        self.cleared.add((row, col))
        if self.neighbouring_mines(row, col) == 0:
            for y in range(row-1, row+2):
                for x in range(col-1, col+2):
                    if (y, x) == (row, col):
                        continue
                    if not (0 <= y < self.height and 0 <= x < self.width):
                        continue
                    self.fill(y, x)

    def clear(self, row: int, col: int):
        if (row, col) in self.mines:
            for row in range(self.height):
                for col in range(self.width):
                    self.cleared.add((row, col))
            print(self)
            print("😭 BLOWN UP 😭")
            return False
        self.fill(row, col)
        return True

    def toggle_mark(self, row: int, col: int):
        if (row, col) in self.marks:
            self.marks.remove((row, col))
        else:
            self.marks.add((row, col))

    @property
    def remaining(self) -> int:
        return self.width * self.height - len(self.marks) - len(self.cleared)

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
            if self.board.remaining == 0:
                print(self)
                print("😊 ALL CLEAR 😊")
                break

Game(10, 10, 5).play()