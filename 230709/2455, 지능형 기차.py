import sys
human = ans = 0
for _ in range(4):
    getin, getout = map(int, sys.stdin.readline().split())
    human = human - getin + getout
    ans = max(ans, human)
print(ans)