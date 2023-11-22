from itertools import permutations
def solution(numbers):
    answer = []
    numbers = list(numbers)

    # 가능한 문자열 리스트 만들기
    num = []
    # permutations을 이용해서 모든 자릿수의 경우의 수를 도출한다
    for i in range(1, len(numbers)+1):
        # append를 쓰면 이차원 배열 되지만
        # +=를 쓰면 일차원 배열이 된다
        num += list(permutations(numbers, i))
    # 나올 수 있는 모든 문자열을 숫자로 바꾼다
    num = list(set([int(''.join(n)) for n in num]))
    
    # 소수 검사 후 소수면 answer에 입력
    # 제곱근까지 나뉘어지는 수가 없으면 소수다
    for n in num:
        if n < 2:
            continue
        ck = True
        for i in range(2, int(n**0.5)+1):
            if n%i == 0:
                ck = False
                break
        if ck:
            answer.append(n)
    return len(answer)


import sys
numbers = sys.stdin.readline().strip()
print(solution(numbers))