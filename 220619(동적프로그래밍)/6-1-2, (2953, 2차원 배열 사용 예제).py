lst = [[int(man) for man in input().split()] for _ in range(5)]

score = sum(lst[0])
cnt = 1

for i in range(1, 5):
  if score < sum(lst[i]):
    score = sum(lst[i])
    cnt = i+1

print(cnt, score)