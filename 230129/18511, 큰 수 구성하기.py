from itertools import product
import sys
N, K = map(int, sys.stdin.readline().split())
k = list(sys.stdin.readline().split())
length = len(str(N))
while True:
    temp = list(product(k, repeat=length))
    ex = []
    for i in temp:
        now = int(''.join(i))
        if now <= N:
            ex.append(now)
    if len(ex) > 0:
        print(max(ex))
        break
    length -= 1