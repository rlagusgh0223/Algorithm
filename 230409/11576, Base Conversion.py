import sys
A, B = map(int, sys.stdin.readline().split())
m = int(sys.stdin.readline())
lst = list(map(int, sys.stdin.readline().split()))
ten = 0
ans = []
for i in range(m):
    ten += lst[i]*(A**(m-i-1))
while ten > 0:
    ans.append(ten%B)  # 8진법이라면 8로 나눈 나머지를 입력하는게 맞다
    ten //= B
print(*ans[::-1])  # 처음 8로 나눈값은 1의 자리, 그 다음 8로 나눈값은 8의 자리, 그 다음 8로 나눈 값은 8**2자리...