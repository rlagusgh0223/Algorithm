import sys
money = 1000 - int(sys.stdin.readline())
coins = [500, 100, 50, 10, 5, 1]
cnt = 0
for coin in coins:
    cnt += money//coin
    money %= coin
print(cnt)