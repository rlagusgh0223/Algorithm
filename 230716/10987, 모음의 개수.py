import sys
word = list(sys.stdin.readline().rstrip())
cnt = 0
for now in word:
    if now in ('a', 'e', 'i', 'o', 'u'):
        cnt += 1
print(cnt)