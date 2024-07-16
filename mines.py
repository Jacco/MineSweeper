import re
from dataclasses import dataclass

coords = "123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

@dataclass
class Board:
    height: int
    width: int
    mine_count: int

    def __post_init__(self):
        self.mines: set[tuple[int,int]] = {(5,5)}

    def __repr__(self):
        lines: list[str] = []
        for y in range(self.height):
            line = ''.join("💣" if (y,x) in  self.mines else "  " for x in range(self.width))
            lines.append(line)
        return "\n".join(lines)

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
            print(row, col, mark)

Game(10, 10, 5).play()