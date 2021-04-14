"""
https://www.acmicpc.net/problem/12946
offset coordinates 로 표현된 육각 타일에 색이 이웃하지 않게 칠할 때 칠해지는 색의 개수
4색정리: 평면을 유한 개의 부분으로 나누어 각 부분에 색을 칠할 때, 서로 맞닿은 부분을 다른 색으로 칠한다면 네 가지 색으로 충분하다
hex tile 의 경우 최대 3개의 색만 필요하다.

아이디어
DFS
꼭 사용해야 하는 이유
이어진 모든타일을 전체를 다같이 판단해야한다. 부분만보고 2가지 색으로 충분한데 3가지 색으로 판단할 수 있기 때문이다.
각 타일마다 주변만 체크한다고 되는 일이 아니다.
"""


# 보드를 색칠한다 '-' = -1, 'X' = 0, 색상은 1, 2, 3
def get_board(n, naive_board):
    new_board = []
    for i in range(n):
        new_board.append([])
        for j in range(n):
            if naive_board[i][j] == '-':
                new_board[i].append(-1)
            else:
                new_board[i].append(0)

    return new_board


# (x-1, y), (x-1, y+1),
# (x, y+1),  (x, y-1),
# (x+1, y), (x+1, y-1)
def get_neighbor(cur_node_x, cur_node_y, board):
    global N, Board
    color = {1: False, 2: False}
    # print("-----", cur_node, "-----")
    dx = [-1, -1, 0, +1, +1, 0]
    dy = [0, +1, +1, 0, -1, -1]
    for idx in range(-1, 6):  # 중복검사
        x = cur_node_x + dx[idx]
        y = cur_node_y + dy[idx]
        if 0 <= x < N and 0 <= y < N and board[x][y] > 0:
            if board[x][y] == 1:
                color[1] = True
            elif board[x][y] == 2:
                color[2] = True

    # print(color[1], color[2])
    if color[1] and color[2]:
        return 3
    elif color[1]:
        board[cur_node_x][cur_node_y] = 2
        return 2
    elif color[2]:
        board[cur_node_x][cur_node_y] = 1
        return 2
    else:
        board[cur_node_x][cur_node_y] = 1
        return 1


def color_tile():
    global N, Board
    ans = 0
    board = get_board(N, Board)
    node_list = []
    for i in range(N):
        for j in range(N):
            if Board[i][j] == 'X':
                node_list.append((i, j))

    # 모든 타일이 '-'인 경우 아래 반복문은 수행하지 않고 ans = 0이다.
    for v in node_list:
        if ans < 3:
            ans = max(ans, get_neighbor(v[0], v[1], board))
            # print(board)
        else:
            return ans

    return ans


N = int(input())
Board = [list(input()) for _ in range(N)]
print(color_tile())
