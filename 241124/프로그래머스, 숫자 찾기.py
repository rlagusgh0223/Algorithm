def solution(num, k):
    num = list(map(int, str(num)))
    if k in num:
        return num.index(k)+1
    return -1

import sys

num, k = map(int, sys.stdin.readline().split())
print(solution(num, k))