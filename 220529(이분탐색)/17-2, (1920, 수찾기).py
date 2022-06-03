import sys
N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
B = list(map(int, sys.stdin.readline().split()))

A.sort()

def check(now):
    start = 0
    end = N-1
    while start<=end:
        mid = (start+end)//2
        if A[mid] == now:
            print(1)
            return
        elif now < A[mid]:
            end = mid-1
        else:
            start = mid+1
    print(0)
    return

for i in range(M):
    check(B[i])