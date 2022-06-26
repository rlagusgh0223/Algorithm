import sys
N = int(sys.stdin.readline())
lst = [int(now) for now in sys.stdin.readline().split()]
max_score = min_score = lst[0]

for i in range(1, N):
  if max_score < lst[i]:
    max_score = lst[i]
  elif min_score > lst[i]:
    min_score = lst[i]

print(min_score, max_score)