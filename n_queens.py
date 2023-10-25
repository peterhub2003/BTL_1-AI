import random
from math import exp
import time
from copy import deepcopy
import pandas as pd

def threat_calculate(n):
    '''Combination formular. It is choosing two queens in n queens'''
    if n < 2:
        return 0
    if n == 2:
        return 1
    return int((n - 1) * n / 2)

class Initialization:
  def __init__(self, n_queens, stragery = None):
    self.n = n_queens
    self.stragery = stragery

  def create_board(self):
    chess_board = {}
    temp = list(range(self.n))
    random.shuffle(temp)  # shuffle to make sure it is random
    column = 0

    while len(temp) > 0:
        row = random.choice(temp)
        chess_board[column] = row
        temp.remove(row)
        column += 1
    del temp
    return chess_board

  def fast_create_board(self):
    chess_board = None
    temp = list(range(self.n))
    random.shuffle(temp)

    chess_board = dict(zip(range(self.n), temp))
    return chess_board


def init_diagonal(chess_board, nega_dia, pos_dia):
  n = len(chess_board)
  first_cost = 0

  for col in chess_board:
    row = chess_board[col]
    nega_dia[row + col] += 1
    pos_dia[n - 1 + row - col] += 1

  for i in nega_dia:
    first_cost += threat_calculate(i)
  for i in pos_dia:
    first_cost += threat_calculate(i)

  return first_cost


def optimizal_cost(col_1, col_2, chess_board, nega_diagonal, pos_diagonal) -> bool:
  n_queens = len(chess_board)
  row_1, row_2 = chess_board[col_1], chess_board[col_2]

  old_threat = nega_diagonal[row_1 + col_1] + nega_diagonal[row_2 + col_2] + pos_diagonal[n_queens - 1 + row_1 - col_1] + pos_diagonal[n_queens - 1 + row_2 - col_2] - 4
  new_threat = nega_diagonal[row_2 + col_1] + nega_diagonal[row_1 + col_2] + pos_diagonal[n_queens - 1 + row_2 - col_1] + pos_diagonal[n_queens - 1 + row_1 - col_2]

  if abs(row_1 - row_2) == abs(col_1 - col_2):
     old_threat -= 1
     new_threat += 1

  return old_threat, new_threat

def update(col_1, col_2, chess_board, nega_diagonal, pos_diagonal):
  n_queens = len(chess_board)
  row_1, row_2 = chess_board[col_1], chess_board[col_2]

  nega_diagonal[row_1 + col_1] -= 1
  pos_diagonal[n_queens - 1 + row_1 - col_1] -= 1
  nega_diagonal[row_2 + col_2] -= 1
  pos_diagonal[n_queens - 1 + row_2 - col_2] -= 1

  nega_diagonal[row_2 + col_1] += 1
  pos_diagonal[n_queens - 1 + row_2 - col_1] += 1
  nega_diagonal[row_1 + col_2] += 1
  pos_diagonal[n_queens - 1 + row_1 - col_2] += 1

  return True

def print_result(i, iterations, time, col_first, ans_cost):
   print(f"Init =  {i}     |  Iterations =  {iterations}     |  Run Time =  {time}      |   First Cost =  {col_first}    |  Answer Cost =  {ans_cost}")

