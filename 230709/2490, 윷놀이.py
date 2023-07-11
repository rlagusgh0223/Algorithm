import sys
for _ in range(3):
    lst = list(map(int, sys.stdin.readline().split()))
    if lst.count(0) == 1:
        print("A")
    elif lst.count(0) == 2:
        print("B")
    elif lst.count(0) == 3:
        print("C")
    elif lst.count(0) == 4:
        print("D")
    else:
        print("E")