import sys
N = int(sys.stdin.readline())
lst = list(map(int, sys.stdin.readline().split()))
answer = 1
lst.sort()
for now in lst:
    if answer < now:
        break
    answer += now
print(answer)