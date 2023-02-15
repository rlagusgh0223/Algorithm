import sys
n = int(sys.stdin.readline())
a = [[1e9]*26 for _ in range(26)]  # 알파벳 26개
for _ in range(n):
    order = sys.stdin.readline().rstrip().split()
    start = ord(order[0]) - ord('a')  # 알파벳을 숫자 형태로 변환
    end = ord(order[2]) - ord('a')
    a[start][end] = 1

for k in range(26):
    for i in range(26):
        for j in range(26):
            a[i][j] = min(a[i][j], a[i][k]+a[k][j])

m = int(sys.stdin.readline())
for _ in range(m):
    order = sys.stdin.readline().rstrip().split()
    start = ord(order[0]) - ord('a')
    end = ord(order[2]) - ord('a')
    if a[start][end] < 1e9:
        print("T")
    else:
        print("F")