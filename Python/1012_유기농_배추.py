# https://www.acmicpc.net/problem/1012

import sys


# dfs
def dfs(land: list, st: list, width, length):
    cur: list = st.pop()
    land[cur[0]][cur[1]] = 2
    for i in range(4):
        n_row, n_col = cur[0] + dr[i], cur[1] + dc[i]
        if width > n_row >= 0 and length > n_col >= 0 and land[n_row][n_col] == 1:
            st.append([n_row, n_col])
            dfs(land, st, width, length)


sys.setrecursionlimit(10000)
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

ans = 0

# 테스트 개수 T 입력; T 만큼 반복
for _ in range(int(input())):
    # 가로 M, 세로 N, 배추 수 K 입력
    M, N, K = map(int, input().split())
    plowland = [[0 for _ in range(M)] for _ in range(N)]

    # K줄에 배추 위치 입력
    for _ in range(K):
        x, y = map(int, input().split())
        plowland[y][x] = 1

    # 탐색
    for row in range(N):
        for col in range(M):
            if plowland[row][col] == 1:
                dfs(plowland, [[row, col]], N, M)
                ans += 1

    print(ans)
    ans = 0
