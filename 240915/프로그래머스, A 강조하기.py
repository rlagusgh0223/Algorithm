def solution(myString):
    answer = ''
    for i in range(len(myString)):
        if myString[i]=='a' or myString[i]=='A':
            answer += myString[i].upper()
        else:
            answer += myString[i].lower()
    return answer

import sys

print(solution(sys.stdin.readline().strip()))
