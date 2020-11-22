import copy


def safety_zone(n, m, lab):
    virus = []
    void = 0
    lab_copy = copy.deepcopy(lab)
    # 감염지역 마킹,
    for i in range(n):
        for j in range(m):
            if lab[i][j] == 2:
                virus.append([i, j])
            elif lab[i][j] == 0:
                void += 1
    min_contamination = void
    # 3개의 벽을 세우는 모든 경우의 수에 대해 contamination BFS를 진행한다.
    for i in range(n * m - 2):
        x1 = i // m
        y1 = i % m
        if lab_copy[x1][y1] == 0:
            for j in range(i + 1, n * m - 1):
                x2 = j // m
                y2 = j % m
                if lab_copy[x2][y2] == 0:
                    for k in range(j + 1, n * m):
                        x3 = k // m
                        y3 = k % m
                        lab_copy[x1][y1] = 1
                        lab_copy[x2][y2] = 1
                        lab_copy[x3][y3] = 1
                        temp = bfs(n, m, lab_copy, copy.deepcopy(virus))
                        if temp < min_contamination:
                            min_contamination = temp
                        lab_copy = copy.deepcopy(lab)
    # 빈공간 - 감염공간 - 추가된 벽
    return void - min_contamination - 3


def bfs(n, m, lab, v_queue):
    contaminated_area = 0
    while v_queue:
        node = v_queue.pop(0)
        # 4방 확산
        if node[1] > 0 and lab[node[0]][node[1] - 1] == 0:
            lab[node[0]][node[1] - 1] = 2
            v_queue.append([node[0], node[1] - 1])
            contaminated_area += 1
        if node[1] < m - 1 and lab[node[0]][node[1] + 1] == 0:
            lab[node[0]][node[1] + 1] = 2
            v_queue.append([node[0], node[1] + 1])
            contaminated_area += 1
        if node[0] > 0 and lab[node[0] - 1][node[1]] == 0:
            lab[node[0] - 1][node[1]] = 2
            v_queue.append([node[0] - 1, node[1]])
            contaminated_area += 1
        if node[0] < n - 1 and lab[node[0] + 1][node[1]] == 0:
            lab[node[0] + 1][node[1]] = 2
            v_queue.append([node[0] + 1, node[1]])
            contaminated_area += 1

    return contaminated_area


N, M = map(int, input().split())

laboratory = [list(map(int, input().split())) for _ in range(N)]

print(safety_zone(N, M, laboratory))
