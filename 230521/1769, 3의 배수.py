import sys
X = [int(x) for x in sys.stdin.readline().rstrip()]
cnt = 0
while len(X)>1:
    cnt += 1
    x = sum(X)
    X = list(map(int, str(x)))
print(cnt)
if X[0]%3 == 0:
    print("YES")
else:
    print("NO")