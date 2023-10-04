import sys
number = [0] * 10
for i in range(5):
    now = int(sys.stdin.readline())
    number[now] = (number[now]+1) % 2
print(number.index(1))