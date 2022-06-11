# 슬라이딩 윈도우 알고르짐
s = str(input())    # 문자열 s를 입력받는다
bomb = str(input())    # 폭발 문자열 bomb를 입력받는다
left = []    # 문제의 시간복잡도를 사용하기 위한 스택 사용

start = 0;    # 슬라이딩 윈도우 알고리즘을 사용하기 위한 범위를 start, end에 부여
end = len(s) - 1
while start<=end:
  tof = True
  left.append(s[start])    # 스택 left에 문자열[start]값을 넣은 후 start를 1 증가시킨다
  start += 1
  if len(left) >= len(bomb):    # 스택의 크기가 폭발 문자열보다 크거나 같다면
    for i in range(len(bomb)):
      if bomb[i] != left[len(left) - len(bomb) + i]:    # 폭발 문자열 길이에 해당하는 스택 상단이 폭발 문자열과 다르다면
        tof = False    # tof=Flase로 설정해두고 for문 종료(문자열 끝과 폭발 문자열 비교)
        break
    if tof == True:    # 폭발 문자열 길이에 해당하는 스택 상단이 폭발 문자열과 같다면
      for i in range(len(bomb)):
        left.pop()    # 폭발 문자열의 길이만큼 스택의 상단을 지워준다(문자열 끝에 있는 폭발 문자열 지움)

if len(left) == 0:    # 스택의 길이가 0이라면(문자열이 비어있다면)
  print('FRULA')    # FRULA 출력
else:
  for i in range(len(left)):    # 문자열의 내용이 있다면 출력
    
    print(left[i], end='')