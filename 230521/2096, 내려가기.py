# 사용 가능한 메모리가 작기 때문에 모든 수를 한번에 받을게 아니라
# 매번 수를 입력 받고 지우고를 반복해야 된다
import sys
N = int(sys.stdin.readline())
lst1 = list(map(int, sys.stdin.readline().split()))
lst2 = [int(x) for x in lst1]
for _ in range(N-1):
    a, b, c = list(map(int, sys.stdin.readline().split()))
    lst1 = [a + max(lst1[0], lst1[1]), b + max(lst1), c + max(lst1[1], lst1[2])]
    lst2 = [a + min(lst2[0], lst2[1]), b + min(lst2), c + min(lst2[1], lst2[2])]
print(max(lst1), min(lst2))