import sys
n = int(sys.stdin.readline())
A = [0]     # 시작점은 계단에 포함되지 않으므로 0으로 입력해서 계산에 방해가 되지 않게 한다
for i in range(n):
    A.append(int(sys.stdin.readline()))

if n == 1:  # n이 1이거나 2일땐 아래의 식을 진행할 수 없음
    print(A[1])
else:   # n이 3 이상 일때
    # d는 각 단계에서 가질 수 있는 최대값
    d = [0, A[1], A[1]+A[2]]    # 시작점은 어차피 값이 없으니까 0으로 한다

    for i in range(3, n+1):
        d.append(max(d[i-2]+A[i], d[i-3]+A[i-1]+A[i]))  # 계단 오르기 점화식(한 칸 떨어진 계단과 더하거나, 바로 붙고 거기서 한칸 떨어진 계단의 합 중 큰 값 입력)

    # 마지막 계단을 반드시 밟으라고 했으므로 마지막 d값을 출력
    # 0을 주고 n개의 리스트를 입력하니까 d[n-1]이 아닌 d[n]이 마지막 값이 된다
    print(d[n])