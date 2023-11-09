def solution(priorities, location):
    # priorities는 각 프로세스의 우선순위를 나타내므로
    # 어떤 프로세스의 우선순위가 어떻게 되는지 같이 저장한다
    # enumerate는 입력된 배열의 순서도 같이 저장한다
    queue = [(x, y) for x, y in enumerate(priorities)]
    answer = 0
    while True:
        cur = queue.pop(0)  # 가장 먼저 입력된거 출력한다
        # any : 하나라도 True면 다 True
        if any(cur[1] < q[1] for q in queue):  # 이번에 나온 프로세스가 우선순위가 가장 높은지 비교
            queue.append(cur)
        else:
            answer += 1
            if cur[0] == location:
                return answer

import sys
priorities = list(map(int, sys.stdin.readline().split(", ")))
location = int(sys.stdin.readline())
print(solution(priorities, location))