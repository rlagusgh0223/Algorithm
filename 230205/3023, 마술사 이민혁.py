import sys
R, C = map(int, sys.stdin.readline().split())
lst = [list(sys.stdin.readline().rstrip()) for _ in range(R)]
for i in range(R):
    lst[i] += lst[i][::-1]
lst2 = [[] for _ in range(R)]
for i in range(R-1, -1, -1):
    lst2[R-1-i] += lst[i][::-1]
lst += lst2
A, B = map(int, sys.stdin.readline().split())
A, B = A-1, B-1
if lst[A][B] == '.':
    lst[A][B] = '#'
else:
    lst[A][B] = '.'
for now in lst:
    print(*now, sep='')