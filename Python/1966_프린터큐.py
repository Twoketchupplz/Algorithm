# https://www.acmicpc.net/problem/1966
# 동작을 그대로 따라하면서
# 목표 문서의 위치와 인쇄하여 빠진 문서의 개수를 계속 최신화한다.

from collections import deque

Tests = int(input())
for test in range(Tests):
    N, idx = map(int, input().split())
    q = deque(map(int, input().split()))
    cnt = 0
    while True:
        # q에서 앞의 숫자가 가장 큰지 판단한다.
        M = max(q)  # 조건문에서 max()를 사용하면 popleft() 이후 빈 큐일때 에러 발생
        cur = q.popleft()
        if cur == M:  # 가장 크다면 뽑아낸다
            cnt += 1
            if idx == 0:  # 원하는 문서인 경우 프린트
                print(cnt)
                break
            else:  # 원하는 문서가 아니면
                idx -= 1
        else:  # 가장 큰 숫자가 아니라면 뒤로 보낸다
            q.append(cur)
            if idx == 0:
                idx = N - cnt - 1
            else:
                idx -= 1
