N = int(input())
unsorted = input().split()
unsorted = list(map(int, unsorted))
ans = []
ctr = 0

while True:
    idx = 0
    if ctr == N:
        break
    while True:
        if idx == N-1:
            break
        num1 = unsorted[idx]
        num2 = unsorted[idx+1]
        if num1 > num2:
            num1 = num1 ^ num2
            num2 = num1 ^ num2
            num1 = num1 ^ num2
            unsorted[idx] = num1
            unsorted[idx+1] = num2
            idx += 1
        elif num1 == num2:
            unsorted.pop(idx)
            N -= 1
        else :
            idx += 1
    ctr += 1

print(unsorted)