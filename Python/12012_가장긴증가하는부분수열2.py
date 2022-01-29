# https://www.acmicpc.net/problem/12015
# 수열 Ai를 차례로 lis배열에 다음과 같은 조건으로 넣는다
# Ai가 lis[-1]보다 크다면 lis.append(Ai)
# 작거나 같다면 lis 를 이분탐색하여 교체한다.
# 만들어진 lis 의 길이가 LIS의 길이
# lis가 실제 정답에 해당하는 LIS는 아니다.


# 수열 A가 주어졌을 때, 가장 긴 증가하는 부분 수열의 길이를 구하시오

# 입력: 수열 A의 크기 N
N = int(input())
# 입력: 수열 A를 이루고 있는 A(i)
A = list(map(int, input().split()))
lis = []
record = []

for i in A:
    if not lis or i > lis[-1]:
        lis.append(i)
        # record.append(len(lis))

    else:
        start, end = 0, len(lis) - 1
        while start < end:
            mid = (start + end) // 2
            if i > lis[mid]:
                start = mid + 1
            else:
                end = mid
        lis[end] = i  # start, mid, end 어떤게 들어가야 함?
    #     record.append(end+1)
    # print(lis)


print(len(lis))
# # 추출한 배열
# print(lis)
# print()
# # 원본배열과 기록, 실제 LIS 는 record 의 역순으로 순회하며 큰 숫자부터 작은 숫자 순으로 찾으면 된다.
# print(A)
# print(record)
