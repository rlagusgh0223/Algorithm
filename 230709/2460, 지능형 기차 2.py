import sys
cnt = 0
human = 0
for _ in range(10):
    getout, getin = map(int, sys.stdin.readline().split())
    human = human - getout + getin
    cnt = max(cnt, human)
print(cnt)