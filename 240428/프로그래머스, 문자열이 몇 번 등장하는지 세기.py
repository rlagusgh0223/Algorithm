def solution(myString, pat):
    answer = 0
    for i in range(len(myString)):
        if pat in myString[i:i+len(pat)]:
            answer += 1
    return answer

import sys

myString = sys.stdin.readline().strip()
pat = sys.stdin.readline().strip()
print(solution(myString, pat))