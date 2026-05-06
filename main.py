class Player:
    def __init__(self, name, marker):
        self.name = name
        self.marker = marker


class Board:
    def __init__(self, size):
        self.reset(size)

    def reset(self, size):
        self.size = size

        self.board = [["" for _ in range(size)] for _ in range(size)]

        self.rowCounts = {}
        self.colCounts = {}
        self.diagCounts = {}  

    def place(self, player, x, y):
        marker = player.marker

        if x < 0 or y < 0 or x >= self.size or y >= self.size:
            raise ValueError("Out of bounds")


        if self.board[y][x] != "":
            raise ValueError("Cell already occupied")

        self.board[y][x] = marker

        self.rowCounts[y] = self.rowCounts.get(y, {})
        self.rowCounts[y][marker] = self.rowCounts[y].get(marker, 0) + 1

        if self.rowCounts[y][marker] == self.size:
            return True


        self.colCounts[x] = self.colCounts.get(x, {})
        self.colCounts[x][marker] = self.colCounts[x].get(marker, 0) + 1

        if self.colCounts[x][marker] == self.size:
            return True


        if x == y:
            self.diagCounts["forward"] = self.diagCounts.get("forward", {})
            self.diagCounts["forward"][marker] = self.diagCounts["forward"].get(marker, 0) + 1

            if self.diagCounts["forward"][marker] == self.size:
                return True

        if x + y == self.size - 1:
            self.diagCounts["backward"] = self.diagCounts.get("backward", {})
            self.diagCounts["backward"][marker] = self.diagCounts["backward"].get(marker, 0) + 1

            if self.diagCounts["backward"][marker] == self.size:
                return True

        return False


class Game:
    def __init__(self, player1, player2, board):
        self.player1 = player1
        self.player2 = player2
        self.board = board

    def playGame(self):
        currTurn = 1
        moves = 0
        maxMoves = self.board.size * self.board.size

        while True:
            currPlayer = self.player1 if currTurn % 2 == 1 else self.player2

            try:
                x = int(input("Enter x: "))
                y = int(input("Enter y: "))

                if self.board.place(currPlayer, x, y):
                    print(f"{currPlayer.name} wins!")
                    break

                moves += 1

                if moves == maxMoves:
                    print("It's a draw!")
                    break

                currTurn += 1

            except ValueError as e:
                print(e)