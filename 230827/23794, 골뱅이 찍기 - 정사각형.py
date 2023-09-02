import sys
N = int(sys.stdin.readline())
for i in range(N+2):
    if i==0 or i==N+1:
        print("@" * (N+2))
    else:
        print("@" + " "*N + "@")