import random

b = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
     [6, 0, 0, 1, 9, 5, 0, 0, 0],
     [0, 9, 8, 0, 0, 0, 0, 6, 0],
     [8, 0, 0, 0, 6, 0, 0, 0, 3],
     [4, 0, 0, 8, 0, 3, 0, 0, 1],
     [7, 0, 0, 0, 2, 0, 0, 0, 6],
     [0, 6, 0, 0, 0, 0, 2, 8, 0],
     [0, 0, 0, 4, 1, 9, 0, 0, 5],
     [0, 0, 0, 0, 8, 0, 0, 7, 9]]


def fill_col(board, index):
    a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for row in range(9):
        num = board[row][index]
        if num != 0:
            a.remove(num)
        else:
            continue
    for row in range(9):
        num = board[row][index]
        if num == 0:
            board[row][index] = random.choice(a)
            a.remove(board[row][index])


def fill_board(board):
    for column in range(9):
        fill_col(board, column)


def col(board, num):
    return [row[num] for row in board]


def box(board, index):
    a = []
    if index == 0:
        r1 = range(3)
        r2 = range(3)
    elif index == 1:
        r1 = range(3)
        r2 = range(3, 6)
    elif index == 2:
        r1 = range(3)
        r2 = range(6, 9)
    elif index == 3:
        r1 = range(3, 6)
        r2 = range(3)
    elif index == 4:
        r1 = range(3, 6)
        r2 = range(3, 6)
    elif index == 5:
        r1 = range(3, 6)
        r2 = range(6, 9)
    elif index == 6:
        r1 = range(6, 9)
        r2 = range(3)
    elif index == 7:
        r1 = range(6, 9)
        r2 = range(3, 6)
    elif index == 8:
        r1 = range(6, 9)
        r2 = range(6, 9)
    else:
        return None
    for i in r1:
        for j in r2:
            a.append(board[i][j])
    return a


def new_board(board, unsolved):
    new = board.copy()
    a = list(range(9))
    col_num = random.choice(a)
    for i in range(9):
        if col(unsolved, col_num)[i] != 0:
            a.remove(i)
    row1 = random.choice(a)
    a.remove(row1)
    row2 = random.choice(a)
    new[row1][col_num], new[row2][col_num] = new[row2][col_num], new[row1][col_num]
    return new


def errors(board):
    err = 0
    for row in board:
        for i in row:
            err += row.count(i)-1
    for box_index in range(9):
        for i in box(board, box_index):
            err += box(board, box_index).count(i)-1
    return err


def diff(board1, board2):
    return errors(board1) - errors(board2)


def solve(board):
    puzzle = [row[:] for row in board]
    fill_board(board)
    energy = 1
    best_so_far = [row[:] for row in board]
    while energy > 0.1 and errors(best_so_far) != 0:
        if errors(board) < errors(best_so_far):
            best_so_far = [row[:] for row in board]
            check_next = new_board(board, puzzle)
            if errors(check_next) <= errors(board):
                board = check_next
            elif errors(check_next) > errors(board):
                if random.random() < (1/diff(check_next, board))*energy*5:
                    board = check_next
                else:
                    break
        else:
            board = new_board(board, puzzle)
        if (errors(board) - errors(best_so_far)) > 7:
            board = [row[:] for row in best_so_far]
        for rw in board:
            print(rw)
        print('')
        energy *= 0.999
    for rw in best_so_far:
        print(rw)
    print('')
    print(errors(best_so_far), 'errors.')


solve(b)
