def solution(arrayA, arrayB):
    answer = 0
    # 각각의 최대공약수를 구한 후,
    # 그게 나누어 떨어지지 않는 수 중에서 가장 큰 값을 리턴하면 된다
    a, b = arrayA[0], arrayB[0]

    # 각각의 최대공약수 구하기
    for n in arrayA[1:]:
        a = gcd(n, a)
    for n in arrayB[1:]:
        b = gcd(n, b)

    # 다른 사람의 숫자로 나누어 떨어지지 않는 수 중 최댓값 구하기
    if notDiv(arrayA, b):
        answer = max(answer, b)
    if notDiv(arrayB, a):
        answer = max(answer, a)

    return answer

def gcd(a, b):
    if a%b == 0:
        return b
    return gcd(b, a%b)

def notDiv(array, gcd):
    for a in array:
        if a%gcd ==0:
            return False
    return True

import sys
a = list(map(int, sys.stdin.readline().split(", ")))
b = list(map(int, sys.stdin.readline().split(", ")))
print(solution(a, b))