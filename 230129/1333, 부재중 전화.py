import sys
N, L, D = map(int, sys.stdin.readline().split())
total = N*L + (N-1)*5
song = [True] * total
for i in range(0, total, L+5):
    for j in range(i, i+L):
        song[j] = False
for i in range(0, total, D):
    if song[i]:
        print(i)
        exit()
print(i+D)