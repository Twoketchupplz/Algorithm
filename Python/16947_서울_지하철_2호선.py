"""
https://www.acmicpc.net/problem/16947
아이디어
지선을 끝에서부터 잘라내어 사이클을 찾는다.

각노드의 에지 개수를 담은 리스트 edge_cnt 를 만든다. O(n^2)
while 사이클만 남을때 까지:
    edge_cnt[idx]의 val이 1인 idx가 지선의 끝이다. val을 0으로 만든다.
    node[idx]에 연결된 유일한 node v를 찾는다. 윗줄과 함께 O(n^2)
    edge_cnt[v] -= 1
edge_cnt[idx] 중 val이 0이 아닌 idx가 사이클에 해당하는 node이다.

이후 거리는 BFS로 구한다.
포인트는 BFS 시작점이 사이클에 해당하는 노드 중 하나라는 점이다.
"""

import sys

sys.setrecursionlimit(4000)

global edges, N, ans, visited


def search_cycle():
    global ans, visited

    linked_edge_ctr = [0 for _ in range(N + 1)]
    for i in range(N + 1):
        cnt = edges[i].count(1)
        linked_edge_ctr[i] = cnt

    # 사이클만 남을 때까지 지선의 끝 노드를 자르고 그 노드와 연결된 다른 노드의 에지 개수도 줄여준다.
    v_idx = 0
    ctr = 0
    while ctr < N:
        v_idx += 1
        if v_idx > N:
            v_idx = 0
        ctr += 1
        if linked_edge_ctr[v_idx] == 1:
            linked_edge_ctr[v_idx] = 0
            for lnk_v_idx in range(1, N + 1):
                if edges[v_idx][lnk_v_idx] == 1:
                    linked_edge_ctr[lnk_v_idx] = max(0, linked_edge_ctr[lnk_v_idx] - 1)
            ctr = 0

    # 남은 에지가 0이 아닌 노드가 사이클에 포함되는 노드이다.
    ans = [0 for _ in range(N + 1)]
    for v_idx in range(N + 1):
        val = linked_edge_ctr[v_idx]
        if val == 0:
            ans[v_idx] = -1
        else:
            ans[v_idx] = 0

    visited = [0 for _ in range(N + 1)]

    return ans.index(0)


def BFS(cur):
    global ans, visited

    visited[cur] = 1
    for adj in range(1, N + 1):
        if visited[adj] == 0:
            if edges[cur][adj] == 1:
                if ans[adj] == -1:  # 지선인 경우 거리 정보를 담아준다.
                    ans[adj] = ans[cur] + 1
                    BFS(adj)
                elif ans[adj] == 0:  # 사이클인 경우
                    BFS(adj)


def solution():
    BFS(search_cycle())
    ans.pop(0)
    for val in ans:
        print(val, end=" ")


N = int(input())
edges = [[0 for _ in range(N + 1)] for _ in range(N + 1)]
for _ in range(N):
    v1, v2 = map(int, input().split())
    edges[v1][v2] = 1
    edges[v2][v1] = 1
solution()
