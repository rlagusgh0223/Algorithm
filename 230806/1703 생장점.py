import sys
while True:
    lst = list(map(int, sys.stdin.readline().split()))
    if lst[0] == 0:
        break
    n = 1
    for i in range(lst[0]):
        # lst[0]은 몇 살 인지를(몇 년 동안 자라고 잘라냈는지) 나타내므로 그 다음인
        # lst[1], lst[2] / lst[3], lst[4]s ... 이런식으로 계산한다
        # splitting facotr를 곱한 만큼 전년도 보다 가지가 늘어난다
        sf = lst[2*i + 1]
        # cut 만큼 가지를 잘라준다
        cut = lst[2*i + 2]
        n = n * sf - cut
    print(n)