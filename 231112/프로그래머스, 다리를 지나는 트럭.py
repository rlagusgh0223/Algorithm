# 다리에 올라갈 수 있는 트럭의 수는
# 다리를 건너는데 드는 시간과 같다
from collections import deque
def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge = deque([0] * bridge_length)
    truck_weights = deque(truck_weights)
    while truck_weights:
        answer += 1
        bridge.popleft()
        if sum(bridge) + truck_weights[0] <= weight:
            bridge.append(truck_weights.popleft())
        else:
            bridge.append(0)
    answer += len(bridge)
    return answer



import sys
b, w = map(int, sys.stdin.readline().split())
t = list(map(int, sys.stdin.readline().strip().split(",")))
print(solution(b, w, t))