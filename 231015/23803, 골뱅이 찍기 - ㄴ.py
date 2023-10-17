import sys
N = int(sys.stdin.readline())
for i in range(5*N):
    if i >= 5*N-N:
        print('@'*(5*N))
    else:
        print('@' * N)