import sys
# 작은 두 변의 길이의 합이 긴 변의 길이보다 커야된다
abc = sorted(map(int, sys.stdin.readline().split()))
print(abc[0] + abc[1] + min(abc[2], abc[0]+abc[1]-1))