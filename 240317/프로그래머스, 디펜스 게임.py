import heapq


def solution(n, k, enemy):
    answer = sumEnemy = 0
    heap = []
    # n의 수보다 enemy의 수가 많다면
    # heapq를 이용해 가장 많은 적을 무적권으로 처리하고 n을 유지한다
    for e in enemy:
        # heapq는 작은 값부터 빼므로(최소힙) 제일 큰 값을 heapq에서 빼기 위해 -를 붙인다
        heapq.heappush(heap, -e)
        sumEnemy += e
        if sumEnemy > n:
            # 남은 무적권이 없으면 종료
            if k == 0:
                break
            # 무적권이 남았다면 무적권을 한번 없애고 sumEnemy에서 가장 많은 적을 뺀다
            # (가장 많은 적을 무적권으로 처리한 셈 친다)
            k -= 1
            sumEnemy += heapq.heappop(heap)
        # 이번 라운드를 계산한다
        answer += 1
    return answer

import sys

n, k = map(int, sys.stdin.readline().split())
enemy = list(map(int, sys.stdin.readline().split(", ")))
print(solution(n, k, enemy))