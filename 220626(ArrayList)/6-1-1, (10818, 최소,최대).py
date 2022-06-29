N = int(input())
number = list(map(int, input().split()))
Max = number[0]
Min = number[0]

for i in range(1, N):
  if Max < number[i]:
    Max = number[i]
  elif Min > number[i]:
    Min = number[i]

print(Min, Max)