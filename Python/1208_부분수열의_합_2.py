"""
부분수열의 합이 S가 되는 경우의 수를 구하시오. 제한시간 1초
S = 3
-2 -1 0 (1 1 1) 2 3 4
-2 -1 0 1 1 (1 2) 3 4
-2 -1 0 1 1 1 2 (3) 4
(-1 -1 0 1 1 1 2) 3 4
-2 -1 (0 1 1 1) 2 3 4
원소가 추가될때 기존의 숫자를 빼던가, 상쇄되는 숫자를 찾아야 한다.

부분수열
1 (1 1)
(1 1) 1 이 둘은 같은것인가 다른것인가
"""


def solution(n, s, seq):
    ans = 0
    seq.sort()
    # 양수 찾기 왜찾아?
    for idx, val in enumerate(seq):
        if val > 0:
            start_idx = idx


    return ans


N, S = map(int, input().split())
Sequence = list(map(int, input().split()))
solution(N, S, Sequence)