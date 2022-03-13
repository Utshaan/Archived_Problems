from rich import print
from time import time


def allowed(board: list, num: int, pos: tuple) -> bool:
    for i in range(len(board)):
        if board[i][pos[1]] == num and pos[0] != i:
            return False

    for j in range(len(board)):
        if board[pos[0]][j] == num and pos[1] != j:
            return False

    for i in range((pos[0] // 3) * 3, (pos[0] // 3) * 3 + 3):
        for j in range((pos[1] // 3) * 3, (pos[1] // 3) * 3 + 3):
            if board[i][j] == num and (i, j) != pos:
                return False

    return True


def zeros(board):
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 0:
                return (i, j)


def solve(board):
    now = zeros(board)
    if not now:
        return True
    else:
        row, col = now

    for i in range(1, 10):
        if allowed(board, i, (row, col)):
            board[row][col] = i

            if solve(board):
                return True

            board[row][col] = 0
    return False


t_1 = time()
with open(
    r"D:\utkarsh\Github_Directories\Repo_Archived_Problems\ArchiveddashProblems\read_from_here\p096_sudoku.txt",
    "r",
) as fl:
    l = fl.readlines()
board_of_boards = []
l = [ele.strip() for ele in l]
for i in range(50):
    temp_board = []
    for j in range(i * 10 + 1, i * 10 + 10):
        temp_board.append(list(int(k) for k in list(l[j])))
    board_of_boards.append(temp_board)


for bo in board_of_boards:
    solve(bo)
ans = 0
for ele in board_of_boards:
    ans += sum(n * (10 ** (2 - ele[0][:3].index(n))) for n in ele[0][:3])
print(ans)
print(f"Time taken = {time() - t_1}")
