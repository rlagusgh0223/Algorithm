import sys
n = int(sys.stdin.readline())
lst = [0, 2, 3, 5] + [0]*(n-4)
for i in range(4, n):
    lst[i] = (lst[i-1]+lst[i-2])%10
print(lst[n-1])