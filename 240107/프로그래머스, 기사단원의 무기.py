def solution(number, limit, power):
    answer = 1
    for i in range(2, number+1):
        cnt = 0
        # 약수는 제곱근 까지만 구하면 그 수와 곱한 어떤 수가 약수이므로 2를 더하면 된다
        for j in range(1, int(i**0.5)+1):
            if i%j == 0:
                cnt += 1
                # 그러나 제곱근을 중복으로 곱한 값이 현재 값일 경우 1만 더한다
                # ex) 5*5 = 25
                if j*j != i:
                    cnt += 1
        if cnt > limit:
            answer += power
        else:
            answer += cnt
    return answer

import sys
n, l, p = map(int, sys.stdin.readline().split())
print(solution(n, l, p))