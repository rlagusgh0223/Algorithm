import sys
N = int(sys.stdin.readline())
lst = list(sys.stdin.readline().rstrip())
S, L = 0, 0
for now in lst:
    if now == 'S':
        S += 1
    else:
        L += 1
if L == 0:
    print(S)
else:
    print(S+(L//2)+1)