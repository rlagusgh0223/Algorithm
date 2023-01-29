import sys
N = int(sys.stdin.readline())
lst = [int(x) for x in range(N+1)]
while len(lst) != 2:
    del lst[1::2]
print(lst[1])