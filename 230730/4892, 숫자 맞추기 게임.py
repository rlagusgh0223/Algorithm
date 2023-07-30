import sys
TC = 0
while True:
    TC += 1
    n1 = int(sys.stdin.readline())
    if n1 == 0:
        break
    if n1 % 2 == 0:
        print("{}. even {}".format(TC, n1//2))
    else:
        print("{}. odd {}".format(TC, (n1 - 1)//2))