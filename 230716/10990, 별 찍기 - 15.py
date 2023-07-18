import sys
N = int(sys.stdin.readline())
for i in range(N):
    if i == 0:
        print("{}{}".format(" "*(N-i-1), "*"))
        continue
    print("{}{}{}{}".format(" "*(N-i-1), "*", " "*(2*i-1), "*"))