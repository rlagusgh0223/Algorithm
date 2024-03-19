def solution(polynomial):
    answer = []
    check = {'x':0, 'const':0}
    polynomial = polynomial.split(" + ")
    for p in polynomial:
        if 'x' in p:
            # x 앞에 수가 없고 x뿐이라면 x의 값에 1만 더한다
            if 'x' == p:
                check['x'] += 1
            else:
                # p의 마지막 p[-1]은 x이므로 이를 제외한 값을 더한다
                check['x'] += int(p[:-1])
        # x가 없는 상수라면
        else:
            check['const'] += int(p)
    
    # x에 대해 x가 0이라면 더할것도 없으니 필요없고
    # x가 1일 경우 x만
    # x가 2 이상일 경우 x의 수만큼의 숫자와 x를 붙인다
    if check['x'] == 1:
        answer.append('x')
    elif check['x'] > 1:
        answer.append(str(check['x'])+'x')
    
    # 상수가 있을경우 상수를 문자열에 붙인다
    if check['const'] > 0:
        answer.append(str(check['const']))

    return " + ".join(answer)

import sys

print(solution(sys.stdin.readline().strip()))
