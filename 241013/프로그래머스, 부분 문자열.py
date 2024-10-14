def solution(str1, str2):
    if str1 in str2:
        return 1
    return 0

import sys

s1 = sys.stdin.readline().strip()
s2 = sys.stdin.readline().strip()
print(solution(s1, s2))