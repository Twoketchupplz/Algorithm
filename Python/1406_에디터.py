"""
시간 제한에 유의한다.
입력을 stdin을 사용해야 한다.
두 개의 스택을 사용해 시간복잡도가 O(1)인 append와 pop()을 사용해야 한다.
"""

from sys import stdin


def editor(sentence, cnt_command):
    left_st = sentence
    right_st = []
    for _ in range(cnt_command):
        command = stdin.readline()
        if command[0] == 'L':
            if left_st:
                right_st.append(left_st.pop())
        elif command[0] == 'D':
            if right_st:
                left_st.append(right_st.pop())
        elif command[0] == 'B':
            if left_st:
                left_st.pop()
        elif command[0] == 'P':
            left_st.append(command[2])

    print("".join(left_st + list(reversed(right_st))))


st = list(stdin.readline().strip())
cnt = int(input())
editor(st, cnt)
