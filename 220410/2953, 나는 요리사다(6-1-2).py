import sys
cnt = 0    # 요리사의 번호를 출력할 변수
result = []    # 각 요리사가 받은 점수를 합할 리스트
for i in range(5):    # 입력받은 5명의 점수를 기록하는 리스트(요리사의 4점수 합산)
    result.append(sum(list(map(int, sys.stdin.readline().split()))))

while True:
    if result[cnt] == max(result):    # 우승자는 항상 유일. 현재의 값이 최댓값이면 그 사람이 우승자
        print(cnt+1, max(result))    # 우승자의 번호와 점수 출력
        break
    cnt += 1