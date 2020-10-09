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

    for i in prm_list[:]:

        if i < pivot:
            lesser.append(prm_list.pop(0))
        elif i > pivot:
            greater.append(prm_list.pop(0))
        else:
            prm_list.pop(0)

    lesser = quick_sort(lesser)
    greater = quick_sort(greater)

    lesser.append(pivot)
    ans = lesser + greater

    return ans


print(quick_sort(unsorted_list))
