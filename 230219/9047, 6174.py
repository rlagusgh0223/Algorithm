import sys
T = int(sys.stdin.readline())
for i in range(T):
    now = int(sys.stdin.readline())
    cnt = 0
    while now != 6174:
        cnt += 1
        # 어차피 4개의 문자열 숫자만 맞으면 된다
        # 0028이나 2800이나 2008이나 최대, 최소값은 같다
        if now < 1000:
            Num = str(now)
            for _ in range(4-len(Num)):
                Num += '0'
            now = int(Num)
        Max = list(str(now))
        Min = list(str(now))
        Max.sort(reverse=True)
        Min.sort()
        now = int(''.join(Max)) - int(''.join(Min))
    print(cnt)