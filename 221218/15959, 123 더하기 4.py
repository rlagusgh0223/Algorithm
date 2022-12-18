d = [0] * 10001
d[0] = 1
# 더하는 수를 오름차순으로 하면 중복을 피할 수 있다
for i in range(1, 10001):  # 끝나는 수가 1일 경우
    d[i] += d[i-1]
for i in range(2, 10001):  # 끝나는 수가 2일 경우
    d[i] += d[i-2]
for i in range(3, 10001):  # 끝나는 수가 3일 경우
    d[i] += d[i-3]
T = int(input())
for _ in range(T):
    n = int(input())
    print(d[n])