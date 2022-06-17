word = input()    # 첫째줄에 주어지는 문자열
bomb = input()    # 폭발 문자열
lst = []    # 문자열과 폭발문자열을 비교하기 위해 사용할 리스트

start = 0    # 리스트 계산할 때 쓸 맨 앞과 뒤의 수
end = len(word) - 1

while start<=end:    # 전부다 체크하도록 start와 end가 같아질때까지 반복
  lst.append(word[start])    # 문자열의 처음부터 하나씩 입력하며 비교
  start += 1    # 다음 문자를 받기 위해 start의 값 1 증가
  chk = True    # 폭발 문자열과 같다면 True, 한번이라도 안맞으면 False
  if len(lst) >= len(bomb):    # 확인하고자 하는 문자열의 길이가 어차피 폭발문자열보다 짧다면 확인하고 말고도 없다
    for i in range(len(bomb)):    # 폭발 문자열의 길이만큼 검색
      if bomb[i] != lst[len(lst) - len(bomb) + i]:    # 폭발문자열과 다른 부분이 하나라도 있다면 해당되지 않으므로
        chk = False
        break
    if chk:    # 폭발 문자열과 일치하다면 폭발 문자열 제거
      for i in range(len(bomb)):
        lst.pop()

if len(lst)==0:    # 문자열의 길이가 없다면 전부 폭발 문자열이므로 FRULA출력
  print("FRULA")
else:
  print("".join(lst))    # 그게 아니라면 리스트 내용 공백 없이 출력