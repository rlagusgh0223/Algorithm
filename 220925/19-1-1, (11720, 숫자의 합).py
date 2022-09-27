import sys
N = int(sys.stdin.readline())
num = list(sys.stdin.readline().rstrip())
answer = 0
for now in num:
    answer += int(now)
print(answer)