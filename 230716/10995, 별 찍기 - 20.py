import sys
N = int(sys.stdin.readline())
for i in range(N):
    if i%2 == 0:
        print("* " * N)
    else:
        print(" *" * N)