def solution(s):
    answer = []
    for S in s:
        if S == '(':
            answer.append(S)
        # 입력이 ')'인 경우
        else:
            # '('가 없다면 무조건
            # 올바르지 않은 괄호이므로 False 리턴 후 종료
            if len(answer) == 0:
                return False
            # ')'를 입력하는 경우는 없으니까
            # answer에 뭔가가 있다면 그건 '('다
            # 짝을 이뤘으므로 '('를 제거한다
            answer.pop()
    return True if len(answer)==0 else False

import sys

print(solution(sys.stdin.readline().strip()))
