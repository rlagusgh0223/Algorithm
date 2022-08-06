import sys
def hanoi(N, start, middle, end):
    if N==1:
        print(start, end)
    else:
        hanoi(N-1, start, end, middle)
        print(start, end)
        hanoi(N-1, middle, start, end)

N = int(sys.stdin.readline())
print(2**N-1)
hanoi(N, 1, 2, 3)