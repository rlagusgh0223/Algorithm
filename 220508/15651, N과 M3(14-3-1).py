# N = 2, M = 2 일때 i와 depth는 2까지만 증가
# NM(0)
# i = 1
# answer = [1] -> NM(1)
#                 i = 1
#                 answer = [1, 1] -> NM(2)
#                                    print([1, 1])
#                 answer = [1]
#                 i = 2
#                 answer = [1, 2] -> NM(2)
#                                    print([1, 2])
#                 answer = [1]
# answer = []
# i = 2
# answer = [2] -> NM(1)
#                 i = 1
#                 answer = [2, 1] -> NM(2)
#                                    print([2, 1])
#                 answer = [2]
#                 i = 2
#                 answer = [2, 2] -> NM(2)
#                                    print([2, 2])
#                 answer = [2]
# answer = []
import sys
N, M = map(int, sys.stdin.readline().split())
answer = []

def NM(depth):
    if depth == M:
        print(' '.join(map(str, answer)))
        return
    for i in range(1, N+1):
        answer.append(i)
        NM(depth+1)
        answer.pop()

NM(0)