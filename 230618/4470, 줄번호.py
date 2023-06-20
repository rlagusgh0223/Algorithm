import sys
N = int(sys.stdin.readline())
for i in range(N):
    now = sys.stdin.readline().rstrip()
    print("{}. {}".format(i+1, now))