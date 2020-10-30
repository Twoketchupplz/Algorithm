# 여기선 import sys, readline 을 input으로 지정하면 안됨

N = list(map(int, input()))

length = len(N)
left, right= 0, 0

for i in range(length):
    if i < length/2:
        left += N[i]
    else:
        right += N[i]

if left == right:
    print("LUCKY")
else:
    print("READY")