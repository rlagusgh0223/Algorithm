import sys
A, B = map(int, sys.stdin.readline().split())
while True:
    B += A
    if B >= 5:
        print("yt")
        break
    A += B
    if A >= 5:
        print("yj")
        break