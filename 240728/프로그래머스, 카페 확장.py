from collections import deque


def solution(menu, order, k):
    answer = 0
    q = deque()  # 주문한 음료의 종류를 기록할 큐. 동시에 있는 사람의 수도 판단할 수 있다
    collect = -1  # 음료 제작 시간. 초기값은 -1로 해서 바로 제작가능한지 판단한다
    idx = 0  # 손님 번호

    # 0초부터 들어오는 손님의 수만큼 초 단위로 계산하는 반복문
    # k가 10이고 4명의 손님이 온다면 0, 10, 20, 30초에 손님이 들어온다
    for t in range(k*(len(order)-1) + 1):
        # 손님이 들어왔을 때
        # 주문을 입력하고 다음 손님 번호를 준비한다
        if t == idx * k:
            q.append(order[idx])
            idx += 1
        
        # 주문한 음료의 제작이 끝났을 때
        # 제작한 음료를 주문 리스트에서 제외하고
        # 음료 제작시간을 초기화해 음료 제작이 가능한 상태로 바꾼다
        if t == collect:
            q.popleft()
            collect = -1
        
        # 음료를 제작할 수 있고 주문이 남아있을 때
        # 음료 완료 시간을 collect에 입력한다
        if collect==-1 and q:
            collect = t + menu[q[0]]
        
        # 동시에 있는 손님의 수 중 최댓값을 구한다
        answer = max(answer, len(q))

    return answer


import sys

menu = list(map(int, sys.stdin.readline().split(", ")))
order = list(map(int, sys.stdin.readline().split(", ")))
k = int(sys.stdin.readline())
print(solution(menu, order, k))