import re

coords = "123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

class Game:
    def __init__(self, height: int, width: int, mines: int):
        self.board = coords[:width] + '\n' + ('*' * width + '\n') * height

    def get_input(self):
        row, col, *mark = [coords.find(v.upper()) for v in re.split(r'\s+', input('row col [mark]: '))]
        return row, col, bool(mark)

    def play(self):
        while True:
            print(self.board)
            row, col, mark = self.get_input()
            print(row, col, mark)

Game(10, 10, 5).play()