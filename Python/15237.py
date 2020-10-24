import sys


def merge(front, rear):
    front_len, rear_len = len(front), len(rear)
    i, j = 0, 0
    merged = []

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

    mid = len(unsorted) // 2
    front_list = unsorted[:mid]
    rear_list = unsorted[mid:]

    front_list = merge_sort(front_list)
    rear_list = merge_sort(rear_list)

    ans_list = merge(front_list, rear_list)

    return ans_list


def freq_sort(unsorted, n):
    # [ [숫자, 개수], [숫자, 개수] ]
    # key = lambda message: message[1], message[0]
    merged = merge_sort(unsorted)
    count = [0]  # index마다 해당 박스의 개수가 담김
    merged_box = [[]]  # 작은 수부터 박스를 만든다.
    box_i = 0
    # 맨처음과 비교해야하므로 자기자신과 비교부터 시작한다.
    pre_i = merged[0]
    for i in merged:
        if i == pre_i:
            merged_box[box_i].append(i)
            count[box_i] += 1
        else:
            merged_box.append([i])
            count.append(0)
            box_i += 1
            pre_i = i

    sorted_by_freq = sorted(merged_box, key=lambda box_info: (-len(box_info), -box_info[0]))
    for i in sorted_by_freq:
        for j in i:
            print(j, end=' ')


input = sys.stdin.readline

N, C = map(int, input().split())
integers = list(map(int, input().split()))

freq_sort(integers, N)