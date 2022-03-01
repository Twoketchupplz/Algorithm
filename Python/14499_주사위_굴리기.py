# https://www.acmicpc.net/problem/14499

# 주사위 좌표, 이동명령이 주어졌을 때 주사위가 이동할 때마다 상단에 쓰여있는 값을 구하라
# 주사위 바닥과 지도가 닿으면
# 1. 지도칸에 숫자가 0이면 주사위 바닥면 숫자가 칸에 복사됨
# 2. 0이 아닌 경우 칸에 숫자가 주사위 바닥면에 복사되며 칸의 숫자는 0이됨
# 주사위는 지도 바깥으로 이동하는 명령을 무시하며 출력도 안한다

# 입력1: 지도 크기 세로 N, 가로 M, 주사위좌표 x, y, 명령 수 K
# 입력2: N개 줄로 지도 정보 입력
# 입력3: 명령 1234 == 동서북남
N, M, x, y, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
cmd = list(map(int, input().split()))

''' 풀이
주사위 정보 유지
- 가로 한바퀴로 정보가 이어짐
- 움직이는 방향이 수직으로 전환되면 주사위눈 리스트가 설정되어야함 혹은 그대로 유지 가능?
0 2 0 0     0 2 0 0
4 1 3 0     4 1 3 6
0 5 0 0     0 5 0 0
0 6 0 0     0 0 0 0

0 0 0 0
0 0 0 0
0 0 0 0
0 0 0 0
'''

RollList = [0, 0, 0, 0]
numE, numW, numN, numS = 0, 0, 0, 0
topIdx, btmIdx = 0, 2
# 출력: 이동마다 주사위 윗면에 쓰인 수 출력 newline


def RollDice(d):
    if d == 1:  # east
        print()
    elif d == 2:  # west
        print()
    elif d == 3:  # north
        print()
    else:  # south
        print("sth")
