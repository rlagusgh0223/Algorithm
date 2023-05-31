# pypy3로 돌려야 된다
def search(target, start, end):
    if start > end:
        return None
    mid = (start+end)//2
    # 찾은 경우 중간점 인덱스 반환
    if D[mid] == target:
        return mid
    # 중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
    elif D[mid] > target:
        return search(target, start, mid-1)
    # 중간점의 값보다 찾고자 하는 값이 큰 경우 오른쪽 확인
    else:
        return search(target, mid+1, end)

import sys
while True:
    N, M = map(int, sys.stdin.readline().split())
    if N==0 and M==0:
        break
    C = [int(sys.stdin.readline()) for _ in range(N)]
    D = [int(sys.stdin.readline()) for _ in range(M)]
    cnt = 0
    for now in C:
        if search(now, 0, len(D)-1) != None:
            cnt += 1
    print(cnt)