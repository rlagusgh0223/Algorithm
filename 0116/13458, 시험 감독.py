import sys
N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
B, C = map(int, sys.stdin.readline().split())

cnt = 0

for i in range(N):
    if A[i] <= B:   # 총감독관 혼자서 담당할 수 있는 인원보다 응시 인원이 적으면 총감독관 1명만 있으면 된다
        cnt += 1
    else:
        a = A[i] - B
        if a <= C:  # 총감독관이 담당할 수 있는 인원보다 많으며, 부감독관이 혼자서 담당할 수 있는 인원이면 총감독관, 부감독관 1명씩만 있으면 된다
            cnt = cnt + 1 + 1
        elif a > C and a % C == 0:  # 부감독관이 담당할 수 있는 인원으로 나누어 떨어지면 남은 인원을 담당 가능 인원으로 나누고 그 몫과 총감독관 1명을 더해준다
            cnt = cnt + (a//C) + 1
        elif a > C and a % C != 0:  # 부감독관이 담당할 수 있는 인원으로 나누어 떨어지지 않으면 총감독관, 나누어떨어지는 부감독관 + 1명의 부감독관을 더 둔다
            cnt = cnt + (a//C) + 1 + 1

print(cnt)