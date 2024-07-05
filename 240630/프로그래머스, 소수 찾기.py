from itertools import permutations


def solution(numbers):
    answer = []
    num = []

    # numbers로 만들 수 있는 모든 수 구하기(중복 제거)
    for i in range(1, len(numbers)+1):
        num += list(permutations(numbers, i))
    num = list(set([int(''.join(n)) for n in num]))
    
    # 소수이면 answer에 입력
    for n in num:
        ck = True
        if n < 2:
            continue
        for i in range(2, int(n**0.5)+1):
            if n%i == 0:
                ck = False
                break
        if ck:
            answer.append(n)

    return len(answer)


import sys

print(solution(sys.stdin.readline().strip()))
