# https://www.acmicpc.net/problem/11724
# 연결요소의 개수를 구하시오
# 번호와 인덱스 일치시킴

from collections import deque


def bfs(link_info, visited, idx):
    queue = deque()
    queue.append(idx)
    while queue:
        node = queue.pop()
        visited[node] = True
        for v in link_info[node]:
            if not visited[v]:
                queue.append(v)


def countLink(node_num, link_info):
    # default
    ans = 0
    visit = [False for _ in range(node_num + 1)]
    visit[0] = True

    # 간선 정보 인덱스(노드 번호)마다 입력
    linked_list = [[] for _ in range(node_num + 1)]
    for link in link_info:
        linked_list[link[0]].append(link[1])
        linked_list[link[1]].append(link[0])

    for i, isVisited in enumerate(visit):
        if not isVisited:
            ans += 1
            bfs(linked_list, visit, i)

    return ans


# 입력: 정점의 개수 N, 간선의 개수 M
N, M = map(int, input().split())
# M줄 입력: 간선의 양 끝점 a, b
links = []
for _ in range(M):
    a, b = map(int, input().split())
    links.append((a, b))

# 출력
print(countLink(N, links))
