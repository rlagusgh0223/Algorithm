from math import factorial
def solution(n, k):
    answer = []
    lst = [i for i in range(1, n+1)]
    while lst:
        # k번째 있는 수를 구하기 위해 k번째 순열에 첫 번째 있는 값의 인덱스 구하기
        a = (k-1)//factorial(n-1)
        answer.append(lst.pop(a))
        # 다음에 올 숫자를 구하기 위해 나머지값으로 바꿈
        k %= factorial(n-1)
        n -= 1
    return answer

import sys
n, k = map(int, sys.stdin.readline().split())
print(solution(n, k))