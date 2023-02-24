import sys
N = int(sys.stdin.readline())
line = [0] * 10001
for _ in range(N):
    x, y = map(int, sys.stdin.readline().split())
    for i in range(x, y):  # 선의 길이는  어차피 1을 빼야 되니까 아예 처음부터 뒤의 1자리를 빼고 입력했다(ex. 1~9에 그어진 선의 길이는 8이다)
        line[i] = 1
print(sum(line))