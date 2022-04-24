# 이건 내 코든데 for문을 두번 쓰고, 리스트를 사용한것만 다르다
# pypy3로는 맞았다고 나온다
from collections import deque
import sys

N = int(sys.stdin.readline())
order = []
q = deque()
for i in range(N):
    order.append(list(sys.stdin.readline().split()))

for i in range(N):    # 원래는 위에서 한번에 해도 되겠지만 내가 보기 편하게 나중에 출력하게 했다.
    if order[0] == 'push':
        q.append(int(order[i][1]))
    elif order[0] == 'pop':
        if len(q) == 0:
            print("-1")
        else:
            out = q.popleft()
            print(out)
    elif order[i][0] == 'size':
        print(len(q))
    elif order[i][0] == 'empty':
        if q:    # q에 정수가 있으면 0 출력
            print("0")
        else:
            print("1")
    elif order[i][0] == 'front':
        if len(q) == 0:
            print("-1")
        else:
            print(q[0])

    elif order[i][0] == 'back':
        if len(q) == 0:
            print("-1")
        else:
            print(q[-1])





################################################
# 모범답안
# from collections import deque
# import sys

# N = int(sys.stdin.readline())
# q = deque()
# for i in range(N):    # 반복문을 2개 둬서 보기 편하게 만들어봤는데 시간초과 났다. 이것만으로 되는지 확인해보겠다.
#     order = sys.stdin.readline().split()
#     if order[0] == 'push':
#         q.append(int(order[1]))
#     elif order[0] == 'pop':
#         if len(q) == 0:
#             print("-1")
#         else:
#             out = q.popleft()
#             print(out)
#     elif order[0] == 'size':
#         print(len(q))
#     elif order[0] == 'empty':
#         if q:    # q에 정수가 있으면 0 출력
#             print("0")
#         else:
#             print("1")
#     elif order[0] == 'front':
#         if len(q) == 0:
#             print("-1")
#         else:
#             print(q[0])
#     elif order[0] == 'back':
#         if len(q) == 0:
#             print("-1")
#         else:
#             print(q[-1])