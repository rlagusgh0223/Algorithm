def solution(k, tangerine):
    # set을 이용하면 시간초과 나온다
    answer = 0
    num = {}
    for t in tangerine:
        if t in num:
            num[t] += 1
        else:
            num[t] = 1
    num = dict(sorted(num.items(), key=lambda x:x[1], reverse=True))
    for n in num:
        k -= num[n]
        answer += 1
        if k <= 0:
            return answer

import sys
k = int(sys.stdin.readline())
t = list(sys.stdin.readline().split())
print(solution(k, t))