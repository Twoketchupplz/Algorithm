N = int(input())
move = 1
for _ in range(N - 1):
    move = move * 2 + 1
print(move)


def Hanoi(N, preTop, postTop, dest):
    if N == 1:
        print(preTop, dest)
        return
    else:
        Hanoi(N - 1, preTop, dest, postTop)
        print(preTop, dest)
        Hanoi(N - 1, postTop, preTop, dest)


Hanoi(N, 1, 2, 3)
