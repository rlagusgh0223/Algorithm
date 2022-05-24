import sys
N, S = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
score = 0

def DFS(now, sum):    # 수열에서 현재의 위치를 나타낼 변수와 지금까지 값들의 합
    global score
    if now == N:
        return
    sum += arr[now]
    if sum == S:
        score += 1
    DFS(now+1, sum-arr[now])    # 현재 수열의 값을 합하지 않은상태로 다음 수열로
    DFS(now+1, sum)    # 현재 수열의 값을 합한 상태로 다음 수열로

DFS(0, 0)
print(score)






# import sys
# N, S = map(int, sys.stdin.readline().split())
# lst = list(map(int, sys.stdin.readline().split()))
# score = 0

# def DFS(idx, sum):    # 현재 정점 위치의 idx, 부분수열의 합을 저장할 sum을 입력받는다
#     global score
#     print(idx, sum)
#     if idx >= N:    # 현재 정점의 위치 idx가 N보다 크다면 종료한다
#         return
#     sum += lst[idx]    # 부분수열의 합을 저장할 sum에 현재 정점 idx 위치에 해당하는 수열의 값을 더한다
#     if S == sum:    # sum이 S와 같다면 정답의 개수를 1 더해준다
#         score += 1
#     DFS(idx+1, sum-lst[idx])    # 현재 정점의 수열을 택하지 않고 현재 정점과 연결된 다음 위치의 정점 idx+1로 이동한다
#     DFS(idx+1, sum)    # 현재 정점의 수열을 택하고 현재 정점과 연결된 다음 위치의 정점 idx+1로 이동한다

# DFS(0, 0)
# print(score)