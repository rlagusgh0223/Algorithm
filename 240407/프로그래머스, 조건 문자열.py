def solution(ineq, eq, n, m):
    # eval() : 괄호 안의 문자열을 식으로 받아서 해결한다
    # ex. eval("1 + 2") => 3 호출
    return int(eval(str(n) + ineq + eq.replace('!', '') + str(m)))

def solutions(ineq, eq, n, m):
    answer = 0
    if ineq == '<':
        if eq == '=':
            if n <= m:
                answer = 1
        else:
            if n < m:
                answer = 1
    elif ineq == '>':
        if eq == '=':
            if n >= m:
                answer = 1
        else:
            if n > m:
                answer = 1

    return answer

import sys

ineq, eq, n, m = sys.stdin.readline().strip().split()
n, m = int(n), int(m)
print(solution(ineq, eq, n, m))