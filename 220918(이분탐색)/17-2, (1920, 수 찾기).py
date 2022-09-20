def search(num):
    start = 0
    end = N-1
    while start<=end:
        mid = (start+end)//2
        if A[mid] == num:
            return 1
        elif num > A[mid]:
            start = mid + 1
        else:
            end = mid - 1
    return 0


N = int(input())
A = list(map(int, input().split()))
A.sort()
M = int(input())
arr = [int(m) for m in input().split()]

for i in arr:
    print(search(i))