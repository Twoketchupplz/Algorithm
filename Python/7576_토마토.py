from collections import deque


def tomato(m, n, boxes):
    delta = [[0, 1], [0, -1], [-1, 0], [1, 0]]
    # enqueue initial tomatoes
    location_queue = deque()
    for row in range(n):
        for col in range(m):
            if boxes[row][col] > 0:
                location_queue.append([row, col])

    while location_queue:
        # 모든 인접노드에 대한 검사
        loc = location_queue.popleft()
        cnt = boxes[loc[0]][loc[1]]
        for pnt in delta:
            i = loc[0] + pnt[0]  # row
            j = loc[1] + pnt[1]  # col
            if 0 <= i < n and 0 <= j < m:  # 갈 수 있는 인접 노드인지 확인
                if boxes[i][j] == 0:  # 그리고 그 박스에 방문하지 않은 토마토가 있으면
                    boxes[i][j] += cnt + 1  # 방문한다. 이때
                    location_queue.append([i, j])

    for line in boxes:
        if 0 in line:
            return -1

    return cnt - 1  # cnt를 global 변수로 만들어야 하는가


M, N = map(int, input().split())
tomato_boxes = [list(map(str, input().split())) for _ in range(N)]
print(tomato(M, N, tomato_boxes))
