import sys
s = list(map(int, sys.stdin.readline().split()))
t = list(map(int, sys.stdin.readline().split()))
S, T = sum(s), sum(t)
if S >= T:
    print(S)
else:
    print(T)