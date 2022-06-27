N = int(input())
lst = list(map(int, input().split()))

max_score = lst[0]
min_score = lst[0]

for i in range(1, N):
  if max_score < lst[i]:
    max_score = lst[i]
  elif min_score > lst[i]:
    min_score = lst[i]

print(min_score, max_score)