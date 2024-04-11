def solution(a, b, c, d):
    answer = 0
    origin = [a, b, c, d]
    check = list(set(origin))
    check.sort()
    # 네 주사위의 수가 같다면
    if len(check) == 1:
        answer = 1111 * check[0]
    # 나온 주사위 수가 두 종류 뿐인데
    elif len(check) == 2:
        p, q = max(check), min(check)
        # 그 중 3개의 값이 같고 하나만 다르다면(3 + 1)
        if origin.count(p) == 3:
            answer = (10 * p + q)**2
        elif origin.count(q) == 3:
            answer = (10 * q + p)**2
        # 각각 2개씩 있다면(2 + 2)
        elif origin.count(p) == 2:
            answer = (p+q) * abs(p-q)
    # 두 개의 같은 값과 하나씩 다른값이라면(2 + 1 + 1)
    elif len(check) == 3:
        for i in range(len(check)):
            if origin.count(check[i]) == 2:
                del check[i]
                break
        answer = check[0] * check[1]
    # 4개씩 값이 다르다면
    else:
        answer = min(check)

    return answer

import sys

a, b, c, d = map(int, sys.stdin.readline().split())
print(solution(a, b, c, d))