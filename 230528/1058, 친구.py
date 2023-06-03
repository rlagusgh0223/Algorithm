import sys
N = int(sys.stdin.readline())
friend = [list(sys.stdin.readline().rstrip()) for _ in range(N)]
cnt = [[0]*N for _ in range(N)]  # 2-친구를 저장하기 위한 리스트
ans = 0  # 가장 많은 2-친구 수
for k in range(N):  # 제 3인원(C)
    for i in range(N):
        for j in range(N):
            if i == j:  # A와 B가 동일할 경우 제외
                continue
            # A와 B가 직접 친구이거나 A와 B가 동시에 친구인 C가 있는 경우
            if friend[i][j]=='Y' or (friend[i][k]=='Y' and friend[k][j]=='Y'):
                cnt[i][j] = 1  # 혹시 이전에 계산한 인물이 나오더라도 더하는게 아닌 1로 만드는 것이므로 상관없다
for now in cnt:
    ans = max(ans, sum(now))
print(ans)