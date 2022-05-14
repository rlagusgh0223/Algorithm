# N=2, M=2 라고 하면 i, depth는 2까지 간다
# NaM(0)
# i = 1
# answer = [1] -> NaM(1)
#                 i = 1
#                 i = 2
#                 answer = [1, 2] -> NaM(2)
#                                    print([1, 2])
#                 answer = [1]
# answer = []
# i = 2
# answer = [2] -> NaM(1)
#                 i = 1
#                 answer = [2, 1] -> NaM(2)
#                                    print([2, 1])
#                 answer = [2]
#                 i = 2
# answer = []

#######################################################

# 내 풀이
# import sys

# N, M = map(int, sys.stdin.readline().split())
# answer = []

# def NaM(depth):
#     if depth == M:
#         print(' '.join(map(str, answer)))
#         return
#     for i in range(1, N+1):
#         cnt = 0
#         for j in answer:
#             if i == j:
#                 cnt = 1

#         if cnt == 0:
#             answer.append(i)
#             NaM(depth+1)
#             answer.pop()

# NaM(0)

#########################################
# 모범답안
import sys

N, M = map(int, sys.stdin.readline().split())
answer = []

def NaM(depth):
    if depth == M:
        print(' '.join(map(str, answer)))
        return
    for i in range(1, N+1):
        if i in answer:    # 중복을 확인하는 조건문
            continue    # 이미 리스트에 있다면 이번 수는 제외

        answer.append(i)    # 리스트에 없다면 입력
        NaM(depth+1)
        answer.pop()

NaM(0)