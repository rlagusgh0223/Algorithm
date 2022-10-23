import sys
while True:
    try:
        n = int(sys.stdin.readline())
    except:
        break
    num = 0
    now = 1
    while True:
        num = num*10 + 1
        num %= n
        if num==0:
            print(now)  # 자리수를 출력하라고 했으므로 ex) 1111 -> 4 출력
            break
        now += 1