# 가장 긴 증가하는 부분수열 응용 문제
# 둘 중 하나의 배열을 기준으로 정렬 후(내 풀이에서는 A)
# 반대 정렬에서 가장 긴 증가하는부분수열을 구하고(내 풀이에서는 B)
# 총 길이에서 가장 긴 증가하는 부분수열의 길이만큼 빼주면 된다
import sys
N = int(sys.stdin.readline())
A = [0] * N
chk = [1] * N
for i in range(N):
    A[i] = list(map(int, sys.stdin.readline().split()))
A.sort(key=lambda x:x[0])  # 0번째 배열을 기준으로 오름차순 정렬
for i in range(N):
    for j in range(i):
        if A[j][1]<A[i][1] and chk[j]>=chk[i]:
            chk[i] = chk[j] + 1
print(N - max(chk))