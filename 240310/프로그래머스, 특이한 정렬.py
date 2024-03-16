def solution(numlist, n):
    # abs(x-n)을 이용해서 n에서 가까운 순서대로 정렬한다
    # -x를 이용해 거리가 같을 경우 더 큰 값이 앞에 정렬되게 한다
    # sort()는 기본적으로 오름차순이기 때문에 -x를 쓰면 더 큰 값이 앞으로 간다
    numlist.sort(key=lambda x:(abs(x-n), -x))
    return numlist

import sys

numlist = list(map(int, sys.stdin.readline().split(", ")))
n = int(sys.stdin.readline())
print(solution(numlist, n))