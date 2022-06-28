import sys

chef = [list(map(int, sys.stdin.readline().split())) for _ in range(5)]

score = 0
cnt = 0

for x in range(5):
  if score < sum(chef[x]):
    score = sum(chef[x])
    cnt = x+1

print(cnt, score)