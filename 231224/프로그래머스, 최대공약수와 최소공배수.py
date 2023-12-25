def solution(n, m):
    answer = []
    x, y = min(n,m), max(n,m)
    # 최대공약수 구하는 점화식
    while y:
        x, y = y, x%y
    answer.append(x)
    answer.append((n*m)//answer[0])  # 최소공배수 구하는 점화식
    return answer

import sys
n, m = map(int, sys.stdin.readline().split())
print(solution(n, m))