"""
부분수열의 합이 S가 되는 경우의 수를 구하시오. 제한시간 1초
원소가 추가될때 기존의 숫자를 빼던가, 상쇄되는 숫자를 찾아야 한다.

부분수열

아이디어
1~n개의 숫자를 골라 s가 되는 경우의 수를 구한다.
1개~n개를 고르는 경우 : n
s가 되는 구간 찾기 : O(n)

안된다. 연속하지 않은 부분집합도 생각해야한다.

dict{number: cnt}
num1 + num2 == s
  cntOfNum1! * cntOfNum2!
"""


def subsequence(size, s, sequence):
    cnt = 0

    for idx in range(len(sequence) - size + 1):
        _sum = 0
        for j in range(idx, idx + size):
            _sum += sequence[j]
        # print("sum =", _sum)

        if _sum > s:
            break
        elif _sum == s:
            cnt += 1

    return cnt


def solution(n, s, seq):
    ans = 0
    seq.sort()
    num_dict = {}

    for num in seq:
        if num_dict.get(num):
            num_dict[num] += 1
        else:
            num_dict[num] = 1

    print(num_dict)
    print(len(num_dict))


    # 1~n개로 이루어진 부분수열 중에 합이 S인 부분수열 찾기
    for size in range(1, n + 1):
        ans += subsequence(size, s, seq)

    return ans


N, S = map(int, input().split())
Sequence = list(map(int, input().split()))
print(solution(N, S, Sequence))
