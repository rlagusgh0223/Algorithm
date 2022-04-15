import sys
rec = [0] * 3
x = [0] * 1001
y = [0] * 1001
for i in range(3):
    rec[i] = list(map(int, sys.stdin.readline().split()))

for i in range(3):
    x[rec[i][0]] += 1
    y[rec[i][1]] += 1

for i in range(3):
    if x[rec[i][0]] == 1:
        print(rec[i][0], end=' ')
for i in range(3):
    if y[rec[i][1]] == 1:
        print(rec[i][1])