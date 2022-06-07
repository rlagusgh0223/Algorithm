import sys
N = int(sys.stdin.readline())
lst = []
for i in range(N):
    age, name = sys.stdin.readline().split()
    lst.append([int(age), name])

lst.sort(key=lambda x:x[0])

for now in lst:
    print(now[0], now[1])