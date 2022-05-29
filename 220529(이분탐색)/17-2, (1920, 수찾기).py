import sys
N = int(sys.stdin.readline())
A = [int(ans) for ans in sys.stdin.readline().split()]
A.sort()
M = int(sys.stdin.readline())
AA = list(map(int, sys.stdin.readline().split()))

def binarySeach(target):    # 이분탐색 정의. 인자로는 AA의 원소를 받는다
    start = 0
    end = N-1
    while start<=end:
        mid = (start+end)//2
        if A[mid] == target:
            print(1)
            return
        elif A[mid] <= target:
            start = mid+1
        else:
            end = mid-1
    print(0)
    return

for i in range(M):    # 배열 AA의 원소들을binarySeach 함수를 통해 이분탐색
    binarySeach(AA[i])