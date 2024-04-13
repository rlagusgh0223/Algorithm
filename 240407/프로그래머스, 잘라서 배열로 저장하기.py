# 모범답안
def solution(my_str, n):
    return [my_str[i:i+n] for i in range(0, len(my_str), n)]

def solutions(my_str, n):
    answer = []
    word = ''
    for i in range(len(my_str)):
        if len(word) == n:
            answer.append(word)
            word = ''
        word += my_str[i]
    if word:
        answer.append(word)
    return answer

import sys

my_str = sys.stdin.readline().strip()
n = int(sys.stdin.readline())
print(solution(my_str, n))