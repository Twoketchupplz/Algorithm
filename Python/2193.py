N = int(input())
pre_ans = 1;
ans = 1;

if N > 2:
    for _ in range(N-2):
        temp = ans
        ans += pre_ans
        pre_ans = temp

print(ans)