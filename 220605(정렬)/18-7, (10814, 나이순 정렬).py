import sys
N = int(sys.stdin.readline())
lst = []
for i in range(N):
    x, y = sys.stdin.readline().split()
    lst.append([int(x), y])

lst.sort(key=lambda x:x[0])

for i in lst:
    print(i[0], i[1])