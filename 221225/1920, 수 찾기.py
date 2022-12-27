N = int(input())
A = {now:1 for now in map(int, input().split())}
M = int(input())
for i in map(int, input().split()):
    print(A.get(i, 0))