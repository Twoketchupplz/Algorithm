# https://www.acmicpc.net/problem/14499

# 주사위 좌표, 이동명령이 주어졌을 때 주사위가 이동할 때마다 상단에 쓰여있는 값을 구하라
# 주사위 바닥과 지도가 닿으면
# 1. 지도칸에 숫자가 0이면 주사위 바닥면 숫자가 칸에 복사됨
# 2. 0이 아닌 경우 칸에 숫자가 주사위 바닥면에 복사되며 칸의 숫자는 0이됨
# 주사위는 지도 바깥으로 이동하는 명령을 무시하며 출력도 안한다


# 입력1: 지도 크기 행개수 N, 열개수 M, 주사위좌표 행x, 열y, 명령 수 K
# 입력2: N개 줄로 지도 정보 입력
# 입력3: 명령 1234 == 동서북남
N, M, r, c, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
cmdList = list(map(int, input().split()))

RollList = [0, 0, 0, 0]
top, btm, est, wst, sth, nth = 0, 0, 0, 0, 0, 0
# 출력: 이동마다 주사위 윗면에 쓰인 수 출력 newline


def RollDice(d):
    global top, btm, est, wst, sth, nth, N, M, r, c, board
    # 보드에서 갈 수 있는 곳인가? 아니라면 명령을 무시한다
    # 방향이 가로? 세로? 이전과 같은 방향?
    # 같다면 그대로 진행
    # 다르다면 새로운 리스트를 만든다
    if d == 1 and c+1 < M:  # east
        # 주사위 위치, 면 갱신
        c += 1
        tmp = top
        top = wst
        wst = btm
        btm = est
        est = tmp

        # 출력
        print(top)

        # 주사위 바닥면과 지도 갱신
        if board[r][c] == 0:
            board[r][c] = btm
        else:
            btm = board[r][c]
            board[r][c] = 0
    elif d == 2 and c-1 >= 0:  # west
        c -= 1
        tmp = top
        top = est
        est = btm
        btm = wst
        wst = tmp
        print(top)
        if board[r][c] == 0:
            board[r][c] = btm
        else:
            btm = board[r][c]
            board[r][c] = 0
    elif d == 3 and r-1 >= 0:  # north
        r -= 1
        tmp = top
        top = sth
        sth = btm
        btm = nth
        nth = tmp
        print(top)
        if board[r][c] == 0:
            board[r][c] = btm
        else:
            btm = board[r][c]
            board[r][c] = 0
    elif d == 4 and r+1 < N:  # south
        r += 1
        tmp = top
        top = nth
        nth = btm
        btm = sth
        sth = tmp
        print(top)
        if board[r][c] == 0:
            board[r][c] = btm
        else:
            btm = board[r][c]
            board[r][c] = 0


for cmd in cmdList:
    RollDice(cmd)
