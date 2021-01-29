"""
N*M 보드를 만들고 입력대로 칠한다.
정상패턴으로 변경하고 좌표마다 변경여부를 저장한다.
8x8로 자를수 있는 방법대로 자르며 변경 횟수를 합한다.

시작 색상은 고민할 필요가 없다.
"""


def chess_board(n, m):
    ans = 32
    board = [[color for color in str(input())] for _ in range(n)]
    mark_board = [[0 for _ in range(m)] for _ in range(n)]

    # M*N 보드를 우선 정상 패턴으로 칠한다.
    fst_cell_color = 0
    for mark_i in range(n):
        cell_color = fst_cell_color
        for mark_j in range(m):
            if cell_color == 0 and board[mark_i][mark_j] != 'W':
                mark_board[mark_i][mark_j] = 1
            elif cell_color == 1 and board[mark_i][mark_j] != 'B':
                mark_board[mark_i][mark_j] = 1
            cell_color = (cell_color + 1) % 2
        fst_cell_color = (fst_cell_color + 1) % 2

    # 8*8로 자르며 가장 작은 횟수를 구한다.
    for board_i in range(n - 7):
        for board_j in range(m - 7):
            temp = 0
            for chess_k in range(board_i, board_i + 8):
                for chess_l in range(board_j, board_j + 8):
                    temp += mark_board[chess_k][chess_l]
            # "64 - temp"는 검은색으로 시작하는 보드로 만드는 경우를 말한다.
            ans = min(ans, temp, 64 - temp)

    return ans


N, M = map(int, input().split())
print(chess_board(N, M))
