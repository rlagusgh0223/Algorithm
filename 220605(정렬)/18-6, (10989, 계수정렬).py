import sys
n = int(sys.stdin.readline())
number = [0] * 10000
for i in range(n):
    number[int(sys.stdin.readline())-1] += 1

for i in range(len(number)):
    if number[i] != 0:
        for j in range(number[i]):
            print(i+1)