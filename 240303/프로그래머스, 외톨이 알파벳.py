from collections import defaultdict


def solution(input_string):
    check = defaultdict(int)
    # 첫 글자는 무조건 새로운 글자 이므로 1 추가한다
    check[input_string[0]] += 1
    # 두번째 글자부터 앞의 글자와 비교하여 다른 글자일 경우 1 추가한다
    # 앞의 글자와 다르다면 새로운 글자 덩어리가 시작된거다
    # 이 덩어리의 수가 2 이상이면 외톨이 알파벳이다
    for i in range(1, len(input_string)):
        if input_string[i-1] != input_string[i]:
            check[input_string[i]] += 1
    answer = [x for x, y in check.items() if y > 1]
    if len(answer) == 0:
        answer = 'N'
    else:
        answer = ''.join(sorted(answer))
    return answer

import sys

print(solution(sys.stdin.readline().strip()))
