# https://www.acmicpc.net/problem/10815
# 함수 내 재귀 호출 앞에 return 키워드를 꼭 붙여야 한다.
# 최종 결과를 가져와도 리턴이 안되기 때문

def binarySearch(target, array, start, end):
    if start > end:
        return 0
    mid = (start + end) // 2
    if target == array[mid]:
        return 1
    elif target > array[mid]:
        return binarySearch(target, array, mid + 1, end)
    elif target < array[mid]:
        return binarySearch(target, array, start, mid - 1)


# 입력: 가지고 있는 숫자 카드 장수
N = int(input())
# 입력: 카드 정보
cardList = list(map(int, input().split()))
cardList.sort()
# 입력: 확인할 카드 장수
M = int(input())
# 입력: 카드 정보
tNumList = list(map(int, input().split()))

for num in tNumList:
    print(binarySearch(num, cardList, 0, N-1), end=' ')
