import sys
N = int(sys.stdin.readline())

number = [int(now) for now in sys.stdin.readline().split()]

max_score = number[0]
min_score = number[0]

for x in range(N):
  if max_score < number[x]:
    max_score = number[x]
  elif min_score > number[x]:
    min_score = number[x]

print(min_score, max_score)