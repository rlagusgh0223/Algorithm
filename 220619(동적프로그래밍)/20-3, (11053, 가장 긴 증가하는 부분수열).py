import sys
N = int(sys.stdin.readline())    # 수열 A의 크기 입력
A = [int(num) for num in sys.stdin.readline().split()]    # 수열 A를 이루고 있는 수 입력
chk = [1] * N    # 증가하는 수열의 길이를 체크하기 위한 리스트. 모든 수는 자시자신도 포함하므로 1부터 시작한다

for i in range(N):    # 모든 수 점검
  for j in range(i):    # 현재 점검 중인 수 앞에까지의 수 비교
    if A[i]>A[j] and chk[i]<=chk[j]:    # 만약 현재의 수가 앞의 수보다 크고, 그 수까지의 수열의 길이보다 작다면
      chk[i] = chk[j]+1    # 현재까지 수열의 길이를 앞의 수까지의 수열의 길이보다 1 증가시킨다

print(max(chk))    # 수열의 길이 중 가장 긴 수열 출력