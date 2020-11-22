def Dummy():
    N = int(input())
    K = int(input())

    board = [[0] * (N + 1) for _ in range(N + 1)]
    board[1][1] = 1

    apple = []
    for _ in range(K):
        a_row, a_col = list(map(int, input().split()))
        apple.append([a_row, a_col])
    num_rotate = int(input())
    for pos in apple:
        board[pos[0]][pos[1]] = 2

    route = []
    for _ in range(num_rotate):
        sec, direction = input().split()
        route.append([int(sec), direction])
    route.append([10001, 'L'])

    return end_time(N, board, route)


def end_time(n, board, route_list):
    ans = 0
    swne = 3  # 시작방향
    cardinal_points = [[1, 0], [0, -1], [-1, 0], [0, 1]]  # Dex++1, Lavo--1 남서북동
    head = [1, 1]
    tail = list()
    pre_time = 0
    while True:
        next_rotate = route_list.pop(0)
        # 다음 plan 나오는 시간까지 진행방향으로 움직인다
        for second in range(next_rotate[0] - pre_time):
            # 한칸 머리만 내밀어본다
            ans += 1
            tail.append([head[0], head[1]])
            head[0] += cardinal_points[swne][0]
            head[1] += cardinal_points[swne][1]
            # 벽?
            if head[0] < 1 or head[0] > n or head[1] < 1 or head[1] > n:
                return ans
            # 몸?
            elif board[head[0]][head[1]] == 1:
                return ans
            # Apple
            elif board[head[0]][head[1]] == 2:
                board[head[0]][head[1]] = 1
            # 0 and not wall
            else:
                temp1, temp2 = tail.pop(0)
                board[temp1][temp2] = 0
                board[head[0]][head[1]] = 1

        # Dextro, Lavo
        if next_rotate[1] == "D":
            swne = (swne + 1) % 4
        else:
            swne = (swne - 1) % 4
        pre_time = next_rotate[0]


print(Dummy())
