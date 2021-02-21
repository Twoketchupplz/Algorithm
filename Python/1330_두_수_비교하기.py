def compare_two_nums(a: int, b: int):
    if a > b:
        print('>')
    elif a < b:
        print('<')
    else:
        print('==')


A, B = map(int, input().split())
compare_two_nums(A, B)
