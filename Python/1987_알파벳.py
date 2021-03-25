"""
https://www.acmicpc.net/problem/1987
알파벳을 중복해서 밟지않고 말이 지나갈 수 있는 칸의 max를 구하시오
v_lst를 위치로 하지 않고 알파벳단위로 하면된다. 어차피 들린 알파벳은 모두 visited나 마찬가지이기 때문
"""
ans = 1
dRow = [0, 0, -1, 1]
dCol = [1, -1, 0, 0]


def dfs(res, stack, v_lst, route):
    global board, ans, dRow, dCol, R, C

    # 스택의 마지막 원소[row, col]을 꺼낸다.
    row = stack[-1][0]
    col = stack[-1][1]

    res += 1
    ans = max(res, ans)
    v_lst[row][col] = 1
    route.append(board[row][col])
    print(v_lst)

    # 인접노드를 찾아 갈수 있다면 스택에 담는다.
    for i in range(4):
        # 갈 수 있다면 (벽, visited, alp)
        n_row = row + dRow[i]
        n_col = col + dCol[i]
        # if 0 <= n_row < R and 0 <= n_col < C:
        #     if v_lst[n_row][n_col] == 0 and board[n_row][n_col] not in route:
        #         stack.append([n_row, n_col])
        #         dfs(res, stack, v_lst, route)
        #     else:
        #         res -= 1
        #         v_lst[row][col] = 0
        #         print(v_lst)
        #         route.pop()
        #         if stack:
        #             dfs(res, stack, v_lst, route)
        #         else:
        #             return

    #   벽이거나, 이미 들렸거나
    #   이미 나온 알파벳이거나
    # res++, v_lst[][] = 1
    # 루트에 이미 나온 알파벳이면 max를 리턴한다.


def solution(r, c):
    visited = [[0 for _ in range(c)] for _ in range(r)]
    visited[0][0] = 1
    print(visited)
    st = [[0, 0]]
    rt = [board[0][0]]
    dfs(1, st, visited, rt)


R, C = map(int, input().split())
board = [list(map(list, input().split())) for _ in range(R)]
solution(R, C)
