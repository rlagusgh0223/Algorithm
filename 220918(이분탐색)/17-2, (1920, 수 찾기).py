import sys

def search(num):
    start = 0
    end = N-1
    while start<=end:
        mid = (start+end)//2
        if A[mid] == num:
            return 1
        elif A[mid] < num:
            start = mid + 1
        else:
            end = mid - 1
    return 0


N = int(sys.stdin.readline())
A = [int(a) for a in sys.stdin.readline().split()]
A.sort()
M = int(sys.stdin.readline())
lst = [int(m) for m in input().split()]

for i in lst:
    print(search(i))