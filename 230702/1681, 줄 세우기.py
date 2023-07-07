import sys
N, L = map(int, sys.stdin.readline().split())
cnt = 1
lst = []
while len(lst) < N:
    if str(L) not in str(cnt):
        lst.append(cnt)
    cnt += 1
print(lst[-1])