import sys

T = int(input())
for _ in range(T):
    N = int(input())
    cnt = 1
    applicants = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
    applicants.sort(key=lambda x: x[0])
    best = applicants.pop(0)
    for i in applicants:
        temp = i
        if best[1] > temp[1]:
            best = temp
            cnt += 1
        if not applicants:
            break
    print(cnt)
