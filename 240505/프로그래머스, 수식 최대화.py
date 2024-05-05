from itertools import permutations


def solution(expression):
    oper = [op for op in permutations(['+', '-', '*'], 3)]
    answer = []

    for op in oper:
        a, b, temp_list = op[0], op[1], []
        # 첫번째 우선순위 연산자로 수식을 나눈다
        for e in expression.split(a):
            # 두번째 우선순위 연산자로 수식을 나누고
            # 각각의 수식들에 ()를 씌운다
            temp = [f'({i})' for i in e.split(b)]
            # ()로 감싼 수식들을 두번째 우선순위 연산자를
            # 붙여서 하나의 문자열을 만들고 다시 ()를 씌운다
            temp_list.append(f'({b.join(temp)})')
        # 모든 문자열을 첫번재 우선순위 연산자를 붙이고 계산한다
        # eval()은 문자열을 계산하는 함수다
        # 이때 나온 값은 절대값으로 저장한다
        answer.append(abs(eval(a.join(temp_list))))
    return max(answer)

import sys

print(solution(sys.stdin.readline().strip()))
