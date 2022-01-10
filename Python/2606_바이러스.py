# https://www.acmicpc.net/problem/2606

N = int(input())
M = int(input())
graph = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visit = [False]*(N+1)
cnt = 0


def dfs(g, cur, v):
    global cnt
    v[cur] = True
    for i in g[cur]:
        if not v[i]:
            dfs(g, i, v)
            cnt += 1


dfs(graph, 1, visit)
print(cnt)
