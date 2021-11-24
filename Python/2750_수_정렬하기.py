"""
https://www.acmicpc.net/problem/2750
1000개 이하 1초이므로 버블정렬을 활용한다.
무조건 n^2 시행하지 않고, 정렬이 완료되는 시점에 bubble_sort 메소드를 종료한다.
이미 정렬된 배열이 입력되는 경우 시간복잡도 = Θ(n)
"""


def bubble_sort(inp_list, size):
    ans = inp_list
    for _ in range(size):
        # 정렬이 완료된 경우 참이 유지되고 메소드를 종료한다.
        solved = True

        for i in range(size-1):
            if ans[i] > ans[i+1]:
                solved = False
                ans[i] = ans[i] ^ ans[i+1]
                ans[i+1] = ans[i+1] ^ ans[i]
                ans[i] = ans[i] ^ ans[i+1]

        if solved:
            return ans
    return ans


num_list = []
N = int(input())
for _ in range(N):
    num = int(input())
    num_list.append(num)

ans_list = bubble_sort(num_list, N)
for element in ans_list:
    print(element)
