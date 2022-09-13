import sys

def search(now):
    start = 0
    end = N-1
    while start<=end:
        mid = (start+end)//2
        if A[mid] == now:
            return 1
        elif A[mid] > now:
            end = mid-1
        else:
            start = mid + 1
    return 0

N = int(sys.stdin.readline())
A = [int(x) for x in sys.stdin.readline().split()]
A.sort()
M = int(sys.stdin.readline())
num = [int(x) for x in sys.stdin.readline().split()]
for now in num:
    print(search(now))