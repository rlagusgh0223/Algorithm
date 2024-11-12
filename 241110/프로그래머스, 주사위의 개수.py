def solution(box, n):
    answer = (box[0]//n) * (box[1]//n) * (box[2]//n)
    return answer

import sys

b = list(map(int, sys.stdin.readline().split(", ")))
n = int(sys.stdin.readline())
print(solution(b, n))