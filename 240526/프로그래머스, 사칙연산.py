# -를 기준으로 나눈다면 그 사이에는 +가 있다
def solution(arr):
    # 수식을 -를 기준으로 나누고
    arrs = list(''.join(arr).split("-"))
    # 처음 -가 나오기 전까지의 부분을 합한다
    front = sum(map(int, arrs[0].split("+")))
    # -가 없다면 이미 최댓값이 나왔으므로 바로 리턴한다
    if len(arrs) == 1:
        return front
    
    minarr = maxarr = 0
    # -다음은 무조건 음수인데
    for a in arrs[:0:-1]:
        x = list(map(int, a.split('+')))
        minx = -sum(x)  # 가장 작은 음수는 다음 -가 나올때까지 합한 후 음수로 만드는 것이고
        maxx = sum(x[1:]) - x[0]  # 가장 큰 음수는 - 다음 수만 음수인 것이다
        # 최대 = max( 최대 + 누적최대, 최소 - 누적최소 )
        # 최소 = min( 최소 + 누적최소, 최소 - 누적최대 )
        minarr, maxarr = min(minx+minarr, minx-maxarr), max(maxx+maxarr, minx-minarr)
    return front + maxarr


import sys

arr = list(sys.stdin.readline().strip().split('", "'))
print(solution(arr))