import sys
while True:
    n = int(sys.stdin.readline())
    if n == 0:
        break
    lst = []
    for i in range(n):
        lst.append(sys.stdin.readline().rstrip())
    lst.sort(key=str.upper)
    print(*lst[0], sep='')