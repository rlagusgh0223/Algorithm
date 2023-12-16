def solution(x):
    answer = True
    ck = list(map(int, str(x)))
    if x % sum(ck) != 0:
        answer = False
    return answer


import sys
x = int(sys.stdin.readline())
print(solution(x))