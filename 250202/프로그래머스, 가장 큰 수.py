def solution(numbers):
    numbers = sorted([str(n) for n in numbers], key=lambda x:x*3, reverse=True)
    # 입력이 0만 있을 경우 무조건 0으로 반환해야 하므로(000처럼 나오면 안된다)
    # int로 한 번 변환하고 다시 str로 변환한다
    return str(int(''.join(numbers)))

import sys

print(solution(list(map(int, sys.stdin.readline().split(", ")))))
