def solution(myString, pat):
    # 모법답안
    # return int(pat.lower() in myString.lower())
    myString = myString.lower()
    pat = pat.lower()
    if pat in myString:
        return 1
    return 0

import sys

myString = sys.stdin.readline().strip()
pat = sys.stdin.readline().strip()
print(solution(myString, pat))