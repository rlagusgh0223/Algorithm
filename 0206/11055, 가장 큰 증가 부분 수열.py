import sys
N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
d = [0] * N     # 각 값을 더한 값이 어떤지 파악하기 위한 리스트

for i in range(N):
    d[i] = A[i] # 수열이 되지 않을 수 있으니 자기 자신의 값을 리스트에 넣어둔다
    for j in range(i+1):
        if A[i] > A[j] and d[i] <= d[j] + A[i]: # 증가하는 수열이니까 당연히 지금 내 값보다 작은 값인지 확인하고 | 그 값까지의 합과 내 값을 더했을 때 지금까지의 합보다 큰지 확인
            d[i] = d[j] + A[i]  # 앞의 값과 내 값을 더한 값을 입력한다

print(max(d))   # 구한 값 중 최고값을 출력