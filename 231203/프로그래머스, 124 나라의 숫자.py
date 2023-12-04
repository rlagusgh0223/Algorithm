def solution(n):
    # 3진법과 동일한 방식으로 풀지만
    # 3으로 나누어 떨어지는 경우에는 3으로 나눈 몫에서 1을 빼야된다
    answer = ''
    while n:
        if n%3 == 0:
            answer += '4'
            n = n//3 - 1
        else:
            answer += str(n%3)
            n //= 3
    # 문자열은 reverse 못쓴다
    return answer[::-1]


import sys
n = int(sys.stdin.readline())
print(solution(n))