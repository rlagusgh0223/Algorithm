import sys
while True:
    lst = list(map(int, sys.stdin.readline().split()))
    lst.sort()
    if lst[2] == 0:
        break
    if lst[2] >= lst[0] + lst[1]:
        print("Invalid")
    elif lst[0] < lst[1] < lst[2]:
        print("Scalene")
    elif lst[0] == lst[1] == lst[2]:
        print("Equilateral")
    else:
        print("Isosceles")