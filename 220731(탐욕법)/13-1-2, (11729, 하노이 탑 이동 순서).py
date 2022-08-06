import sys
def hanoi(N, start, to, end):    # 원판의 수, 시작위치, 중간위치, 종료위치
    if N == 1:    # 원판 N이 1이라면, start에서 end로 이동을 출력해준다.
        print(start, end)
    else:
        hanoi(N-1, start, end, to)    # N-1개의 원판을 start에서 end를 거쳐 to로 간다
        print(start, end)    # 원판 N을 start에서 end로 이동을 출력해준다
        hanoi(N-1, to, start, end)    # N-1개의 원판을 to부터 시작해서 start를 거쳐 end로 이동시킨다

N = int(sys.stdin.readline())
print(2**N - 1)    # 원판을 총 옮겨야 되는 횟수
hanoi(N, 1, 2, 3)