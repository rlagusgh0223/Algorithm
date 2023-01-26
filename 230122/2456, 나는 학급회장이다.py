# 인터넷 참고하였음
# 최고 점수가 같다면 점수를 받을때마다 제곱한 값의 합을 비교한다
# 3점을 받으면 9점이 더해지고, 2점을 받으면 4점이 더해지므로 확실하게 비교가 된다
import sys
N = int(sys.stdin.readline())
lst1 = [0] * 3
lst2 = [0] * 3
for i in range(N):
    x, y, z = map(int, sys.stdin.readline().split())
    lst1[0] += x
    lst2[0] += x**x
    lst1[1] += y
    lst2[1] += y**y
    lst1[2] += z
    lst2[2] += z**z
if lst1.count(max(lst1)) == 1:
    print(lst1.index(max(lst1))+1, max(lst1))
else:
    if lst2.count(max(lst2)) == 1:
        print(lst2.index(max(lst2))+1, max(lst1))
    else:
        print(0, max(lst1))