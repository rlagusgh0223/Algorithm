from collections import deque


def solution(queue1, queue2):
    answer = 0
    q1, q2 = deque(queue1), deque(queue2)
    sum1, sum2 = sum(q1), sum(q2)

    # q의 길이 3배만큼 계산해도 답이 안 나오면 -1을 리턴한다
    for i in range(3 * len(q1)):
        if sum1 > sum2:
            sum1 -= q1[0]
            sum2 += q1[0]
            q2.append(q1.popleft())
        elif sum1 < sum2:
            sum1 += q2[0]
            sum2 -= q2[0]
            q1.append(q2.popleft())
        # 양쪽 큐의 합이 같아진다면 그대로 리턴
        else:
            return answer
        answer += 1
    return -1

import sys

q1 = list(map(int, sys.stdin.readline().split(", ")))
q2 = list(map(int, sys.stdin.readline().split(", ")))
print(solution(q1, q2))