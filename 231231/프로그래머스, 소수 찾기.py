# 모범답안
def solution(n):
    answer = set(range(2, n+1))
    for i in range(2, n+1):
        if i in answer:
            answer -= set(range(2*i, n+1, i))
    return len(answer)

def solutions(n):
    answer = 0
    for i in range(2, n+1):
        ck = True
        for j in range(2, int(i**0.5)+1):
            if i%j == 0:
                ck = False
                break
        if ck:
            answer += 1
    return answer

import sys
n = int(sys.stdin.readline())
print(solution(n))