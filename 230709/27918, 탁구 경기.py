import sys
N = int(sys.stdin.readline())
X = Y = 0
for _ in range(N):
    winner = sys.stdin.readline().rstrip()
    if winner == 'D':
        X += 1
    else:
        Y += 1
    if abs(X-Y) >= 2:
        break
print("{}:{}".format(X, Y))