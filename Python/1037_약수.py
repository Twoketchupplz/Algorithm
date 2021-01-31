"""
어떤수 A는 다음과 같이 소인수분해할 수 있다.
A = a^x * b^y * c^z ... (간단하게 a, b, c까지만 표현함) (a < b < c)
여기서 1과 자기자신을 제외한 가장 작은 약수는 a 이고 가장 큰 약수는 a^(x-1) * b^y * c^z 이다.
따라서 약수를 크기 순 정렬한 후 가장 큰 수와 작은 수를 곱하면 A를 구할 수 있다.
"""


def find_number(count, divisors):
    sorted_divisors = sorted(divisors)
    print(sorted_divisors[0] * sorted_divisors[count - 1])


n = int(input())
inp_divs = list(map(int, input().split()))
find_number(n, inp_divs)
