"""
https://www.acmicpc.net/problem/11651
y 좌표가 증가하는 순으로, 같으면 x 좌표가 증가하는 순으로
x 기준 정렬후 y 기준 정렬해야 한다.

* reference type data 초기화 주의 *
line 23을 value type 처럼 "front = rear = []"로 하면 같은 주소를 가리키므로 오류 발생
"""

import sys

input = sys.stdin.readline


def quick_sort(arr: list, axis: int):
    size = len(arr)

    # "front, rear"가 빈 리스트 [] 일 수도 있다.
    if size <= 1:
        return arr

    pivot = arr.pop()
    front, rear = [], []

    for coordinate in arr:
        if coordinate[axis] <= pivot[axis]:
            front.append(coordinate)
        else:
            rear.append(coordinate)

    sorted_front = quick_sort(front, axis)
    sorted_rear = quick_sort(rear, axis)

    sorted_front.append(pivot)
    sorted_front.extend(sorted_rear)

    return sorted_front


N = int(input())

coordinate_list = [list(map(int, input().split())) for _ in range(N)]

ans = quick_sort(quick_sort(coordinate_list, 0), 1)
for coor in ans:
    print(coor[0], coor[1])
