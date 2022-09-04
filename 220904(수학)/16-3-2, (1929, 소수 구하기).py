import sys

def search(now):
    if now == 1:
        return False
    for i in range(2, int(now**0.5)+1):
        if now % i == 0:
            return False
    return True

M, N = map(int, sys.stdin.readline().split())
for i in range(M, N+1):
    if search(i):
        print(i)