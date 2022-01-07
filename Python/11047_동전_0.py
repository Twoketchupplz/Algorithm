# https://www.acmicpc.net/problem/11047
# 동전의 종류 N개
# 가치의 합을 K로 만들 때 동전 개수의 최솟값

# 입력: N, K
N, K = map(int, input().split())

# 입력: N개의 줄에 동전의 가치 A(i)가 오름차순으로 주어짐, A(i)는 A(i-1)의 배수, 그리디
coinArr = []
for _ in range(N):
    coinArr.append(int(input()))
coinArr.sort(reverse=True)
cnt = 0

# 가장 큰 동전 부터 차례로 대입한다.
# 동전의 가치가 K원보다 작거나 같은 경우 개수 세기 시작
for coin in coinArr:
    tmp = K // coin
    cnt += tmp
    K -= tmp * coin
    if K == 0:
        break

# 출력 K원을 만드는데 필요한 동전 개수의 최소값
print(cnt)
