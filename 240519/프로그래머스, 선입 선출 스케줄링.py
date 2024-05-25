def solution(n, cores):
    # 작업할 개수가 core의 개수보다 적다면
    # 순서대로 작업을 주고 n번째 코어를 리턴하면 된다
    if n <= len(cores):
        return n
    
    # 처음 모든 코어에 작업을 줬으므로 작업의 개수 감소
    n -= len(cores)

    # 이분탐색을 이용해 작업을 마칠때의 시간을 구한다
    l, r = 1, max(cores) * n
    while l < r:
        mid = (l+r) // 2  # 작업 시간
        work = 0  # 해당 작업시간이라고 가정할 경우 가능한 작업 개수
        for c in cores:
            work += mid // c  # mid시간 동안 c시간마다 코어를 돌리는 작업 수 더한다
        # 작업을 n보다 많이 하면 최대시간을 줄이고
        # 아니면 최소시간을 줄인다
        if work >= n:
            r = mid
        else:
            l = mid + 1
    
    # 작업 완료 1시간 전까지 작업한 개수를 뺀다
    # 이거 없으면 시간초과 나온다
    for c in cores:
        n -= (r-1) // c
    
    # 마지막 작업 시간 동안 작업 횟수를 빼고
    # 작업을 마치면 해당 cpu 번호를리턴한다
    for i in range(len(cores)):
        if r % cores[i] == 0:
            n -= 1
            if n == 0:
                return i + 1

import sys

n = int(sys.stdin.readline())
cores = list(map(int, sys.stdin.readline().split(",")))
print(solution(n, cores))