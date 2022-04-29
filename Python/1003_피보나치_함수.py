# https://www.acmicpc.net/problem/1003
# 다이나믹 프로그래밍

# 입력 케이스 T 횟수만큼
T = int(input())
caseList = []
dpFibo = [[1, 0], [0, 1]]

for _ in range(T):
    caseList.append(int(input()))

for caseNum in caseList:
    if caseNum < 2:
        print(dpFibo[caseNum][0], dpFibo[caseNum][1])
    else:
        cnt = len(dpFibo) - 1
        while cnt < caseNum:
            dpFibo.append([x + y for x, y in zip(dpFibo[cnt - 1], dpFibo[cnt])])
            cnt += 1
        print(dpFibo[caseNum][0], dpFibo[caseNum][1])
