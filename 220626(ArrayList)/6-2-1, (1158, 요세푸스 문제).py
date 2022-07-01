from collections import deque
N, K = map(int, input().split())    # 입력값 입력
lst = deque([int(now) for now in range(1, N+1)])    # 1부터 N까지의 수만큼 리스트 입력
answer = []    # 빠지는 수들을 저장할 리스트
cnt = 0    # 빠질 타이밍을 계산하기 위한 변수

while lst:    # 빠질 수열이 있는한 반복
  cnt += 1
  now = lst.popleft()    # 가장 앞에 있는 사람 이동
  if cnt == K:    # 한 명이 빠질 타이밍이면
    answer.append(str(now))    # answer로 보낸다(join은 문자를 합치는 함수라 문자로 선언해준다)
    cnt = 0    # 다음 계산을 위해 cnt를 0으로 초기화해준다
  else:    # 빠질 타이밍이 아니면
    lst.append(now)    # 다시 뒤로 들어간다

print("<", end='')    # 문제에서 요구한 모양으로 출력하기 위해 print를 나눠서 출력
print(", ".join(answer), end='')    # 문자열을 ', '로 구분하여서 합쳐서 출력
print(">")