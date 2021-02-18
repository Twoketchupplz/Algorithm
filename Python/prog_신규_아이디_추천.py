import copy


def solution(new_id):
    # 1단계: 모든 대문자를 소문자로 치환
    lower_id = new_id.lower()

    # 2단계: 알파벳 소문자, 숫자, 빼기, 밑줄, 마침표를 제외한 모든 문자 제거
    recommend_id = list(lower_id)
    for text in recommend_id[:]:
        if not text.isalpha() and not text.isdigit() and text != '-' and text != '_' and text != '.':
            recommend_id.remove(text)

    # 3단계: 마침표가 두번 연속나온다면 하나의 마침표만 남긴다.
    temp = ''
    deepcopy_list = copy.deepcopy(recommend_id)
    ori_idx = 0
    for copy_idx in range(len(recommend_id)):
        if temp == '.' and deepcopy_list[copy_idx] == '.':
            recommend_id.pop(ori_idx)
        else:
            temp = deepcopy_list[copy_idx]
            ori_idx += 1

    # 4단계: 마침표가 처음이나 마지막에 위치한다면 제거한다.
    if not recommend_id.empty():
        if recommend_id[0] == '.':
            recommend_id.pop(0)
    if recommend_id:
        if recommend_id[-1] == '.':
            recommend_id.pop()

    # 5단계: 빈문자열이라면 "a"를 대입한다.
    if not recommend_id:
        recommend_id.append('a')

    # 6단계: 16자가 넘어간다면 뒤를 자르고 마지막에 점이 있다면 점을 제거한다.
    if len(recommend_id) >= 16:
        for _ in range(len(recommend_id) - 15):
            recommend_id.pop()
        if recommend_id[-1] == '.':
            recommend_id.pop()

    # 7단계: 길이가 2자 이하라면 길이가 3이 될 때까지 마지막 문자를 반복해서 붙입니다.
    if len(recommend_id) <= 2:
        repeat_text = recommend_id[-1]
        while len(recommend_id) < 3:
            recommend_id.append(repeat_text)

    answer = "".join(map(str, recommend_id))
    return answer


print(solution("...!@BaT#*..y.abcdefghijklm"))
