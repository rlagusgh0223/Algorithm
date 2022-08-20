def DFS(idx, sum):    # 현재 정점의 위치(idx), 부분수열의 합(sum)을 입력받는다
    global answer
    if idx>=n:
        return
    sum += arr[idx]    # 부분수열의 합을 저장할 sum에 현재 정점idx위치에 해당하는 수열의 값을 더한다.
    if s==sum:
        answer += 1
    DFS(idx+1, sum-arr[idx])    # 현재 정점의 수열을 택하지 않고 현재 정점과 연결된 다음 위치의 정점으로 이동
    DFS(idx+1, sum)    # 현재 정점의 수열을 택하고 현재 정점과 연결된 다음 위치의 정점으로 이동

n, s = map(int, input().split())
arr = list(map(int, input().split()))
answer = 0
DFS(0, 0)
print(answer)