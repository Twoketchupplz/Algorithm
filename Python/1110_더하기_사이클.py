# https://www.acmicpc.net/problem/1110


def cycle(ori: int, pre: int):
    global cnt
    cnt += 1
    post = 0
    # 숫자를 자리수 별로 나눈다
    digit = [pre // 10, pre % 10]

    # 10의자리 만들기
    post += 10 * digit[1]
    # 1의자리 만들기
    post += sum(digit) % 10
    # ori와 같은지 비교한다
    if ori == post:
        return

    else:
        cycle(ori, post)


N = int(input())
cnt = 0
cycle(N, N)
print(cnt)
