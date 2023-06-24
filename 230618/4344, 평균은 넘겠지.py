import sys
C = int(sys.stdin.readline())
for _ in range(C):
    lst = list(map(int, sys.stdin.readline().split()))
    N = lst.pop(0)
    Csum = sum(lst) / N
    cnt = 0
    for now in lst:
        if now > Csum:
            cnt += 1
    result = cnt / N * 100
    # 무슨 원리인지는 모르겠는데 그냥 .3f로 출력하는건 이제 안된단다
    # 사사오입 문제라는데 아래 식을 이용해 반올림 하게 해야 된다
    print("{:.3f}%".format(round(result+10**(-len(str(result))-1), 3)))