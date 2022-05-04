# https://www.acmicpc.net/problem/1305
# Failure Function 실패함수, KMP Algorithm

# 광고문구가 연속적으로 반복하는데 광고판의 크기는 한정되어있음
# 광고판을 보고 가능한 광고 문구중 가장 짧은 것의 길이를 출력한다

# 이유를 모르겠네
# L에서 조건 prefix == suffix을 만족하는 가장 긴 길이를 뺀 값을 출력한다.

# 시간초과: 2초, N < 1,000,000
# O(N^2) == 10000초, NlogN 해야 0.06초
import sys
input = sys.stdin.readline


def solution(size: int, text: str):
    cnt = 0
    maxi = 0
    for i in range(1, size):
        for pre, suf in zip(text[:i], text[size-i:]):
            if pre == suf:
                cnt += 1
            else:
                cnt = 0
                break
        maxi = max(maxi, cnt)
        cnt = 0

    return size - maxi


print(solution(int(input()), input().rstrip()))
