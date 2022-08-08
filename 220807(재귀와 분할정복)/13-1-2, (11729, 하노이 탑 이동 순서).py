import sys

def hanoi(N, start, to, end):
    if N==1:
        print(start, end)
    else:
        hanoi(N-1, start, end, to)
        print(start, end)
        hanoi(N-1, to, start, end)

K = int(sys.stdin.readline())
print(2**K-1)
hanoi(K, 1, 2, 3)