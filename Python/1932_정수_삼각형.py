"""
꼭대기 줄부터 아래로 나올 수 있는 가장 큰 합을 적어나간다.
각 줄마다 첫번째 값과 마지막 값은 다른 선택지가 없으므로 각각 이전줄의 처음, 마지막 값과 합한다.
"""


def int_triangle(size, first):
    pre_line = [first]
    for _ in range(size - 1):
        current_line = list(map(int, input().split()))

        current_line[0] += pre_line[0]
        for idx in range(1, len(current_line) - 1):
            current_line[idx] += max(pre_line[idx - 1], pre_line[idx])
        current_line[len(current_line) - 1] += pre_line[len(pre_line) - 1]
        pre_line = current_line
    print(max(current_line))


n = int(input())
fst = int(input())
int_triangle(n, fst)
