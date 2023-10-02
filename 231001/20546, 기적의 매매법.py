import sys
money = int(sys.stdin.readline())
MD = list(map(int, sys.stdin.readline().split()))
BM = TM = money
BD = TD = 0
for now in range(len(MD)):
    # 준현(BNP)
    if BM >= MD[now]:
        BD += BM // MD[now]
        BM %= MD[now]
        # print("준현", now+1,"일", BD, BM)

    # 성민(TIMING)
    if now >= 3:
        if MD[now-3] < MD[now-2] < MD[now-1] and TD > 0:
            TM += TD * MD[now]
            TD = 0
            # print("상민 매도", now+1,"일", TD, TM)
        elif MD[now-3] > MD[now-2] > MD[now-1] and TM > MD[now]:
            TD += TM // MD[now]
            TM %= MD[now]
            # print("상민 매수", now+1,"일", TD, TM)

# print(BM + BD*MD[-1])
# print(TM + TD*MD[-1])
if (BM + BD*MD[-1]) > (TM + TD*MD[-1]):
    print("BNP")
elif (BM + BD*MD[-1]) < (TM + TD*MD[-1]):
    print("TIMING")
else:
    print("SAMESAME")