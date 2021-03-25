"""
https://www.acmicpc.net/problem/14888
N개의 숫자가 주어지고 N-1개의 사칙연산자가 주어진다. 각 개수는 입력받는다.
만들 수 있는 식의 결과 Max, min을 구하라.
dfs 백트래킹으로 모든 경우를 따진다. 숫자 하나가 추가될때 마다 남은 사칙연산을 모두 시도하며 들어간다.
Todo Big-O 시간복잡도 계산법
"""


def dfs(n, res, plus_ctr, minus_ctr, multi_ctr, div_ctr):
    global minimum, maximum, N, num_list
    if n == N:
        maximum = max(res, maximum)
        minimum = min(res, minimum)
        return
    else:
        if plus_ctr:
            dfs(n + 1, res + num_list[n], plus_ctr - 1, minus_ctr, multi_ctr, div_ctr)
        if minus_ctr:
            dfs(n + 1, res - num_list[n], plus_ctr, minus_ctr - 1, multi_ctr, div_ctr)
        if multi_ctr:
            dfs(n + 1, res * num_list[n], plus_ctr, minus_ctr, multi_ctr - 1, div_ctr)
        if div_ctr:
            dfs(n + 1, int(res / num_list[n]), plus_ctr, minus_ctr, multi_ctr, div_ctr - 1)


minimum, maximum = 1e9, -1e9
N = int(input())
num_list = list(map(int, input().split()))
plus, minus, multi, div = map(int, input().split())
dfs(1, num_list[0], plus, minus, multi, div)
print(maximum)
print(minimum)
