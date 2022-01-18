# https://www.acmicpc.net/problem/14503
# 청소하는 영역의 개수를 구하라.

# 지도의 크기, 청소기 위치, 바라보는 방향 d(북동남서), 지도 정보 입력
N, M = map(int, input().split())
r, c, d = map(int, input().split())
Area = [list(map(int, input().split())) for _ in range(N)]

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
cnt = 0
rotCnt = 0

while True:
    # 현재 위치를 청소한다
    if Area[r][c] == 0:  # 위치청소; cnt++;
        Area[r][c] = 2
        cnt += 1
        # r += dr[d]
        # c += dc[d]
        rotCnt = 0

    if rotCnt != 4:  # 현재 direction 에서 왼쪽 탐색; 왼쪽으로 회전;
        d = (d - 1) % 4
        n_row, n_col = r + dr[d], c + dc[d]
        leftCell = Area[n_row][n_col]

        if leftCell == 0:  # 전진; rotCnt = 0;
            r, c = n_row, n_col
            rotCnt = 0
        else:  # rotCnt++;
            rotCnt += 1
            continue

    else:  # 네 방향 모두 탐색 완료, 0이 아님. 후진 판단
        if Area[r - dr[d]][c - dc[d]] != 1:
            # 후진; rotCnt = 0;
            r -= dr[d]
            c -= dc[d]
            rotCnt = 0
        else:  # 후진이 불가능
            break

print(cnt)
