import sys

input = sys.stdin.readline

N, L, R = map(int, input().split())


def bfs(n, left, right):
    population = [list(map(int, input().split())) for _ in range(n)]
    x = [0, 1, 0, -1]
    y = [-1, 0, 1, 0]
    day = 0

    # 더이상 day 가 늘어나지 않을 때까지 찾는다. 이부분이 미지수 Z
    while True:
        visited = [list(False for _ in range(n)) for _ in range(n)]
        move = False
        next_nation = [0, 0]
        counter = 0

        # 하루동안 인구 변화 O()
        while True:
            uni_pos = []
            uni_q = [[next_nation[0], next_nation[1]]]
            uni_pos.append([next_nation[0], next_nation[1]])
            num_nation = 1

            # union을 bfs로 찾는다. O(N)
            while uni_q:
                current = uni_q.pop(0)
                visited[current[0]][current[1]] = True
                counter += 1

                # 사방을 조사한다. O(4)
                for i in range(4):
                    next_row = current[0] + x[i]
                    next_col = current[1] + y[i]
                    if 0 <= next_row < n \
                            and 0 <= next_col < n \
                            and not visited[next_row][next_col] \
                            and left <= abs(
                        population[current[0]][current[1]] - population[next_row][next_col]) <= right:
                        uni_q.append([next_row, next_col])
                        visited[next_row][next_col] = True
                        uni_pos.append([next_row, next_col])
                        num_nation += 1

            # union간 인구이동이 발생시 이동시킨다. 이때 이동이 있었음을 감지할 수 있다.
            if num_nation > 1:
                move = True
                uni_population = 0
                for nation in uni_pos:
                    uni_population += population[nation[0]][nation[1]]
                each_population = int(uni_population / num_nation)
                for nation in uni_pos:
                    population[nation[0]][nation[1]] = each_population

            # 다음 시작 nation을 찾는다.
            for j in range(n):
                for i in range(n):
                    if not visited[i][j]:
                        next_nation = [i, j]

            if counter == n*n:
                break

        if move:
            day += 1
        else:
            break
    print(day)


bfs(N, L, R)
