# https://www.acmicpc.net/problem/1026

N = int(input())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
B.sort(reverse=True)

S = 0
for i in range(N):
    S += A[i]*B[i]

print(S)