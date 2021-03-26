"""
https://www.acmicpc.net/problem/1987
알파벳을 중복해서 밟지않고 말이 지나갈 수 있는 칸의 max를 구하시오
visited 좌표를 따로 구하지 않아도 된다. 밟은 알파벳만 기억하면 된다.
set 자료형은 순서를 구분하지 않고 '중복을 허용하지 않는다'.
백트래킹시 route 에 포함했던 문자를 빼낼 필요가 없다.
어차피 구하고자 하는건 가장 긴 route 이기 때문
"""
dRow = [0, 0, -1, 1]
dCol = [1, -1, 0, 0]
ans = 1


def dfs(r, c, board):
    global dRow, dCol, ans

    stack = {(0, 0, board[0][0])}

    while stack:
        row, col, route = stack.pop()
        # 인접노드 탐색
        for i in range(4):
            n_row, n_col = row + dRow[i], col + dCol[i]
            if (0 <= n_row < r) and (0 <= n_col < c) and (board[n_row][n_col] not in route):
                stack.add((n_row, n_col, route + board[n_row][n_col]))
                ans = max(ans, len(route) + 1)

    return ans


R, C = map(int, input().split())
Board = [list(input()) for _ in range(R)]
print(dfs(R, C, Board))
