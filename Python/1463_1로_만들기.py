def make_one(num):
    if num == 1:
        return 0

    dp_list = [0 for _ in range(num + 1)]
    for i in range(2, num + 1):
        min1, min2 = num, num
        if i % 3 == 0:
            min1 = dp_list[i // 3] + 1
        if i % 2 == 0:
            min2 = dp_list[i // 2] + 1
        min3 = dp_list[i - 1] + 1
        dp_list[i] = min(min1, min2, min3) #핵심
    return dp_list[num]


x = int(input())
print(make_one(x))
