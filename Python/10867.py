N = int(input())
unsorted_list = input().split()
unsorted_list = list(map(int, unsorted_list))


def quick_sort(prm_list):
    length = len(prm_list)
    if length < 2:
        return prm_list
    lesser = []
    greater = []

    pivot = prm_list.pop(0)

    idx = 0
    for _ in prm_list[:]:

        if prm_list[idx] < pivot:
            lesser.append(prm_list.pop(idx))
        elif prm_list[idx] > pivot:
            greater.append(prm_list.pop(idx))
        else:
            prm_list.pop(idx)
        idx += 1

    lesser = quick_sort(lesser)
    greater = quick_sort(greater)

    lesser.append(pivot)
    ans = lesser + greater

    return ans


print(quick_sort(unsorted_list))
