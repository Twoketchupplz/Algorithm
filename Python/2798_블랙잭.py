"""
https://www.acmicpc.net/problem/2798
N이 최대 100 이므로 모든 경우를 계산해도 무방함
"""

import sys

input = sys.stdin.readline


def blackjack(cards_list: list, card_num, bj_num: int):
    ans = 0
    cards_list.sort(reverse=True)

    for i in range(card_num-2):
        for j in range(i+1, card_num-1):
            for k in range(j+1, card_num):
                tmp = cards_list[i]+cards_list[j]+cards_list[k]
                if tmp <= bj_num:
                    if tmp >= ans:
                        ans = tmp
                        if ans == bj_num:
                            return ans
                else:
                    pass

    return ans


N, M = map(int, input().split())
cards = list(map(int, input().split()))

print(blackjack(cards, N, M))
