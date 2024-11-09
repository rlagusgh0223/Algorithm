def solution(age):
    answer = ''
    age = str(age)
    for a in age:
        answer += chr(ord('a') + int(a))
    return answer

import sys

print(solution(int(sys.stdin.readline())))
