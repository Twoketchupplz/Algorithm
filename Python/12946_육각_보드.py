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

import sys

sys.setrecursionlimit(100000)


def dfs(x, y, color):
    global N, board, ans
    dx = [-1, -1, 0, +1, +1, 0]
    dy = [0, +1, +1, 0, -1, -1]

    board[x][y] = color
    ans = max(ans, 1)
    for idx in range(6):
        adj_x, adj_y = x + dx[idx], y + dy[idx]
        if not (0 <= adj_x < N and 0 <= adj_y < N): continue
        if board[adj_x][adj_y] == '-': continue
        if board[adj_x][adj_y] == 'X':
            dfs(adj_x, adj_y, 1 - color)
        ans = max(ans, 2)
        if board[adj_x][adj_y] == color:
            ans = max(ans, 3)


def color_tile():
    global N, board
    for i in range(N):
        for j in range(N):
            if board[i][j] == 'X':
                dfs(i, j, 0)
    return ans


global board, ans
ans = 0
N = int(input())
board = [list(input()) for _ in range(N)]
print(color_tile())
