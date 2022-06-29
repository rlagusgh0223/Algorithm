chef = [list(map(int, input().split())) for _ in range(5)]
score = 0
cnt = 0
for i in range(5):
  if score < sum(chef[i]):
    score = sum(chef[i])
    cnt = i+1

print(cnt, score)