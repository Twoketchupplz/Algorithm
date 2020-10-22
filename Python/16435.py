import sys

def merge(front, rear):
    front_len, rear_len = len(front), len(rear)
    i, j = 0, 0
    merged = []

    # front나 rear 중 하나의 리스트라도 끝까지 사용했으면 멈추고 남은 리스트를 붙인다.
    while i < front_len and j < rear_len:
        if front[i] > rear[j]:
            merged.append(rear[j])
            j += 1
        else:
            merged.append(front[i])
            i += 1
    while i < front_len:
        merged.append(front[i])
        i += 1
    while j < rear_len:
        merged.append(rear[j])
        j += 1

    return merged


def merge_sort(unsorted):
    if len(unsorted) <= 1:
        return unsorted

    # 반으로 가른다.
    mid = len(unsorted) // 2
    front_list = unsorted[:mid]
    rear_list = unsorted[mid:]

    # front, rear list에 각각 재귀
    front_list = merge_sort(front_list)
    rear_list = merge_sort(rear_list)

    # 정렬 결과를 반환한다.
    ans_list = merge(front_list, rear_list)

    return ans_list


def SBIsSoCute(length, unsorted):
    sorted_list = merge_sort(unsorted)
    for h in sorted_list:
        if length >= h:
            length += 1
        else:
            break
    print(length)


input = sys.stdin.readline

N, L = map(int, input().split())

fruits_height = list(map(int, input().split()))

SBIsSoCute(L, fruits_height)