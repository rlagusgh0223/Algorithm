import sys
s = sys.stdin.readline().rstrip()
bomb = sys.stdin.readline().rstrip()
left = []

start = 0
end = len(s)-1
while start<=end:
  check = True
  left.append(s[start])
  print(left)
  start += 1
  if len(left) >= len(bomb):
    for i in range(len(bomb)):
      if bomb[i] != left[len(left) - len(bomb) + i]:
        print(len(left) - len(bomb) + i)
        print(left)
        check = False
        break
    if check == True:  # 폭발문자열과 동일한 문자열이 left에 있다면
      for i in range(len(bomb)):  # 폭발문자열의 길이만큼
        left.pop()  # left에서 빼버린다

if len(left)==0:
  print("FRULA")
else:
  for i in left:
    print(i, end='')