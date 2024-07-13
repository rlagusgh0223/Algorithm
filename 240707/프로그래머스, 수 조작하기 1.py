def solution(n, control):
    for c in control:
        if c == 'w':
            n += 1
        elif c == 's':
            n -= 1
        elif c == 'd':
            n += 10
        else:
            n -= 10
    return n

import sys

n = int(sys.stdin.readline())
control = sys.stdin.readline().strip()
print(solution(n, control))