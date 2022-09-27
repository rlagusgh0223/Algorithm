import sys
N = int(sys.stdin.readline())
lst = [0] * 10001
for i in range(N):
    lst[int(sys.stdin.readline())] += 1
for i in range(len(lst)):
    if i != 0:
        for j in range(lst[i]):
            print(i)