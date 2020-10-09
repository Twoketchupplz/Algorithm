N = int(input())
unsorted = input().split()
unsorted = list(map(int, unsorted))
ctr = N-1
idx = 0

#버블소트 도중 중복된 쌍이 있으면 제거한다. 버블소트를 써서 느린듯..
while True:
    #탐색횟수를 모두 소모하면 종료한다.
    if ctr == 0:
        break

    num1 = unsorted[idx]
    num2 = unsorted[idx + 1]

    # 오름차순으로 스위치
    if num1 > num2:
        num1 = num1 ^ num2
        num2 = num1 ^ num2
        num1 = num1 ^ num2
        unsorted[idx] = num1
        unsorted[idx + 1] = num2
        idx += 1

    #같은 숫자가 나오면 제거하고, 전체길이와 탐색 횟수를 줄인다.
    elif num1 == num2:
        unsorted.pop(idx)
        N -= 1
        ctr -= 1
    # 오름차순이면 이미 넘어간다.
    elif num1 < num2:
        idx += 1

    # 남은 리스트의 끝까지 탐색한경우 idx를 처음으로 돌린다. 탐색횟수를 소모한다.
    if idx == N-1:
        idx = 0
        ctr -= 1

print(unsorted)
