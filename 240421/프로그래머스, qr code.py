def solution(q, r, code):
    answer = [code[i+r] for i in range(0, len(code), q) if i+r<len(code)]
    return ''.join(answer)

import sys

q, r = map(int, sys.stdin.readline().split())
code = sys.stdin.readline().strip()
print(solution(q, r, code))