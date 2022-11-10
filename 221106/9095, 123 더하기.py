import sys
T = int(sys.stdin.readline())
for i in range(T):
    n = int(sys.stdin.readline())
    lst = [1] * (n+2)
    lst[2] = 2
    for j in range(3, n+1):
        lst[j] = lst[j-1] + lst[j-2] + lst[j-3]
    print(lst[n])