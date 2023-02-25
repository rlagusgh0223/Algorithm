# 문제에선 주어지지 않았지만, 지그재그 수열이 되지 않는다면 2를 출력한다
# i, i+1, i+2가 단조증가 수열이거나 단조감소 수열인 경우 cnt를 2로 초기화해준다
# 그런지 않은 경우 지그재그 수열이므로 cnt를 1 더해준다
import sys
N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
ans = [2]
cnt = 2
for i in range(N-2):
    if A[i]<=A[i+1]<=A[i+2] or A[i]>=A[i+1]>=A[i+2]:
        cnt = 2
    else:
        cnt += 1
        ans.append(cnt)
print(max(ans))