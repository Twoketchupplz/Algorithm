# https://www.acmicpc.net/problem/4256
# preorder의 맨앞이 root이다.
# 구한 루트로 inorder에서 left right 나누기
# 위에 구한 left right 사이즈로 preorder left right 나누기

# 후위순회 알고리즘 순서대로 프로그래밍 한다.
# if left != null 재귀 left
# if right != null 재귀 right
# left == null and right == null root인 v를 출력한다.

global preorder_list, inorder_list


def postorder(rt_idx, head, tail):  # init: rt = 0, head = 0 tail = sizeofList
    global preorder_list, inorder_list

    for idx in range(head, tail):
        if preorder_list[rt_idx] == inorder_list[idx]:
            postorder(rt_idx + 1, head, idx)
            postorder(rt_idx + idx + 1 - head, idx + 1, tail)
            print(preorder_list[rt_idx], end=" ")


T = int(input())
for _ in range(T):
    N = int(input())
    preorder_list = list(map(int, input().split()))
    inorder_list = list(map(int, input().split()))
    postorder(0, 0, N)
    print()
