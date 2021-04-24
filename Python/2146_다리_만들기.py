"""
아이디어
모든 섬마다 고유번호를 준다 BFS or DFS
섬 주변에 해당섬 고유번호를 가진 다리를 두른다.
서로 다른 고유번호를 가진 다리가 만날때 가장 짧은 다리가 만들어진다.

문제점
매번 섬 테두리를 찾아야 하는가. 아니 그렇지 않다. 고유번호를 줌과 동시에 번호를 부여받지 못한 인접노드를 찾는다.
"""


def identify_island(n, land_map):
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]


def solution(n, land):
    identify_island(n, land)
    ans = 0
    return ans


N = int(input())
Land = []
for i in range(N):
    Land.append(list(map(int, input().split())))
solution(N, Land)