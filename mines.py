import random
from enum import IntFlag
from dataclasses import dataclass
import re

coords = "123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

mine = "💣"
digits = ["⏹️ ", "1️⃣ ", "2️⃣ ", "3️⃣ ", "4️⃣ ","5️⃣ ", "6️⃣ ", "7️⃣ ", "8️⃣ "]

class State(IntFlag):
    Marked = 32
    Checked = 64
    Mine = 128

    Empty = 0
    Neighbours = 15

    @property
    def is_empty(self) -> bool:
        return self.neighbour_mine_count == 0
    
    @property
    def neighbour_mine_count(self) -> int:
        return self & State.Neighbours
    
    @property
    def str(self) -> str:
        if State.Marked in self:
            return mine
        elif State.Checked in self:
            return mine if State.Mine in self else digits[self.neighbour_mine_count]
        else:
            return "  "

@dataclass
class Board:
    height: int
    width: int
    mines: int

    def __post_init__(self):
        self.board: list[list[State]] = [[State.Empty] * self.width for _ in range(self.height)]
        self.set_mines(self.mines)
        self.checked = 0

    def toggle_mark(self, row: int, col: int) -> None:
        self.board[row][col] ^= State.Marked

    @property
    def remaining(self) -> int:
        return self.width * self.height - self.mines - self.checked

    def __repr__(self) -> str:
        top = "  " + "".join([ch+" " for ch in coords[:self.width]])
        lines = [f"{mine} Mine Sweeper {mine}".center(len(top))]
        lines.append("")
        lines.append(top)
        for idx, line in enumerate(self.board):
            lines.append(coords[idx]+" "+"".join(v.str for v in line))
        lines.append("")
        lines.append(f"Remaining {self.remaining}")
        lines.append("")
        return "\n".join(lines)

    def set_mines(self, number_of_mines: int) -> None:
        count = 0
        while count < number_of_mines:
            row, col = divmod(random.randint(0, self.height*self.width-1), self.width)
            if State.Mine not in self.board[row][col]:
                count = count + 1
                self.board[row][col] = State.Mine
        for row in range(self.height):
            for col in range(self.width):
                if State.Mine not in self.board[row][col]:
                    self.board[row][col] = State(sum(
                        State.Mine in self.board[coord[0]][coord[1]] 
                        for coord in self.get_coords_around(row, col))
                    )

    def get_coords_around(self, row: int, col: int):
        for y in range(max(row-1, 0), min(row+2, self.height)):
            for x in range(max(col-1, 0), min(col+2, self.width)):
                if (y, x) == (row, col):
                    continue
                yield y, x

    def floodfill(self, row: int, col: int):
        if State.Checked in self.board[row][col]:
            return
        self.checked += 1
        self.board[row][col] |= State.Checked
        if self.board[row][col].is_empty:
            for coords in self.get_coords_around(row, col):
                self.floodfill(coords[0], coords[1])

    def clear(self, row: int, col: int) -> bool:
        if State.Mine in self.board[row][col]:
            for row in range(self.height):
                for col in range(self.width):
                    self.board[row][col] |= State.Checked
            print(self)
            print("😭 BLOWN UP 😭")
            return False
        else:
            self.floodfill(row, col)
            if self.remaining == 0:
                print(self)
                print("😊 ALL CLEAR 😊")
                return False
        return True

class Game:
    def __init__(self, board_height: int, board_width: int, number_of_mines: int):
        self.board = Board(board_height, board_width, number_of_mines)

    def play(self):
        while True:
            print(self.board)
            row, col, *mark = [coords.find(v.upper()) for v in re.split(r'\s+', input('row col [mark]: '))]
            if mark:
                self.board.toggle_mark(row, col)
            else:
                if not self.board.clear(row, col):
                    break

if __name__ == "__main__":
    Game(10, 10, 5).play()