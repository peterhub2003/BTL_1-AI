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


class BFS:
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
        # Tạo queue để lưu trạng thái ban đầu
        queue = []

        # Bắt đầu từ hàng đầu tiên
        for i in range(self.n):
            board = np.array([0]*self.n)
            board[0] = i
            queue.append((board, 1))

        while queue:
            board, row = queue.pop(0)  # Lấy trạng thái từ queue

            if len(self.solutions) == 1:
                break

            if row == self.n:
                # Nếu đã đặt N quân hậu, thì lưu giải pháp
                self.solutions.append(board)
            else:
                # Nếu chưa đặt đủ N quân hậu, thử đặt ở hàng tiếp theo
                for col in range(self.n):
                    if self.is_safe(board, row, col):
                        new_board = board.copy()
                        new_board[row] = col
                        queue.append((new_board, row + 1))

        return self.solutions


if __name__ == '__main__':
    n = int(input("Nhập số quân hậu: "))
    Board = Board(n)
    solution = BFS(n)
    solution.solve_nqueens()
    for i, position in enumerate(solution.solutions):
        print("Solution", i + 1, ':')
        Board.Draw_board(position)
