import sys
K = int(sys.stdin.readline())
for X in range(K):
    math = list(map(int, sys.stdin.readline().split()))
    math = sorted(math[1:])
    minm, maxm = math[0], math[-1]
    ans = 0
    for i in range(1, len(math)):
        ans = max(ans, math[i]-math[i-1])
    print("Class", X+1)
    print("Max {}, Min {}, Largest gap {}".format(maxm, minm, ans))