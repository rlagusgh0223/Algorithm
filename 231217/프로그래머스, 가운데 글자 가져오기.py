def solution(s):
    s = list(s)
    if len(s)%2 == 1:
        return s[len(s)//2]
    else:
        return s[(len(s)//2)-1]+s[len(s)//2]


import sys
s = sys.stdin.readline().strip()
print(solution(s))