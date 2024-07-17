def solution(bridge_length, weight, truck_weights):
    answer = 0  # 걸리는 시간
    b = [0] * bridge_length  # 다리에 올라갈 트럭들을 저장할 리스트, 다리의 길이만큼 0으로 초기화
    w = 0  # 다리에 올라온 트럭들의 무게의 합을 저장할 변수

    # 모든 트럭이 다리에 올라올 때 까지 반복
    while truck_weights:
        answer += 1
        w -= b.pop(0)  # 다리 맨 앞 트럭이 다리를 건너면 무게를 뺀다
        
        # 다음 트럭이 다리에 올라와도 견딜 수 있으면 트럭을 다리에 올라가게 한다
        if w+truck_weights[0] <= weight:
            w += truck_weights[0]
            b.append(truck_weights.pop(0))
        # 다리가 견딜 수 없으면 0을 추가하여 시간만 보낸다
        else:
            b.append(0)
            
    # 위의 반복문은 마지막 트럭이 다리에 올라가는 것 까지만 계산되므로
    # 마지막 트럭이 다리를 지나가는 시간까지 더한다
    return answer + bridge_length

import sys

bridge_length, weight = map(int, sys.stdin.readline().split())
truck_weights = list(map(int, sys.stdin.readline().split(",")))
print(solution(bridge_length, weight, truck_weights))