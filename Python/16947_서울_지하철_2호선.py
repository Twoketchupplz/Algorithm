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
"""

from collections import deque

global edges, N


def search_cycle():
    # 각노드의 에지 개수를 담은 리스트 edge_cnt 를 만든다. O(n^2)
    linked_edge_ctr = [0 for _ in range(N + 1)]
    for i in range(N + 1):
        cnt = edges[i].count(1)
        linked_edge_ctr[i] = cnt
    # print(edges)
    # print(e_cnt)

    # 사이클만 남을 때까지 아래를 반복한다.
    v_idx = 0
    ctr = 0
    # deleted = [0 for _ in range(N+1)]
    while ctr < N:
        v_idx += 1
        if v_idx > N:
            v_idx = 0
        ctr += 1
        # print("idx", idx)
        # edge_cnt[idx]의 val이 1인 idx가 지선의 마지막 노드이다. val을 0으로 만든다.
        if linked_edge_ctr[v_idx] == 1:
            # deleted[v_idx] = 1
            linked_edge_ctr[v_idx] = 0
            # 마지막 노드와 연결된 살아있는 유일한 node v를 찾는다.
            for lnk_v_idx in range(1, N+1):
                if edges[v_idx][lnk_v_idx] == 1:
                    # linked_edge_ctr[lnk_v_idx] -= 1
                    linked_edge_ctr[lnk_v_idx] = max(0, linked_edge_ctr[lnk_v_idx] - 1)
            ctr = 0
            # print("edge counter")
        # print("idx, e")
        # print(idx, e_cnt)

    # 남은 에지가 0이 아닌 노드가 사이클에 포함되는 노드이다.
    # print(e_cnt)
    ans = [0 for _ in range(N + 1)]
    for v_idx, val in enumerate(linked_edge_ctr):
        if val == 0:
            ans[v_idx] = -1
        else:
            ans[v_idx] = 0
    # print("ans", ans)
    return ans


def BFS(cycle_nodes):
    ans = cycle_nodes
    # 노드마다 하나씩 순회한다.
    for start, is_cycle in enumerate(cycle_nodes):
        # 사이클이면 시작하지 않는다. 0이 사이클임을 의미
        if start == 0 or is_cycle == 0:
            continue
        # 노드가 지선이면 탐색을 시작한다 사이클을 만날때까지
        else:
            # print("--- start node num :", start)
            queue = deque()
            distance = [-1 for _ in range(N + 1)]
            queue.append(start)
            distance[start] = 0
            got_ans = False
            # 하나의 노드로부터 사이클까지의 거리 찾기 시작
            while queue and not got_ans:
                cur = queue.popleft()
                # print("current node:", cur)
                dist = distance[cur]
                for lnk_node in range(1, N + 1):
                    if edges[cur][lnk_node] == 1 and distance[lnk_node] == -1:
                        if cycle_nodes[lnk_node] == 0:  # 사이클에 닿으면
                            ans[start] = dist + 1
                            # print("got ans, distances: ", distance)
                            got_ans = True
                            break
                        distance[lnk_node] = dist + 1
                        # print("distances:", distance)
                        queue.append(lnk_node)
                # print("current queue:", queue)
        # print("ans of a node", ans)
    return ans


def solution(ans):
    ans.pop(0)
    for val in ans:
        print(val, end=" ")


N = int(input())
edges = [[0 for _ in range(N + 1)] for _ in range(N + 1)]
for _ in range(N):
    v1, v2 = map(int, input().split())
    edges[v1][v2] = 1
    edges[v2][v1] = 1
solution(BFS(search_cycle()))
