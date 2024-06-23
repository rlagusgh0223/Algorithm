def solution(a, b, flag):
    return a+b if flag==True else a-b

import sys

a, b = map(int, sys.stdin.readline().split())
flag = sys.stdin.readline().strip()
print(solution(a, b, flag))