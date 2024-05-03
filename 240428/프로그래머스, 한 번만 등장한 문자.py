# 모범답안
def solution(s):
    answer = ''.join(sorted(w for w in s if s.count(w)==1))
    return answer

def solutions(s):
    answer = [0] * 26
    result = ''
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    for i in s:
        answer[alpha.index(i)] += 1
    for i in range(len(answer)):
        if answer[i] == 1:
            result += alpha[i]
    if result:
        return result
    return []

import sys

print(solution(sys.stdin.readline().strip()))
