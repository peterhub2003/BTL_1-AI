import numpy as np


class Board:
    def __init__(self, n):
        self.N = n

    def Draw_board(self, position: np.array):
        for i in range(self.N):
            for j in range(self.N):
                if j == position[i]:
                    print('|', end='Q')
                else:
                    print('|', end=' ')
            print('|')


class DFS:
    def __init__(self, n):
        self.n = n
        self.solutions = []

    def is_safe(self, board, row, col):
        # Kiểm tra xem vị trí đặt quân hậu có hợp lệ hay không
        for i in range(row):
            if board[i] == col or \
               board[i] - i == col - row or \
               board[i] + i == col + row:
                return False
        return True

    def solve_nqueens(self):
        def dfs(row, board):
            if len(self.solutions) == 1:
                return
            if row == self.n:
                self.solutions.append(np.array(board))
                return
            for col in range(self.n):
                if self.is_safe(board, row, col):
                    board.append(col)
                    dfs(row + 1, board)
                    board.pop()

        dfs(0, [])
        return self.solutions


if __name__ == '__main__':
    n = int(input("Nhập số quân hậu: "))
    Board = Board(n)
    solution = DFS(n)
    solution.solve_nqueens()
    for i, position in enumerate(solution.solutions):
        print("Solution", i + 1, ':')
        Board.Draw_board(position)
