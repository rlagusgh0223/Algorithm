def bfs():
    q = deque()
    q.append(B)
    cnt = 0
    while q:
        x = q.popleft()
        cnt += 1
        if x == A:
            return cnt
        elif x < A:
            break
        elif x%10 == 1:
            x -= 1
            x //= 10
            q.append(x)
        elif x%2==0:
            x //= 2
            q.append(x)
        else:
            break
    return -1

from collections import deque
import sys
A, B = map(int, sys.stdin.readline().split())
print(bfs())


# 아래 코드가 시간은 더 오래 걸리지만, 메모리나 코드길이는 작다
# BFS에는 이 코드가 더 어울리는 것 같아서 만들어봤다
# def bfs():
#     q = deque()
#     q.append((A, 1))  # A<B이므로 한번은 반드시 연산한다
#     while q:
#         x, cnt = q.popleft()
#         if x == B:
#             return cnt
#         if x*2 <= B:
#             q.append((x*2, cnt+1))
#         if x*10+1 <= B:
#             q.append((x*10+1, cnt+1))
#     return -1

# from collections import deque
# import sys
# A, B = map(int, sys.stdin.readline().split())
# print(bfs())