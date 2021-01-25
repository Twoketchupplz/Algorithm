import sys

ctr = 0


def merge(front, rear):
    front_len, rear_len = len(front), len(rear)
    i, j = 0, 0
    global ctr
    merged = []
    while i < front_len and j < rear_len:
        if front[i] > rear[j]:
            # Swap 횟수를 센다. front에 있는 rear[j]보다 큰 수의 개수만큼씩 더해진다.
            merged.append(rear[j])
            j += 1
            ctr += front_len - i
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


input = sys.stdin.readline

N = int(input())

A = input().split()
A = list(map(int, A))

merge_sort(A)
print(ctr)
