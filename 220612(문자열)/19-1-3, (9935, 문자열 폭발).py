s = input()
bomb = input()
start = 0
end = len(s) - 1
lst = []

while start<=end:
  lst.append(s[start])
  start+=1
  chk = True
  if len(lst) >= len(bomb):
    for i in range(len(bomb)):
      if bomb[i] != lst[len(lst) - len(bomb) + i]:
        chk = False
        break
    if chk:
      for i in range(len(bomb)):
        lst.pop()

if len(lst) == 0:
  print("FRULA")
else:
  for word in lst:
    print(word, end='')