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

for i in A:
    if not lis or i > lis[-1]:
        lis.append(i)

    else:
        start, end = 0, len(lis)-1
        while start <= end:
            mid = (start + end) // 2
            if i < lis[mid]:
                end = mid-1
            elif i > lis[mid]:
                start = mid+1
            else:
                break
        lis[mid] = i

print(len(lis))
# 출력: 가장 긴 증가하는 부분 수열의 길이

