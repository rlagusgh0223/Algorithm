import sys

def hanoi(N, start, to, end):
    if N==1:
        print(start, end)
    else:
        hanoi(N-1, start, end, to)
        print(start, end)
        hanoi(N-1, to, start, end)

N = int(sys.stdin.readline())
print(2**N-1)
hanoi(N, 1, 2, 3)