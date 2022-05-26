import sys
N, S = map(int, sys.stdin.readline().split())
lst = list(map(int, sys.stdin.readline().split()))
score = 0

def DFS(now, sum):    # 리스트의 현재 위치와 지금까지 더한 값 입력받아 함수 시작
    global score
    if now == N:    # 리스트의 끝까지 오면 이번 계산은 종료
        return
    sum += lst[now]    # sum에 lst의 현재 좌표가 가리키는 값을 더한다
    if sum == S:    # sum이 목표값을 달성하면 가능횟수를 1 더한다
        score += 1
    DFS(now+1, sum-lst[now])    # 다음에 DFS로 넘어갈 때 지금 값을 더하지 않은 값을 넘겨준다
    DFS(now+1, sum)    # 다음에 DFS로 넘어갈 때 지금 값을 더한 값을 넘겨준다

DFS(0, 0)    # 처음 시작이니까 위치와 합을 0으로 DFS 호출
print(score)    # 가능한 모든 경우의 수 호출