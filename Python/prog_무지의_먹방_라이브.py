def solution(food_times, k):
    idx = 0
    dSize = len(food_times)
    # 문제는 빈접시를 무시하고 다음 접시로 넘어가야 한다.

    # 네트워크 장애 전까지 먹어댄다.
    for second in range(k):
        print(second, "초 접시상황:", food_times)
        # 빈접시를 무시하고 다음 접시로 넘어간다. 모든 접시가 비어있다면 그만해야한다.
        while food_times[idx] == 0:
            print("현재 접시상황 :", food_times)
            dSize -= 1
            if dSize == 0:
                print("네트워크 오류 이전에 모든 접시를 비웠다..")
                return -1
            idx = (idx + 1) % len(food_times)
        dSize = len(food_times)
        food_times[idx] = food_times[idx] - 1
        idx = (idx + 1) % len(food_times)

    # 네트워크가 복구되었다. 다음 먹을 접시는..
    print("네트워크 복구 이후 접시 상황", food_times)
    print("원래 먹어야할 다음 접시는:", idx + 1)
    for _ in range(dSize):
        # 다음 먹을 접시가 있는 경우
        if food_times[idx] != 0:
            return idx + 1  # 1부터 시작하는 인덱스이므로
        else:
            idx = (idx + 1) % dSize
    return -1


food_list = list(map(int, input().split()))
sec = int(input())
print(solution(food_list, sec))
