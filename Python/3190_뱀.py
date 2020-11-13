# 넘파이는 쓰면 안되는 거시여따..
import numpy as np

def Dummy(N, apple, plan):
    board = np.zeros((N + 1, N + 1), int)

    for pos in apple:
        board[pos[0], pos[1]] = -1
    board[1, 1] = 1

    plan.append([10001, 'L'])
    plan.reverse()

    return end_time(board, plan)


def end_time(board, route_list):
    ans = 0
    swne = 3  # 시작방향
    cardinal_points = np.array([[1, 0], [0, -1], [-1, 0], [0, 1]])  #Dex++1, Lavo--1
    head = np.array([1, 1])
    snake_size = 1
    pre_time = 0
    while True:
        next_rotate = route_list.pop()
        # 다음 plan 나오는 시간까지 진행방향으로 움직인다
        for second in range(next_rotate[0] - pre_time):
            # 한칸 머리만 내밀어본다
            ans += 1
            head += cardinal_points[swne]
            # 벽?
            if head[0] < 1 or head[0] > N or head[1] < 1 or head[1] > N:
                return ans
            # 몸?
            elif board[head[0]][head[1]] > 0:
                return ans
            # Apple
            elif board[head[0]][head[1]] == -1:
                snake_size += 1
                board[head[0]][head[1]] = snake_size
            # 0 and not wall
            else:
                board = np.where(board > 0, board - 1, board)
                board[head[0]][head[1]] = snake_size

        # Dextro, Lavo
        if next_rotate[1] == 'D':
            swne = (swne + 1) % 4
        else:
            swne = (swne - 1) % 4
        pre_time = next_rotate[0]


N = int(input())
K = int(input())

apple = []
for _ in range(K):
    a_row, a_col = map(int, input().split())
    apple.append([a_row, a_col])
num_rotate = int(input())
route = []
for _ in range(num_rotate):
    sec, direction = input().split()
    sec = int(sec)
    route.append([sec, direction])

print(Dummy(N, apple, route))
