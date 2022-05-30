# start<=end로 두는것 잊지 말것
import sys
N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
B = list(map(int, sys.stdin.readline().split()))

A.sort()

for i in B:
    start = 0
    end = N-1
    chk = True
    while start<=end:
        mid = (start+end)//2
        if i == A[mid]:
            print(1)
            chk = False
            break
        elif i >= A[mid]:
            start = mid+1
        else:
            end = mid-1
    
    if chk:
        print(0)

############################################
# 모범답안
# import sys
# N = int(sys.stdin.readline())
# A = [int(ans) for ans in sys.stdin.readline().split()]
# A.sort()
# M = int(sys.stdin.readline())
# B = list(map(int, sys.stdin.readline().split()))

# def binarySeach(target):
#     start = 0
#     end = N-1
#     while start<=end:
#         mid = (start+end)//2
#         if A[mid] == target:
#             print(1)
#             return
#         elif A[mid] <= target:
#             start = mid+1
#         else:
#             end = mid-1
#     print(0)
#     return

# for i in range(M):
#     binarySeach(B[i])