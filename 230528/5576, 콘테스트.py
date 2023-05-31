# sort를 사용하면 쉽지만 정렬에 익숙해지기 위해 퀵 정렬을 사용해보겠다
# 퀵 정렬은 피벗을 설정 후, 왼쪽에서부터 피벗보다 큰 수를, 오른쪽에서부터 피벗보다 작은 수를 구해서 서로 교환해주는 정렬이다
def quick(array, start, end):
    if start >= end:
        return
    pivot = start  # 피벗은 첫번째 원소
    left = start + 1
    right = end
    while left <= right:
        # 피벗보다 큰 데이터를 찾을 때까지 반복
        while left<=end and array[left]<=array[pivot]:
            left += 1
        # 피벗보다 작은 데이터를 찾을 때까지 반복
        while right>start and array[right]>=array[pivot]:
            right -= 1
        # 엇갈렸다면 작은 데이터와 피벗을 교체
        if left > right:
            array[right], array[pivot] = array[pivot], array[right]
        # 엇갈리지 않았다면 작은 데이터와 큰 데이터를 교체
        else:
            array[left], array[right] = array[right], array[left]
    quick(array, start, right-1)
    quick(array, right+1, end)

import sys
W = [int(sys.stdin.readline()) for _ in range(10)]
K = [int(sys.stdin.readline()) for _ in range(10)]
quick(W, 0, len(W)-1)
quick(K, 0, 9)
print(sum(W[-3:]), sum(K[-3:]))