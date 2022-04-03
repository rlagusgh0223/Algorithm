import sys
n = int(sys.stdin.readline())
for i in range(n):
    r, e, c = map(int, sys.stdin.readline().split())
    if r == e-c:    # 광고를 하지 않았을 때와 광고 비용을 뺀 광고 이익의 수익이 같은 경우
        print("does not matter")
    elif r > e-c:    # 광고를 하지 않았을 때의 수익이 광고 이익을 뺀 광고 했을 때의 수익보다 많은 경우
        print("do not advertise")
    elif r < e-c:    # 광고를 하지 않았을 때의 수익이 광고 이익을 뺀 광고 했을 때의 수익보다 적을 경우
        print("advertise")