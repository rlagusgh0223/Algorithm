import sys
n, k = map(int, sys.stdin.readline().split())
lst = [[1]*(i+1) for i in range(n)]
for i in range(2, n):
    for j in range(1, len(lst[i])-1):
        lst[i][j] = lst[i-1][j-1]+lst[i-1][j]
print(lst[n-1][k-1])