def search(now):
    start = 0
    end = N-1
    while start<=end:
        mid = (start+end) // 2
        if A[mid] == now:
            return 1
        elif A[mid] < now:
            start = mid + 1
        else:
            end = mid - 1
    return 0

import sys

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
A.sort()
M = int(sys.stdin.readline())
Num = [int(num) for num in sys.stdin.readline().split()]

for now in Num:
    print(search(now))