def quick(N, start, end):
    if start >= end:
        return
    pivot = start
    left = start + 1
    right = end
    while left <= right:
        # 피벗보다 큰 데이터를 찾을 때까지 반복
        while left<=end and N[left]<=N[pivot]:
            left += 1
        # 피벗보다 작은 데이터를 찾을때가지 반복
        while right>start and N[right]>=N[pivot]:
            right -= 1
        # 엇갈렸다면 작은 데이터와 피벗을 교체
        if left > right:
            N[right], N[pivot] = N[pivot], N[right]
        # 엇갈리지 않았다면 작은 데이터와 큰 데이터를 교체
        else:
            N[left], N[right] = N[right], N[left]
    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행
    quick(N, start, right-1)
    quick(N, right+1, end)

import sys
T = int(sys.stdin.readline())
for _ in range(T):
    N = list(map(int, sys.stdin.readline().split()))
    quick(N, 0, len(N)-1)
    if N[-2] - N[1] >= 4:
        print("KIN")
    else:
        print(sum(N[1:-1]))