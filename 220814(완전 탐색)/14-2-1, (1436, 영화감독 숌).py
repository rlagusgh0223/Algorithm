import sys
N = int(sys.stdin.readline())
series = 665

while N>0:
    series += 1
    if '666' in str(series):
        N-=1
        
print(series)