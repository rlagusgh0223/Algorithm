N = int(input())
lst = list(map(int, input().split()))
max_num = lst[0]
min_num = lst[0]

for i in range(1, N):
  if max_num<lst[i]:
    max_num = lst[i]
  elif min_num>lst[i]:
    min_num = lst[i]

print(min_num, max_num)