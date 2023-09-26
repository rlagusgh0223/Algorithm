# pypy3로 해야된다
import sys
N, M = map(int, sys.stdin.readline().split())
student = [[0]*N for _ in range(N)]
for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    student[a-1][b-1] = 1

# 플로이드 워셜 알고리즘
for k in range(N):
    for i in range(N):
        for j in range(N):
            if student[i][k]==1 and student[k][j]==1:
                student[i][j] = 1

# 자신의 키가 몇 번째인지 아는 사람 계산
ans = 0
for i in range(N):
    check = 0
    for j in range(N):
        check += student[i][j] + student[j][i]
    # check 가 N-1이라는건 자신을 제외한 나머지와 연결됐다는 의미이므로 모두와 연결됐다는 뜻이다
    # 즉, 자기보다 큰 사람과 작은 사람을 다 안다는 의미다
    if check == N-1:
        ans += 1

print(ans)