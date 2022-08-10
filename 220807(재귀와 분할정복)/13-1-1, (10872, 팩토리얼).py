import sys

def fact(N):
    if N>1:
        N *= fact(N-1)
    else:
        N = 1
    return N

N = int(sys.stdin.readline())
print(fact(N))