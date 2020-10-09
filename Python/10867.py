def quick_sort(prm_list):
    length = len(prm_list)
    if length < 2:
        return prm_list

    lesser = []
    greater = []

    pivot = prm_list.pop()

    for i in range(length - 2, -1, -1):
        if prm_list[i] < pivot:
            lesser.append(prm_list.pop())
        elif prm_list[i] > pivot:
            greater.append(prm_list.pop())
        else:
            prm_list.pop()

    lesser = quick_sort(lesser)
    greater = quick_sort(greater)

    lesser.append(pivot)
    ans = lesser + greater

    return ans


N = int(input())
unsorted_list = input().split()
unsorted_list = list(map(int, unsorted_list))

print(" ".join(map(str, quick_sort(unsorted_list))))
