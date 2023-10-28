# 그냥 리스트에서 지우고 이어붙이면 시간초과 나온다
# stack을 활용할 것
def solution(s):
    answer = []
    for now in s:
        if len(answer)==0 or answer[-1]!=now:
            answer.append(now)
        else:
            answer.pop()
    if len(answer) == 0:
        return 1
    else:
        return 0

import sys
words = sys.stdin.readline().strip()
print(solution(words))