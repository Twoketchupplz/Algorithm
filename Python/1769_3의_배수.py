"""
모든 자리수(백만)마다 연산하면 시간초과
첫 연산이후엔 숫자가 커봐야 7자리이므로 첫연산에만 주의한다.
"""
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
