def solution(s):
    answer = []
    for now in s:
        if now == '(':
            answer.append(now)
        else:
            # 현재 ')'이고 이전에 '('가 입력되지 않았을때
            if len(answer)==0:
                return False
            # 현재 ')'이고 이전에 '('가 입력됐다면 이전에 입력된 '('를 제거
            answer.pop()
    # 문자열이 끝났을땐 모든 괄호가 맞아 다 사라져야 한다
    if len(answer)==0:
        return True
    else:
        return False

import sys
s = sys.stdin.readline().rstrip()
if solution(s):
    print("True")
else:
    print("False")