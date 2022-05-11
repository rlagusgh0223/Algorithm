import sys
N = int(sys.stdin.readline())
cnt = 0    # 1부터 666이 있는지 계속 비교하기 위한 변수

while N > 0:    # N이 0보다 크면 계속 반복
    cnt += 1    # 1부터 비교하기 위해 1씩 더한다
    if '666' in str(cnt):    # cnt의 값 중 666이 들어있다면
        N -= 1    # 하나 해당사항 있는것이므로 1 뺀다

print(cnt)    # 1부터 시작해서 N번째 666이 들어있는 수 출력