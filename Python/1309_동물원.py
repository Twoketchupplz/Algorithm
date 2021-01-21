# 점화식을 사용한다. A(n) = A(n-1)*2 + A(n-2)
def lion_cage(num):
    a0 = 1
    a1 = 3
    if num == 1:
        return a1
    else:
        for _ in range(1, n):
            ans = (a1 * 2) + a0
            a0 = a1
            a1 = ans
        return ans % 9901


n = int(input())
print(lion_cage(n))
