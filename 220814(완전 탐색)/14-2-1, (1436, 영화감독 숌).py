import sys
N = int(sys.stdin.readline())
now = 665

while N>0:
    now += 1
    if '666' in str(now):
        N -= 1

print(now)