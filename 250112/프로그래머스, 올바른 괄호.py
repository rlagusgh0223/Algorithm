def solution(s):
    stack = []
    for now in s:
        if now == '(':
            stack.append(now)
        else:
            if len(stack) == 0:
                return False
            stack.pop()
    return True if len(stack)==0 else False

import sys

print(solution(sys.stdin.readline().strip()))
