# 몬스터가 어디에 있든 마지막줄에 있는게 아니면 잡힌다
# 마지막 줄인 경우 윗줄에서 바로 내려가면 몬스터를 피할 수 있다
import sys
N, M = map(int, sys.stdin.readline().split())
A, D = map(int, sys.stdin.readline().split())
r, c = map(int, sys.stdin.readline().split())
if D == 0:
    if r != N:
        print("NO...")
    else:
        if N%2 == 1:
            print("YES!")
        else:
            print("NO...")
elif D == 1:
    if r != N:
        print("NO...")
    else:
        if N%2 == 0:
            print("YES!")
        else:
            print("NO...")
    



# import sys
# N, M = map(int, sys.stdin.readline().split())
# A, D = map(int, sys.stdin.readline().split())
# r, c = map(int, sys.stdin.readline().split())
# i = 1
# while i <= N:
#     if i==r and A==c:
#         print("NO...")
#         break
#     if i==N and A==M:
#         print("YES!")
#         break
#     if i%2==1 and D==0:
#         A -= 1
#     elif i%2==0 and D==0:
#         A += 1
#     elif i%2==1 and D==1:
#         A += 1
#     else:
#         A -= 1
#     if A==0 or A==M+1:
#         i += 1