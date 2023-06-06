def search(array, target, start, end):
    if start > end:
        return 0
    mid = (start+end) // 2
    if array[mid] == target:
        return 1
    # 중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
    elif array[mid] > target:
        return search(array, target, start, mid-1)
    # 중간점의 값보다 찾고자 하는 값이 큰 경우 오른쪽 확인
    else:
        return search(array, target, mid+1, end)

import sys
T = int(sys.stdin.readline())
for _ in range(T):
    N = int(sys.stdin.readline())
    N1 = list(map(int, sys.stdin.readline().split()))
    N1.sort()  # 이분탐색은 정렬되어 있는 데이터에 대해서 작업해야 돌아간다
    M = int(sys.stdin.readline())
    M1 = list(map(int, sys.stdin.readline().split()))
    for now in M1:
        print(search(N1, now, 0, N-1))