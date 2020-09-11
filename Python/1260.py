N, M, V = map(int, input().split())
edge = []
visited_D = []
visited_B = []

for i in range(N + 1):
    edge.append([])
    visited_D.append(0)
    visited_B.append(0)
visited_D[0] = 1

for _ in range(M):
    e1, e2 = map(int, input().split())
    edge[e1].append(e2)
    edge[e2].append(e1)

for i in range(N):
    edge[i + 1].sort()


def DFS(v):
    print(v, end=" ")
    visited_D[v] = 1
    for linked_node in edge[v]:
        if visited_D[linked_node] == 0:
            DFS(linked_node)


def BFS(v):
    queue = [v]
    visited_B[v] = 1
    while queue:
        for linked_v in edge[queue[0]]:
            if visited_B[linked_v] == 0:
                queue.append(linked_v)
                visited_B[linked_v] = 1
        print(queue.pop(0), end=" ")


DFS(V)
print()
BFS(V)
