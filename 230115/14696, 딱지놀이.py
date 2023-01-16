import sys
N = int(sys.stdin.readline())
for _ in range(N):
    A = list(map(int, sys.stdin.readline().split()))[1:]
    B = list(map(int, sys.stdin.readline().split()))[1:]
    for i in range(4, 0, -1):
        if A.count(i) > B.count(i):
            print("A")
            break
        elif A.count(i) < B.count(i):
            print("B")
            break
        if i == 1:
            print("D")


# 내 코드
# import sys
# input = sys.stdin.readline
# N = int(sys.stdin.readline())
# for i in range(N):
#     A = list(map(int, input().split()))
#     B = list(map(int, input().split()))
#     del A[0]
#     del B[0]
#     if A.count(4) > B.count(4):
#         print("A")
#     elif A.count(4) < B.count(4):
#         print("B")
#     elif A.count(3) > B.count(3):
#         print("A")
#     elif A.count(3) < B.count(3):
#         print("B")
#     elif A.count(2) > B.count(2):
#         print("A")
#     elif A.count(2) < B.count(2):
#         print("B")
#     elif A.count(1) > B.count(1):
#         print("A")
#     elif A.count(1) < B.count(1):
#         print("B")
#     else:
#         print("D")