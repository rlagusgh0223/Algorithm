def Rev(x):
    return int(x[::-1])

import sys
X, Y = sys.stdin.readline().split()
print(Rev(str(Rev(X) + Rev(Y))))