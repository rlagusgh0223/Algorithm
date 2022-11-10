import sys
n = int(sys.stdin.readline())
if n == 1:
    print(n%10007)
else:
    lst = [0] * (n+1)
    lst[1] = 1
    lst[2] = 3
    for i in range(3, n+1):
        lst[i] = lst[i-1] + 2*lst[i-2]
    print(lst[n]%10007)