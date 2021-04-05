"""
https://www.acmicpc.net/problem/12946
offset coordinates 로 표현된 육각 타일에 색이 이웃하지 않게 칠할 때 칠해지는 색의 개수
4색정리: 평면을 유한 개의 부분으로 나누어 각 부분에 색을 칠할 때, 서로 맞닿은 부분을 다른 색으로 칠한다면 네 가지 색으로 충분하다
hex tile 의 경우 최대 3개의 색만 필요하다.
"""

ans = 0


def get_neighbor(cur_node):
    global ans, N, Board
    cnt = 1
    ans = max(1, ans)
    dx = [-1, -1, 0, +1, +1, 0]
    dy = [0, +1, +1, 0, -1, -1]
    for idx in range(-1, 6):  # 중복검사
        x = cur_node[0] + dx[idx]
        y = cur_node[1] + dy[idx]
        if 0 <= x < N and 0 <= y < N and Board[x][y] == 'X':
            # print("카운트된 노드(", x, ",", y, ")")
            cnt += 1
            # print("cnt:", cnt)
            ans = max(cnt, ans)
            # print("ans:", ans)
            if ans == 3:
                return
        else:
            cnt = 1
    return


def color_tile():
    global ans, N, Board
    node_list = []
    for i in range(N):
        for j in range(N):
            if Board[i][j] == 'X':
                node_list.append((i, j))

    for v in node_list:
        if ans != 3:
            get_neighbor(v)

    return ans


N = int(input())
Board = [list(input()) for _ in range(N)]
print(color_tile())
