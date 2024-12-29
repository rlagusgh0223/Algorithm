def solution(numbers):
    numbers = sorted([str(n) for n in numbers], key=lambda x:x*3, reverse=True)
    answer = int(''.join(numbers))  # 숫자 앞의 불필요한 0을 제거하기 위해 필요
    return str(answer)

import sys

print(solution(list(map(int, sys.stdin.readline().split(", ")))))
