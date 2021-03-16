def tomato(m, n, warehouse):
    # 인접확인은 +-1로 확인한다. 여기서 row col이 0보다 작거나 각각 n, m보다 크거나 같으면 아웃라인
    #
    # 들어온 모든 리스트의 visited를 False한다.

    # 시작지점을 찾는다. visited True
    # 시작지점을 큐에 넣는다.
    # while (Q != null):
    #     u = deque(Q)
    #     init L(u)
    #     for each v in L(u):
    #         if (not visited[v]):
    #             visited[v] = True
    #             enqueue(Q, v)

    return 0


M, N = map(int, input().split())
tomato_warehouse = [list(map(int, input().split())) for _ in range(N)]
print(tomato(M, N, tomato_warehouse))
