def solution(sticker):
    if len(sticker) == 1:
        return sticker[-1]
    
    # 첫번째 스티커부터 떼면 마지막 스티커는 떼지 못한다
    dp1 = [0] + sticker[:-1]
    # 마지막 스티커를 떼려면 두번째 스티커부터 떼야 한다
    dp2 = [0] + sticker[1:]

    # 현재 위치의 최댓값은 이전값과 전전값+현재값 중 큰 값이다
    # [0, 14, 6, 5] -> [0, 14, 14, 5] -> [0, 14, 14, 19]
    for i in range(2, len(sticker)):
        dp1[i] = max(dp1[i-1], dp1[i-2]+dp1[i])
        dp2[i] = max(dp2[i-1], dp2[i-2]+dp2[i])
    
    return max(dp1[-1], dp2[-1])


import sys

sticker = list(map(int, sys.stdin.readline().split(", ")))
print(solution(sticker))