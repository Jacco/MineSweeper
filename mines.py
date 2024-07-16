coords = "123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

class Game:
    def __init__(self, height: int, width: int, mines: int):
        self.board = coords[:width] + '\n' + ('*' * width + '\n') * height

    def get_input(self):
        return input("row col [mark]: ")

    def play(self):
        while True:
            print(self.board)
            self.get_input()

Game(10, 10, 5).play()