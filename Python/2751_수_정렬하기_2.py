"""
파이썬으로 병합정렬을 구현하면 백준에서 시간초과가 종종 일어난다.
pypy3로 채점받으면 통과한다.
sys.stdin.readline을 활용하면 시간이 줄어든다. 2148ms to 1472ms
"""

import sys

input = sys.stdin.readline


def merge_sort(arr: list):
    if len(arr) == 1:
        return arr

    # [0 ~ mid], [mid+1 ~ rear]로 나뉨.
    m_idx = len(arr) // 2
    f_arr = merge_sort(arr[:m_idx])
    r_arr = merge_sort(arr[m_idx:])

    return merge(f_arr, r_arr)


def merge(front: list, rear: list):
    merged_arr = []
    f = r = 0

    while f < len(front) and r < len(rear):
        if front[f] < rear[r]:
            merged_arr.append(front[f])
            f += 1
        else:
            merged_arr.append(rear[r])
            r += 1

    # 슬라이싱은 인덱스 범위를 벗어나도 에러를 일으키지 않고 빈 리스트를 반환함
    merged_arr += front[f:]
    merged_arr += rear[r:]

    return merged_arr


whole_list = []
N = int(input())
for _ in range(N):
    whole_list.append(int(input()))

ans = merge_sort(whole_list)
for ele in ans:
    print(ele)
