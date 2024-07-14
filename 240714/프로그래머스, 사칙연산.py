def solution(arr):
    # -를 기준으로 나누면 그 정수만 있거나(문자로 있다)
    # +를 포함한 정수문자열이 남는다
    arr = list(''.join(arr).split("-"))
    front = sum(map(int, arr[0].split("+")))
    # -가 없는 경우 그 자체가 최대값이다
    if len(arr) == 1:
        return front
    
    minarr = maxarr = 0
    # arr[1:] 로 계산하면 다른 결과가 나온다
    for a in arr[:0:-1]:
        x = list(map(int, a.split("+")))
        # 현재 문자열에서 가장 작은 음수는 -다음의 모든 수를 더한 값이다
        minx = -sum(x)
        # 현재 문자열에서 가장 큰 음수는 -바로 다음값만 -에 참가했을때다
        maxx = sum(x[1:]) - x[0]
        # 최대 = max(최대+누적최대, 최소-누적최소)
        # 최소 = min(최소+누적최소, 최소-누적최대)
        # 이 계산을 한줄에서 시행해야 된다
        # 각 연산에 누적최대, 누적최소가 들어가므로
        # 하나라도 먼저 시행하면 그 값으로 연산하기 때문에 값이 달라진다
        minarr, maxarr = min(minx+minarr, minx-maxarr), max(maxx+maxarr, minx-minarr)

    return front + maxarr

import sys

print(solution(list(sys.stdin.readline().strip().split('", "'))))







# # -를 기준으로 나눈다면 그 사이에는 +가 있다
# def solution(arr):
#     # 수식을 -를 기준으로 나누고
#     arrs = list(''.join(arr).split("-"))
#     # 처음 -가 나오기 전까지의 부분을 합한다
#     front = sum(map(int, arrs[0].split("+")))
#     # -가 없다면 이미 최댓값이 나왔으므로 바로 리턴한다
#     if len(arrs) == 1:
#         return front
    
#     minarr = maxarr = 0
#     # -다음은 무조건 음수인데
#     for a in arrs[:0:-1]:
#         x = list(map(int, a.split('+')))
#         minx = -sum(x)  # 가장 작은 음수는 다음 -가 나올때까지 합한 후 음수로 만드는 것이고
#         maxx = sum(x[1:]) - x[0]  # 가장 큰 음수는 - 다음 수만 음수인 것이다
#         # 최대 = max( 최대 + 누적최대, 최소 - 누적최소 )
#         # 최소 = min( 최소 + 누적최소, 최소 - 누적최대 )
#         minarr, maxarr = min(minx+minarr, minx-maxarr), max(maxx+maxarr, minx-minarr)
#     return front + maxarr