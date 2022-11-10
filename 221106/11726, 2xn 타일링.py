import sys
n = int(sys.stdin.readline())
lst = [0] * (n+1)
if n > 3:
    lst[1] = 1
    lst[2] = 2
    lst[3] = 3
    for i in range(4, n+1):
        lst[i] = lst[i-1] + lst[i-2]
    print(lst[n]%10007)
else:
    print(n%10007)
