import sys
T = int(sys.stdin.readline())
for i in range(T):
    lst = sorted(map(int, sys.stdin.readline().split()))
    if lst[0] + lst[1] <= lst[2]:    # 이 조건이 먼저 나와야 맞다고 한다
        print("Case #{}: invalid!".format(i+1))
    elif lst[0] == lst[1] == lst[2]:
        print("Case #{}: equilateral".format(i+1))
    elif lst[0]==lst[1] or lst[1]==lst[2] or lst[0]==lst[2]:
        print("Case #{}: isosceles".format(i+1))
    else:
        print("Case #{}: scalene".format(i+1))