from collections import deque


def solution(menu, order, k):
    answer = 0
    q = deque()
    complete = -1  # 음료 주문 가능한지(-1) 또는 음료 만드는 시간 몇분인지 표시하는 변수
    idx = 0  # 몇번째 손님인지 체크하는 변수

    # 4명일 경우 0, 10, 20, 30초에 주문하므로 k*(len(order)-1) 초 만큼 주문한다
    # range의 마지막이 30으로 입력되면 29까지만 돌아가므로 1을 더해준다
    for t in range(k*(len(order)-1) + 1):
        # 사람이 들어온 경우
        if t == k*idx:
            q.append(order[idx])
            idx += 1

        # 사람이 나간 경우(음료를 다 만든 경우)
        if t == complete:
            q.popleft()
            complete = -1

        # 음료를 만들 수 있고 손님도 있어 음료를 만들기 시작한 경우
        if complete==-1 and len(q)>0:
            complete = t + menu[q[0]]

        # 가장 손님이 많을 경우 몇 명인지 계산
        answer = max(answer, len(q))

    return answer

import sys

menu = list(map(int, sys.stdin.readline().split(", ")))
order = list(map(int, sys.stdin.readline().split(", ")))
k = int(sys.stdin.readline())
print(solution(menu, order, k))