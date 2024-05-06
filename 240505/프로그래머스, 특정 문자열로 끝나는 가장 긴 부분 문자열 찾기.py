def solution(myString, pat):
    end = myString.rfind(pat)
    return myString[:end+len(pat)]

import sys

myString = sys.stdin.readline().strip()
pat = sys.stdin.readline().strip()
print(solution(myString, pat))