# https://www.acmicpc.net/problem/4963
# 8방위로 연결된 섬의 개수를 구하시오
import sys


# 하나의 섬을 파악
def dfs(width, height, board, st):
    cur = st.pop()
    # 방문 == 2
    board[cur[0]][cur[1]] = 2
    for i in range(8):
        n_row = cur[0] + dr[i]
        n_col = cur[1] + dc[i]
        if height > n_row >= 0 and width > n_col >= 0 and board[n_row][n_col] == 1:
            st.append([n_row, n_col])
            dfs(width, height, board, st)


sys.setrecursionlimit(10000)
cnt = 0
# 8방위 동에서 반시계
dr = [0, -1, -1, -1, 0, 1, 1, 1]
dc = [1, 1, 0, -1, -1, -1, 0, 1]

# 테스트 케이스 반복; 0 0 입력시 종료
while True:
    # 지도의 너비와 높이 w, h 입력
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    # h 줄의 지도 입력
    islands = [[int(i) for i in input().split()] for _ in range(h)]

    # islands 지도 탐색
    for row in range(h):
        for col in range(w):
            if islands[row][col] == 1:
                cnt += 1
                dfs(w, h, islands, [[row, col]])

    # 정답 출력
    print(cnt)
    cnt = 0
