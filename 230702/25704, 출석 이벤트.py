import sys
N = int(sys.stdin.readline())
P = int(sys.stdin.readline())
if N >= 20:
    money = P - int(max(2000, P*0.25))
elif N >= 15:
    money = P - int(max(P*0.1, 2000))
elif N >= 10:
    money = P - int(max(500, P*0.1))
elif N >= 5:
    money = P - 500
else:
    money = P
if money < 0:
    print(0)
else:
    print(money)