import sys
s = sys.stdin.readline().rstrip()
bomb = sys.stdin.readline().rstrip()
left = []
start = 0
end = len(s)-1

while start<=end:
  left.append(s[start])
  start += 1
  chk = True
  if len(left) >= len(bomb):
    for i in range(len(bomb)):
      if bomb[i] != left[len(left) - len(bomb) + i]:
        chk = False
        break
    if chk:
      for i in range(len(bomb)):
        left.pop()

if len(left) == 0:
  print("FRULA")
else:
  for i in left:
    print(i, end='')