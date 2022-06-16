word = input()
bomb = input()
lst = []
start = 0
end = len(word)-1

while start<=end:
  lst.append(word[start])
  start += 1
  chk = True
  if len(lst) >= len(bomb):
    for i in range(len(bomb)):
      if bomb[i] != lst[len(lst)-len(bomb)+i]:
        chk = False
        break
    if chk:
      for i in range(len(bomb)):
        lst.pop()

if len(lst)==0:
  print("FRULA")
else:
  print("".join(lst))