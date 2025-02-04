def solution(bridge_length, weight, truck_weights):
    answer = 0
    # 다리 위의 상황을 저장할 변수, 다리 위의 무게를 저장할 변수수
    b, w = [0] * bridge_length, 0
    
    # 모든 트럭이 다리에 올라갈 때까지 반복복
    while truck_weights:
        answer += 1
        w -= b.pop(0)  # 현재 다리에서 맨 앞의 트럭이 다리를 지나가면 무게를 뺀다
        # 다음 트럭이 다리에 올라와도 무게를 견딜 수 있으면 다리에 올린다
        if w+truck_weights[0] <= weight:
            w += truck_weights[0]
            b.append(truck_weights.pop(0))
        # 못 견디면 다리에 올리지 않는다
        else:
            b.append(0)

    # 위의 반복문은 마지막 트럭이 다리에 막 올라갔을때 까지만이므로
    # 다리를 지나가는 시간(다리의 길이) 만큼 더해준다
    return answer + bridge_length

import sys

b, w = map(int, sys.stdin.readline().split())
t = list(map(int, sys.stdin.readline().split(",")))
print(solution(b,w,t))