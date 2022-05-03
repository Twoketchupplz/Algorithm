# https://www.acmicpc.net/problem/1149

houseNum = int(input())
costInfo = []
ans = []
for _ in range(houseNum):
    costInfo.append(list(map(int, input().split())))

ans.append(costInfo[0])

for house in range(1, houseNum):
    for ansIdx in range(3):
        for costIdx in range(3):
            # ans[house-1]의 ansIdx 중 != costIdx 인 가장 작은 costInfo[house][?] 수를 구해서
            # ans[에 합산한다




# costInfo[i]를 훑으며 누적합을 적어나간다.
