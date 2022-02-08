import sys
n = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
d = A[:]    # 그냥 d = A를 하면 같은 리스트를 지칭하는 변수만 2개이므로 슬라이싱[:]을 이용하여 동일한 값을 다른 메모리에 저장하도록 해준다

for i in range(1, n):   # 앞 까지의 합 중 최대값과 자기 자신의 값을 비교하기 위해 두번째 값부터 계산 시작
    if d[i-1] + A[i] > A[i]:    # 자기 자신의 값과 앞 까지 연속된 수의 최댓값을 합 한 수 중 더 큰 값을 이번의 최댓값으로 저장
        d[i] = d[i-1] + A[i]

print(max(d))   # 저장된 연속된 최댓값들 중 가장 큰 값 호출