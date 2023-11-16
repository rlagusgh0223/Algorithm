# 다리에 올라갈 수 있는 트럭의 수는
# 다리를 건너는데 드는 시간과 같다
from collections import deque
def solution(bridge_length, weight, truck_weights):
    answer = 0
    b = deque([0] * bridge_length)  # 다리 위에 있는 트럭
    t = deque(truck_weights)  # 지나가야 되는 트럭
    w = 0  # 다리 위의 트럭 무게(sum(b)로 하면 시간초과 나므로 따로 계산을 해줘야 된다)
    while t:
        answer += 1
        w -= b.popleft()
        if w+t[0] <= weight:
            w += t[0]
            b.append(t.popleft())
        else:
            b.append(0)
    # 위의 반복문으로는 트럭이 다리에 올라오는 것 까지만 계산되므로,
    # 올라온 후 지나가는 시간도 더해줘야 한다
    answer += len(b)
    return answer



import sys
b, w = map(int, sys.stdin.readline().split())
t = list(map(int, sys.stdin.readline().strip().split(",")))
print(solution(b, w, t))