def solution(goal, num_list):
    ans = 0
    seq_sum = num_list[0]
    length = len(num_list)
    head, tail = 0, 0

    # 마지막에 tail이 head를 넘어서거나, head가 마지막에 도달하여 더 이상 볼 필요가 없는경우 종료된다.
    while tail <= head < length:
        if seq_sum < goal:
            head += 1
            if head < length:
                seq_sum += num_list[head]

        elif seq_sum > goal:
            seq_sum -= num_list[tail]
            tail += 1
            if head < tail < len(num_list):
                head = tail
                seq_sum = num_list[tail]

        else:
            ans += 1
            head += 1
            if head < length:
                seq_sum += num_list[head]

    return ans


N, M = map(int, input().split())
A = list(map(int, input().split()))
print(solution(M, A))
