def solution(t, p):
    answer = 0
    check = []
    P = len(p)
    p = int(p)
    for i in range(len(t)-P+1):
        check.append(int(t[i:i+P]))
    for c in check:
        if c <= p:
            answer += 1
    return answer

import sys
t = sys.stdin.readline().strip()
p = sys.stdin.readline().strip()
print(solution(t, p))