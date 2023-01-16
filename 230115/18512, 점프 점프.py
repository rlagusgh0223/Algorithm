import sys
X, Y, P1, P2 = map(int, sys.stdin.readline().split())
lst1 = [0] * 200  # 최댓값이 지정되어 있지 않아 그냥 임의로 줬다.
lst2 = [0] * 200
for i in range(200):
    p1 = P1+X*i
    p2 = P2+Y*i
    lst1[i] = p1
    lst2[i] = p2
    if p1 in lst2:
        print(p1)
        exit()
    elif p2 in lst1:
        print(p2)
        exit()
print(-1)