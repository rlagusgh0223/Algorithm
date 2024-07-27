from collections import defaultdict


def solution(input_string):
    answer = 'N'  # 외톨이 알파벳을 알파벳순으로 출력할 문자열
    check = defaultdict(int)  # 알파벳 덩어리가 몇 개인지 기록할 딕셔너리
    # 처음 알파벳은 무조건 새로운 알파벳이므로 1로 시작한다
    check[input_string[0]] += 1

    # 앞의 단어와 다를 경우 알파벳 덩어리의 갯수를 하나 추가한다
    for i in range(1, len(input_string)):
        if input_string[i-1] != input_string[i]:
            check[input_string[i]] += 1

    # 알파벳 덩어리가 2번 이상 나온 알파벳만 word에 입력
    word = [key for key, value in check.items() if value>1]

    # 외톨이 알파벳이 하나라도 있다면 알파벳순으로 정렬해서
    # 하나의 문자열로 만든다
    if len(word) > 0:
        answer = ''.join(sorted(word))
    
    return answer

import sys

print(solution(sys.stdin.readline().strip()))
