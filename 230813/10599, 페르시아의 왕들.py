import sys
while True:
    a, b, c, d = map(int, sys.stdin.readline().split())
    if a == b == c == d == 0:
        break
    print(c-b, d-a)