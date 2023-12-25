def solution(n):
    answer = 0
    three = []
    while n>0:
        three.append(n%3)
        n //= 3
    for t in three:
        answer = answer*3 + int(t)
    return answer


import sys
n = int(sys.stdin.readline())
print(solution(n))