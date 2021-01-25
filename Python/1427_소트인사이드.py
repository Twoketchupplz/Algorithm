unsorted = list(map(int, list(input())))
list_length = len(unsorted)
ans = 0

for j in range(list_length - 1):
    for i in range(0, list_length - 1 - j):
        num_1 = unsorted[i]
        num_2 = unsorted[i+1]
        if num_1 < num_2:
            num_1 = num_1 ^ num_2
            num_2 = num_1 ^ num_2
            num_1 = num_1 ^ num_2
            unsorted[i] = num_1
            unsorted[i+1] = num_2

for k in range(list_length):
    ans += unsorted[k] * 10**(list_length-1-k)

print(ans)