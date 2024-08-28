def solution(s):
    # stack = []
    # for S in s:
    #     if len(stack)==0:
    #         if S == '(':
    #             stack.append(S)
    #         else:
    #             return False
    #     elif stack[-1]=='(' and S==')':
    #         del stack[-1]
    #     else:
    #         stack.append(S)
    # return True if len(stack)==0 else False

    # 모범답안
    # 코드도 이게 적고 속도도 더 빠르다
    stack = []
    for S in s:
        if S == '(':
            stack.append(S)
        else:
            if len(stack) == 0:
                return False
            stack.pop()
    return True if len(stack)==0 else False

import sys

print(solution(sys.stdin.readline().strip()))
