def solution(num):
    answer = ''
    if num%2 == 0:
        answer = "Even"
    else:
        answer = "Odd"
    return answer


import sys
num = int(sys.stdin.readline())
print(solution(num))