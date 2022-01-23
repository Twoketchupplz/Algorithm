# https://www.acmicpc.net/problem/2447
# 가운데 공백을 만들고 주변 8칸에 빈 공간을 만든다.
# 재귀


def makePattern(size):
    global Pattern
    if size == 1:
        return
    else:
        # pSize/3 크기의 공백을 중앙에 생성한다.
        for row in Pattern[size/3:2*size/3]:
            for idx in range[size/3, 2*size/3]:
                row[idx] = ' '

        # 나머지 8 slice 의 중심을 구한다. board[][]에 +- (pSize/3)-1
        # centerList[]
        # 각 중심마다 makePattern(centerIdx, pSize/3)


# N을 입력
N = int(input())

# N by N 크기의 '*'로 채워진 전역변수 생성 Pattern
Pattern = [['*' for _ in range(N)] for _ in range(N)]

# makePattern((N-1)/2,N)

for i in Pattern:
    print()
    for j in i:
        print(j, end='')

