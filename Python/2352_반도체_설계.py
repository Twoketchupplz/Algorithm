# https://www.acmicpc.net/problem/2352
# 이분탐색, LIS

# 입력: 정수 n
n = int(input())
# 입력: 1~n 포트와 연결되어야 하는 포트 번호
port = map(int, input().split())

lis = []

# lis에 숫자를 이분탐색을 활용하여 집어넣는다
for num in port:
    if not lis or num >= lis[-1]:
        lis.append(num)
    else:
        start, end = 0, len(lis)-1
        while start < end:
            mid = (start + end)//2
            if num > lis[mid]:
                start = mid + 1
            else:
                end = mid

        lis[end] = num

print(len(lis))
