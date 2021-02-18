import copy


def solution(new_id):
    lower_id = new_id.lower()
    recommend_id = list(lower_id)
    for text in recommend_id[:]:
        if not text.isalpha() and not text.isdigit() and text != '-' and text != '_' and text != '.':
            recommend_id.remove(text)
    temp = ''
    deepcopy_list = copy.deepcopy(recommend_id)
    ori_idx = 0
    for copy_idx in range(len(recommend_id)):
        if temp == '.' and deepcopy_list[copy_idx] == '.':
            recommend_id.pop(ori_idx)
        else:
            temp = deepcopy_list[copy_idx]
            ori_idx += 1
    if recommend_id:
        if recommend_id[0] == '.':
            recommend_id.pop(0)
    if recommend_id:
        if recommend_id[-1] == '.':
            recommend_id.pop()
    if not recommend_id:
        recommend_id.append('a')
    if len(recommend_id) >= 16:
        for _ in range(len(recommend_id) - 15):
            recommend_id.pop()
        while True:
            if recommend_id[-1] == '.':
                recommend_id.pop()
            else:
                break
    if len(recommend_id) <= 2:
        repeat_text = recommend_id[-1]
        while len(recommend_id) < 3:
            recommend_id.append(repeat_text)

    answer = "".join(map(str, recommend_id))
    return answer


print(solution("...!@BaT#*..y.abcdefghijklm"))
