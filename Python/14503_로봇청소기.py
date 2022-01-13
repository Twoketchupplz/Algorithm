# https://www.acmicpc.net/problem/14503
# 청소하는 영역의 개수를 구하라.
# 청소기 위치 N x M, 지도는 행렬 기준으로 표기한다.
# 청소기는 바라보는 방향이 있다. 동서남북
# 이미 청소한 칸을 청소하지 않는다. 벽을 통과할 수 없다.
# 청소기 시작 위치는 항상 빈 칸이다.

'''
반복문 첫번째 명령문이 이게 맞나
회전후 맨 첫번째 명령인데 r,c에 대하여
'''

# 지도의 크기, 청소기 위치, 바라보는 방향 d(북동남서), 지도 정보 입력
N, M = map(int, input().split())
r, c, d = map(int, input().split())
Area = [list(map(int, input().split())) for _ in range(N)]

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
cnt = 0
rotCnt = 0

while True:
    # 1. 현재 위치 청소; cnt++
    print("현재 위치:", r, c)
    if Area[r][c] == 0:
        Area[r][c] = 2
        cnt += 1
        # r += dr[d]
        # c += dc[d]
        # rotCnt = 0
        print("카운터 증가", cnt)
    if rotCnt != 4:
        # 현재 direction 에서 왼쪽 탐색; 왼쪽으로 회전; rotCnt++
        d -= 1
        n_row, n_col = r + dr[d], c + dc[d]
        leftCell = Area[n_row][n_col]
        rotCnt += 1
        print("leftCell:", n_row, n_col, leftCell)
        if leftCell == 0:
            # 전진; rotCnt = 0
            r, c = n_row, n_col
            rotCnt = 0
    else:  # 네 방향 모두 0이 아님
        if Area[r - dr[d]][c - dc[d]] != 1:
            # 후진; rotCnt = 0;
            r -= dr[d]
            c -= dc[d]
            rotCnt = 0
        else:  # 후진이 불가능
            break

print(cnt)
