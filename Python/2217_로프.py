'''
https://www.acmicpc.net/problem/2217
N개의 로프 중량 w 인 물체
k개의 로프로 w인 물체를 들어올릴때 각 로프마다 w/k의 중량이 걸림
로프 정보가 주어지면 들어올릴 수 있는 물체의 최대 중량을 구하시오
모든 로프를 사용할 필요가 없다.

solution:
로프를 내림차순으로 정렬한다.
가장 무거운 무게 w
사용한 로프 k개 중 가장 약한 로프 w=weak*k
'''

N = int(input())
w = 0
ropeList = [int(input()) for _ in range(N)]
ropeList.sort()
# 전부 다 사용하는 경우부터 가장 약한 로프를 하나씩 빼면서 비교하자
for i in range(N):
    tmp = (N-i) * ropeList[i]
    if tmp > w:
        w = tmp

print(w)