def maxPoint(sticker, N):
    ans = [[0] * N, [0] * N]

    ans[0][0] = sticker[0][0]
    ans[1][0] = sticker[1][0]

    if N == 1:
        return max(ans[0][0], ans[1][0])

    for i in range(1, N):
        if i == 1:
            ans[0][i] = ans[1][0] + sticker[0][i]
            ans[1][i] = ans[0][0] + sticker[1][i]
        else:
            ans[0][i] = max(ans[1][i - 1] + sticker[0][i], ans[1][i - 2] + sticker[0][i])
            ans[1][i] = max(ans[0][i - 1] + sticker[1][i], ans[0][i - 2] + sticker[1][i])

    print(max(ans[0][N - 1], ans[1][N - 1]))

T = int(input())
for t in range(T):
    n = int(input())
    new_sticker = []
    new_sticker.append(list(map(int, input().split())))
    new_sticker.append(list(map(int, input().split())))
    maxPoint(new_sticker, n)

