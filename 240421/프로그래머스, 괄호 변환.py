def solution(p):
    # 1. 입력이 빈 문자열인 경우, 빈 문자열을 반환
    if not p:
        return p
    
    # 2. 문자열 w를 두 "균형잡힌 괄호 문자열" u, v로 분리
    u, v = True, 0
    for i in range(len(p)):
        if p[i] == '(':
            v -= 1
        else:
            v += 1
        
        if v > 0:
            u = False
        
        if v == 0:
            # 3. 문자열 u가 "올바른 괄호 문자열" 이라면
            if u:
                # 수행한 결과 문자열을 u에 이어 붙인 후 반환
                return p[:i+1] + solution(p[i+1:])
            # 4. 문자열 u가 "올바른 괄호 문자열"이 아니라면
            else:
                #   4-1. 빈 문자열에 첫 번째 문자로 '('를 붙입니다. 
                #   4-2. 문자열 v에 대해 1단계부터 재귀적으로 수행한 결과 문자열을 이어 붙입니다. 
                #   4-3. ')'를 다시 붙입니다. 
                #   4-4. u의 첫 번째와 마지막 문자를 제거하고, 나머지 문자열의 괄호 방향을 뒤집어서 뒤에 붙입니다. 
                #   4-5. 생성된 문자열을 반환합니다.
                return '(' + solution(p[i+1:]) + ')' + ''.join(list(map(lambda x:'(' if x==')' else ')', p[1:i])))

import sys

print(solution(sys.stdin.readline().strip()))
