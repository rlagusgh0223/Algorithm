def solution(n, a, b):
    answer = 0
    while a != b:
        answer += 1
        # (+1)//2 를 함으로써 다음 경기에서 몇번째 경기인지 구할 수 있다
        # a, b를 그대로 나누면 1//2=0, 2//2=1이 되므로
        # 1번을 빼고 2-3, 4-5 이런식으로 붙게 되는걸로 계산한다
        a, b = (a+1)//2, (b+1)//2
    return answer

import sys
N, A, B = map(int, sys.stdin.readline().split())
print(solution(N, A, B))