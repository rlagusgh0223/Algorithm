import sys
chef = [[int(now) for now in sys.stdin.readline().split()] for _ in range(5)]

lst = []

for i in range(5):
  lst.append(sum(chef[i]))

for i in range(5):
  if sum(chef[i]) == max(lst):
    cnt = i+1
    break
print(cnt, max(lst))