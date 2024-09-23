def solution(myString, pat):
    myString = list(myString)
    for i in range(len(myString)):
        if myString[i] == 'A':
            myString[i] = 'B'
        elif myString[i] == 'B':
            myString[i] = 'A'
    myString = ''.join(myString)
    if pat in myString:
        return 1
    return 0

import sys

m = sys.stdin.readline().strip()
p = sys.stdin.readline().strip()
print(solution(m, p))