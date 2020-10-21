import sys


def BubbleSort(unsorted, n):
    swap = 0
    for j in range(n - 1):
        for i in range(n - j - 1):
            if unsorted[j] > unsorted[j + i + 1]:
                swap += 1
    return swap


input = sys.stdin.readline

N = int(input())

A = input().split()
A = list(map(int, A))

print(BubbleSort(A, N))


# 시간초과 이중포문을 쓰면 시간초과??