import sys
N = int(sys.stdin.readline())
for now in range(N, 3, -1):
    ck = True
    for number in str(now):
        if int(number)!=4 and int(number)!=7:
            ck = False
            break
    if ck:
        print(now)
        break