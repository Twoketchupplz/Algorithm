T = int(input())
ans = []

for _ in range(T):
    N, M = map(int, input().split())
    if N < 12 or M < 4:
        ans.append(-1)
    else :
        ans.append(11*M + 4)

for i in ans:
    print(i)