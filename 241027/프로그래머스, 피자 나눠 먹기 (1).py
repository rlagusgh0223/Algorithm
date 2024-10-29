def solution(n):
    return n//7 if n%7==0 else (n//7) + 1
    # return (n-1)//7 + 1  # 모범답안

import sys

print(solution(int(sys.stdin.readline())))
