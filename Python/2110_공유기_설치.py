# https://www.acmicpc.net/problem/2110
# 파라메트릭 서치
#   설정 후 조건을 만족하는지 판단, 탐색 범위를 좁혀가며 설정
# 일정거리 d 마다 공유기를 설치하고 공유기 개수를 보고 d의 크기를 조정하여 판단한다.
# 공유기가 너무 많이 설치됐다면 거리를 늘리고, 반대면 좁힌다.
# d만큼 이동했는데 설치할 수 없다면 더 이동한다.
# d는 집 사이 거리 중 최대 최소값의 중간값으로 시작하며, 이분탐색을 활용하여 조정한다.

import sys

input = sys.stdin.readline


def ParametricSearch(houses, r_num):
    ans = 0
    # min, max distance = 집사이 거리의 최소, 최대값
    start, end = 1, houses[-1] - houses[0]

    # 주의: start 와 end 는 같을 수 있다. (start + end) /2 == start == end
    # 다시 말하면 범위가 정확히 하나를 가리키기 때문에 포함해야 한다.
    while start <= end:
        dist = (start + end) // 2
        counter = 1
        last = houses[0]

        for h in houses:
            if h >= last + dist:
                counter += 1
                last = h
        if counter >= r_num:
            ans = dist
            start = dist + 1
        else:
            end = dist - 1

    return ans


# 입력: 집의 개수 N, 공유기 개수 C
N, C = map(int, input().split())
# N줄 입력: 집의 좌표
houseList = [int(input()) for _ in range(N)]
houseList.sort()

# 출력: 가장 인접한 공유기 사이 최대 거리
print(ParametricSearch(houseList, C))
