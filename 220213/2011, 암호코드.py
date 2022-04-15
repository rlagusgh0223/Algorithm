import sys
n = list(str(sys.stdin.readline().strip()))
d = [0 for _ in range(len(n) + 1)]
d[0], d[1] = 1, 1

if n[0] == '0':    # 첫 수부터 0이 나오면 암호가 잘못 입력된 것이므로 0을 출력한다
    print(0)
else:
    for i in range(2, len(n) + 1):
        if int(n[i-1]) > 0:    # A ~ I 일 경우 한자리 숫자로 계산
            d[i] += d[i-1]
            #print(i, "한자리수 :",d[i])

        to_int = int(n[i-2])*10 + int(n[i-1])
        if 10 <= to_int <= 26:    # J ~ Z 일 경우
            d[i] += d[i-2]
            #print(i, "두자리수 :",d[i])
    print(d[len(n)] % 1000000)