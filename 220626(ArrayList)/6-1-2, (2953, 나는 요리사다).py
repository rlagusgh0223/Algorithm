chef = [[int(now) for now in input().split()] for _ in range(5)]    # 요리사들의 점수 입력

cnt = 0    # 몇번째 요리사인지 저장할 변수
score = 0    # 최고 점수를 저장할 변수

for i in range(5):
  if score < sum(chef[i]):    # 최고점수가 현재 요리사 점수의 총합보다 작다면
    cnt = i+1    # 몇번째 요리사인지 기록
    score = sum(chef[i])    # 최고점수 수정

print(cnt, score)    # 순서와 점수 출력