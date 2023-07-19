import sys
T = int(sys.stdin.readline())
for _ in range(T):
    a, b = map(int, sys.stdin.readline().split())
    money = 0
    if a == 0:
        money += 0
    elif a <= 1:
        money += 5000000
    elif a <= 1+2:
        money += 3000000
    elif a <= 1+2+3:
        money += 2000000
    elif a <= 1+2+3+4:
        money += 500000
    elif a <= 1+2+3+4+5:
        money += 300000
    elif a <= 1+2+3+4+5+6:
        money += 100000

    if b == 0:
        money += 0
    elif b <= 1:
        money += 5120000
    elif b <= 1+2:
        money += 2560000
    elif b <= 1+2+4:
        money += 1280000
    elif b <= 1+2+4+8:
        money += 640000
    elif b <= 1+2+4+8+16:
        money += 320000
    print(money)