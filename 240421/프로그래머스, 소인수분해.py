def solution(n):
    answer = set()
    d = 2
    while d <= n:
        if n%d == 0:
            answer.add(d)
            n //= d
        else:
            d += 1
    # set()을 사용하면 순서는 무시한 채 리스트에 중복만 제거한다
    return sorted(list(answer))

import sys

print(solution(int(sys.stdin.readline())))
