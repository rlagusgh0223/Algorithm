def solution(my_string):
    answer = [0] * 52
    for s in my_string:
        if s.isupper():
            # A : 65
            answer[ord(s)-65] += 1
        else:
            # a : 97
            # 97에서 71을 빼야 26번째 순서부터 시작한다
            answer[ord(s)-71] += 1
    return answer

def solutions(my_string):
    answer = [0] * 52
    word = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    for s in my_string:
        i = word.index(s)
        answer[i] += 1
    return answer

import sys

print(solution(sys.stdin.readline().strip()))
