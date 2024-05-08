def solution(n, s):
    answer = []
    # s가 n보다 작다면 n개의 1을 더해도 s가 나올 수 없으므로 [-1] 리턴
    if n > s:
        return [-1]
    
    # n개의 수의 합이 s가 되는 수 들의 곱 중 가장 큰 곱은
    # 가장 비슷한 크기의 곱으로 곱하는거다
    num = s // n
    rest = s % n
    for i in range(n):
        answer.append(num)
    # 나누어 떨어지지 않더라도 rest는 num보다 작으므로
    # rest만큼 각각의 num값에 1씩 더하면 최고의 집합을 구할 수 있다
    if rest != 0:
        for i in range(n):
            answer[i] += 1
            rest -= 1
            if rest == 0:
                break
    answer.sort()
    return answer

import sys

n, s = map(int, sys.stdin.readline().split())
print(solution(n, s))