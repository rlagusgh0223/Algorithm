import sys
N = int(sys.stdin.readline())
lst = list(sys.stdin.readline().rstrip())
num = 0
for i in lst:
  num += int(i)
print(num)