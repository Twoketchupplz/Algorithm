'''
파이썬의 int 타입에서 허용하는 범위를 넘어서는 입력이 들어왔을 때 오버플로우 문제가 발생하는 듯하여 맨 처음에만 입력된 숫자를 바로 정수로 바꾸지 않고 그대로 리스트에 넣었다.
입력될 수 있는 가장 큰 숫자 999...99(백만자리)이므로 다음 연산부터는 int 그대로 계산한다.
(하지만 실제로 백만자리가 넘는 숫자를 넣어봤는데 계산이 잘된다..)
'''
def multiples(num_in_char):
    cnt = 0
    char_list = []
    converted_num = 0

    # 숫자가 1자리인 경우 input 값을 바로 int로 변환해도 된다.
    if len(num_in_char) == 1:
        converted_num = int(num_in_char)
        print(cnt)
    else:
        # 처음에만 문자 그대로 리스트에 담는다.
        for i in str(num_in_char):
            char_list.append(i)
        for j in char_list:
            converted_num += int(j)
        cnt += 1

        while converted_num >= 10:
            int_list = []
            while converted_num != 0:
                int_list.append(converted_num % 10)
                converted_num = converted_num // 10
            for k in int_list:
                converted_num += k
            cnt += 1
        print(cnt)

    if converted_num % 3 == 0:
        print("YES")
    else:
        print("NO")


X = input()
multiples(X)
