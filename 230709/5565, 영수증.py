import sys
money = int(sys.stdin.readline())
for _ in range(9):
    money -= int(sys.stdin.readline())
print(money)