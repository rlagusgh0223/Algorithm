chef = [[int(now) for now in input().split()] for _ in range(5)]

score = cnt = 0

for i in range(5):
  if score < sum(chef[i]):
    score = sum(chef[i])
    cnt = i+1

print(cnt, score)