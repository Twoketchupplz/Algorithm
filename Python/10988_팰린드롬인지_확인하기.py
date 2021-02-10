"""
시간을 단축하기 위해 pop()과 append 연산을 활용한다.
"""


def check_pal(char_list):
    size = len(char_list)
    comparative_list = []
    for _ in range(size // 2):
        comparative_list.append(char_list.pop())
    if size % 2 == 1:
        char_list.pop()
    if comparative_list != char_list:
        print(0)
    else:
        print(1)


word = list(input())
check_pal(word)