def simulated_annealing(no_of_init, N_QUEENS, T_min = 0, T_max = 1000, sch = 0.95):

    '''Simulated Annealing'''
    solution_found = False
    init = Initialization(N_QUEENS)

    s = time.time()
    if N_QUEENS < 1e4:
      answer = init.create_board()
    else:
      answer = init.fast_create_board()
    e = time.time()
    #print(f"Create Board successfully in  {e - s} seconds")

    nega_diagonal = [0] * (2*N_QUEENS - 1)
    pos_diagonal = [0] * (2*N_QUEENS - 1)
    s = time.time()
    first_cost = init_diagonal(answer, nega_diagonal, pos_diagonal)
    e = time.time()
    #print(f"Init Diagonal and calculate first cost successfully in  {e - s} seconds")

    cost_answer = first_cost
    t = T_max
    sch = sch
    iterations = 0
    number_of_dec = 0

    start_algo = time.time()
    random_uni = 0
    max_delta, no_delta = 0, 0
    num_unchange = 0
    max_unchange = 2
    _cost = cost_answer

    while t > T_min:
        t *= sch

        while True:
            index_1 = random.randrange(0, N_QUEENS - 1)
            index_2 = random.randrange(0, N_QUEENS - 1)
            if index_1 != index_2:
                break

        old_cost, new_cost = optimizal_cost(index_1, index_2, answer, nega_diagonal, pos_diagonal)
        delta = new_cost - old_cost

        max_delta = max(max_delta, abs(delta))
        if delta < 0:
          number_of_dec += 1

        if delta < 0 or random.uniform(0, 1) < exp(-delta / t): #or num_unchange >= max_unchange:

            if delta > 0:
              random_uni += 1
            else:
              no_delta += 1

            update(index_1, index_2, answer, nega_diagonal, pos_diagonal)
            answer[index_1], answer[index_2] = answer[index_2], answer[index_1]  # swap two chosen queens
            cost_answer = cost_answer + delta

            #_cost = cost_answer
            # if num_unchange >= max_unchange:
            #   num_unchange = 0


        iterations += 1
        if iterations % (N_QUEENS * 10) == 0:
            print(f"Epochs:   {iterations}  | Cost:   {cost_answer}  |  Random Uniform:   {random_uni}  |  Delta = 0:  {no_delta}  |Max delta:  {abs(max_delta)}  |  Num_of_dec:   {number_of_dec}")
            random_uni = 0
            number_of_dec = 0
            no_delta = 0
            # if cost_answer - _cost == 0:
            #   num_unchange += 1

        #if max(nega_diagonal) == 1 and max(pos_diagonal) == 1:
        if cost_answer == 0:

            solution_found = True
            #print_chess_board(answer)
            end_algo = time.time()
            exec_time = round(end_algo - start_algo, 3)
            #ans_cost = init_diagonal(answer, [0]*(2*N_QUEENS - 1),[0]*(2*N_QUEENS - 1))
            print_result(no_of_init, iterations, exec_time, first_cost, cost_answer)
            break


    if solution_found is False:
        print("Failed")

    return first_cost, iterations, answer, exec_time


def print_chess_board(board):
    '''Print the chess board'''
    print(list(board.values()))


def main(N: int, N_QUEENS: int, T_max=None):
    results = {"Init": [], "First_cost": [], "Iterations": [], "Time": [], "Answer": []}

    for init in range(1, N + 1):
      if T_max == None:
        first_cost, iterations, answer, time = simulated_annealing(init, N_QUEENS)
      else:
        first_cost, iterations, answer, time = simulated_annealing(init, N_QUEENS, T_max)

      results["Init"].append(init)
      results["First_cost"].append(first_cost)
      results["Iterations"].append(iterations)
      results["Time"].append(time)
      results['Answer'].append(list(answer.values()))


    df = pd.DataFrame(results)
    return df

def compare_temperature(temp: list[int], n_queens: int, no_of_init = 1):
  for T_max in temp:
    results = main(no_of_init, n_queens, T_max)

def main_running(list_n_queens: list[int], no_of_init: int, T_max=None, is_recorded = False):
    for n_queen in list_n_queens:
      print(f"********************************* {n_queen} - QUEENS *********************************")
      if T_max == None:
        results = main(no_of_init, n_queen)
      else:
        results = main(no_of_init, n_queen, T_max = T_max)
      if is_recorded:
        results.to_csv(f"results_{n_queen}.csv", index=False)

if __name__ == "__main__":

    list_temp = [1000, 2000, 3000, 5000, 10000]
    number_of_init = 1
    main_running([100000], number_of_init, is_recorded = False)
