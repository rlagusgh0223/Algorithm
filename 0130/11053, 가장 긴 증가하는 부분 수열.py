import sys
n = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))    # 각 열의 값을 받는 리스트
D = [1] * n     # 각 열의 길이를 적기 위한 리스트. 그 자체로도 하나의 길이가 되므로 1로 초기값을 잡는다

for i in range(n):                          # 리스트의 수를 한 번씩 수행
    for j in range(i):                      # 처음부터 리스트의 수 바로 앞까지 확인
        if A[i] > A[j] and D[i] <= D[j]:    # 만약 현재 리스트의 수가 앞의 리스트의 수보다 큰데 수열의 길이가 짧거나 같다면
            D[i] = D[j] + 1                 # 앞의 수열의 길이 + 1

print(max(D))   # 수열에서 가장 긴 부분을 찾아야 되므로