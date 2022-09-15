def search(num):
    start = 0
    end = N-1
    while start<=end:
        mid = (start+end)//2
        if A[mid] == num:
            return 1
        elif A[mid] > num:
            end = mid - 1
        else:
            start = mid + 1
    return 0

N = int(input())
A = list(map(int, input().split()))
M = int(input())
arr = list(map(int, input().split()))
A.sort()
for i in range(M):
    print(search(arr[i])) 