import sys
input = sys.stdin.readline
L = int(input())
N = int(input())
cake = [0] * (L+1)
man = [0] * (N+1)
for i in range(1, N+1):
    x, y = map(int, input().split())
    man[i] = y-x
    for j in range(x, y+1):
        if cake[j] == 0:
            cake[j] = i
print(man.index(max(man)))
man = [0] * (N+1)
for i in range(1, N+1):
    for j in range(1, L+1):
        if cake[j] == i:
            man[i] += 1
print(man.index(max(man)))