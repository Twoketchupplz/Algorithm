"""
https://www.acmicpc.net/problem/11399
index 0 은 사용하지 않는다
"""

import sys

input = sys.stdin.readline

global heap, size


def build_heap(k_idx: int):
    global heap
    if k_idx == 1:  # 루트에 도달
        return
    elif heap[k_idx] >= heap[k_idx // 2]:  # 부모보다 자식이 큼
        return
    else:  # 부모보다 자식이 작음
        parent_idx = k_idx // 2
        heap[k_idx], heap[parent_idx] = heap[parent_idx], heap[k_idx]
        build_heap(parent_idx)
        return


def heapify(p_idx, size_left):
    global heap
    left = 2 * p_idx
    right = 2 * p_idx + 1
    if right <= size_left:
        if heap[left] <= heap[right]:
            smaller_c = left
        else:
            smaller_c = right
    elif left <= size_left:
        smaller_c = left
    else:  # parent가 리프노드
        return
    if heap[smaller_c] < heap[p_idx]:
        heap[p_idx], heap[smaller_c] = heap[smaller_c], heap[p_idx]
        heapify(smaller_c, size_left)


def ascd_order():
    global heap
    for idx in range(size - 1, 0, -1):
        heap[1], heap[idx] = heap[idx], heap[1]
        heapify(1, idx-1)


def heap_sort():
    global heap
    for it in range(1, size):
        build_heap(it)
    ascd_order()
    return


N = int(input())
size = N + 1
heap = [0] + list(map(int, input().split()))
heap_sort()
ans = 0
for i in range(1, N + 1):
    ans += heap[i] * i

print(ans)
