import sys
import math

input = sys.stdin.readline

N, M = map(int, input().split())

if N < 2:
    ans = 1
elif N == 2:
    ans = min(4, math.ceil(M/2))
else:
    if M <= 6:
        ans = min(4, M)
    else:
        ans = M-2
print(ans)