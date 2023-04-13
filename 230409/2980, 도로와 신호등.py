import sys
N, L = map(int, sys.stdin.readline().split())
now = 0  # 지금 위치
ans = 0  # 현재까지 걸린 시간
for _ in range(N):
    D, R, G = map(int, sys.stdin.readline().split())
    ans += D - now  # 거리와 시간이 같으므로 다음 신호등과 지금 위치의 거리만큼이 다음 신호등까지 이동 시간이다
    now = D  # 다음 신호등까지 이동했으므로 위치를 다음 신호등 위치로 바꿔준다
    if ans % (R+G) <= R:  # 빨+녹 시간이 한 사이클이고, 아직 빨간불이 켜져 있는 동안이라면
        ans += R - (ans % (R+G))  # 빨간불이 앞으로 켜지는 시간만큼 대기한다
ans += L - now  #  신호등을 지나고 길의 끝까지는 장애물이 없으므로 남은 거리 그대로 다 더해주면 된다
print(ans)