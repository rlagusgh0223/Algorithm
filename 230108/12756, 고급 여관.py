import sys
A1, A2 = map(int, sys.stdin.readline().split())
B1, B2 = map(int, sys.stdin.readline().split())
while True:
    A2 -= B1
    B2 -= A1
    if A2<=0 and B2<=0:
        print("DRAW")
        break
    elif A2 <= 0:
        print("PLAYER B")
        break
    elif B2 <= 0:
        print("PLAYER A")
        break