from collections import deque
import sys
N = int(sys.stdin.readline())
card = deque(list(i for i in range(1, N+1)))    # 1부터 N까지 card 큐에 입력

while True:
    if len(card) == 1:    # 마지막 한 장 남을때까지 반복
        break
    del card[0]    # 이번 턴 맨 앞의 숫자(숫자더미의 맨 위의 수) 삭제
    x = card.popleft()    # 그 다음 수 마지막으로 이동
    card.append(x)

print(card[0])    # 마지막 남은 수 출력


##############################
# 모범답안
# from collections import deque
# import sys

# N = int(sys.stdin.readline())

# queue = deque()
# for i in range(N):
#     queue.append(i+1)

# while len(queue) > 1:
#     queue.popleft()
#     queue.append(queue.popleft())

# print(queue.pop())