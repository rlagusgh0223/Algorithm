def solution(stones, k):
    answer = 0
    # 이진탐색을 이용한 풀이
    # 주어진 값 중 가장 작은값을 왼쪽,
    # 큰 값을 오른쪽에 있다고 가정하고 푼다
    l, r = 1, max(stones)
    while l <= r:
        mid = (l+r) // 2
        ck = 0  # 건너지 못하는 디딤돌의 수를 체크하는 변수
        for stone in stones:
            if stone-mid <= 0:
                ck += 1
            else:
                ck = 0
            # 연속으로 건너지 못하는 디딤돌이 k만큼 있을때 반복문 종료
            # 이거 없으면 만약 이후에 0이 아닌것이 나오면 ck는 다시 0이되고
            # 건너뛸 수 없는 상황임에도 건너뛸 수 있다고 계산할 수 있다
            if ck == k:
                break
        # 여기서 l, r은 거리가 아닌 원하는 값을 구하기 위한 변수이므로
        # 이진탐색을 이용해 건널 수 없는 디딤돌이 연속으로 k개 나올때까지
        # 지나가는 사람 수(mid)를 구하도록 l, r의 값을 조정한다
        if ck < k:
            l = mid + 1
        else:
            answer = mid
            r = mid - 1
    return answer

import sys

stones = list(map(int, sys.stdin.readline().split(", ")))
k = int(sys.stdin.readline())
print(solution(stones, k))