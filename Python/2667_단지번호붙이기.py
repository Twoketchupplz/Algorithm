# https://www.acmicpc.net/problem/2667


# DFS
def dfs(st):
    global visited, complexSize, dr, dc, N
    cur = st.pop()
    # 현재 노드 방문처리; complexSize++;
    visited[cur[0]][cur[1]] = 2
    complexSize += 1
    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문; 방문하지 않는 노드
    for i in range(4):
        n_row = cur[0] + dr[i]
        n_col = cur[1] + dc[i]
        if N > n_row >= 0 and N > n_col >= 0 and visited[n_row][n_col] == 1:
            st.append([n_row, n_col])
            dfs(st)


dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

# 지도의 크기 N 입력
N = int(input())
# 단지 크기 카운터, 단지 크기 리스트, 단지 개수 카운터, 방문 리스트
complexSize = 0
sizeList = []
complexCnt = 0
visited = []
for row in range(N):
    line = list(map(int, input()))
    visited.append(line)

# 탐색 시작
for row in range(N):
    for col in range(N):
        # 해당 좌표에서 DFS 시작; 단지 수 ++; 단지 크기 입력 및 초기화;
        if visited[row][col] == 1:
            complexCnt += 1
            dfs([[row, col]])
            # dfs 끝난 후 결과 입력; 초기화;
            sizeList.append(complexSize)
            complexSize = 0

# 단지 수 출력
print(complexCnt)
sizeList.sort()
# 단지내 집 수 오름차순 출력
for at in sizeList:
    print(at)
