def solution(str1, str2):
    return 1 if str2 in str1 else 2

import sys

s1 = sys.stdin.readline().strip()
s2 = sys.stdin.readline().strip()
print(solution(s1, s2))