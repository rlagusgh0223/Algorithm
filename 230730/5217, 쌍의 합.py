import sys
t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    lst = []
    for x in range(1, 11):
        for y in range(x+1, 12):
            if x + y == n:
                lst.append([x, y])
    print("Pairs for {}: ".format(n), end='')
    for i in range(len(lst)):
        print(*lst[i], end='')
        if i < len(lst) - 1:
            print(", ", end='')
    print()