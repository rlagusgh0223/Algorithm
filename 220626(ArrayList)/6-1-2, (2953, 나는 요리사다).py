import sys
chef = [list(map(int, sys.stdin.readline().split())) for _ in range(5)]
score = 0

for i in range(5):
  if score < sum(chef[i]):
    score = sum(chef[i])
    cnt = i+1

print(cnt, score)