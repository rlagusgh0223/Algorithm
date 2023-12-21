def solution(s):
    answer = sorted(list(s), reverse=True)
    return ''.join(answer)

import sys
s = sys.stdin.readline().strip()
print(solution(s))