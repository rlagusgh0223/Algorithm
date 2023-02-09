import sys
i = 0
while True:
    o, w = map(int, sys.stdin.readline().split())
    if o==0 and w==0:
        break
    while True:
        ef, n = sys.stdin.readline().split()
        n = int(n)
        if ef=='#' and n==0:
            break
        if ef=='E' and w>0:
            w -= n
        elif ef=="F" and w>0:
            w += n
    i += 1
    if w <= 0:
        print(i, "RIP")  # 이 부분을 :RIP으로 출력하게 해서 계속 틀렸다. 코드 자체는 진작에 맞았다
    elif o*0.5 < w < o*2:
        print(i, ":-)")
    else:
        print(i, ":-(")