import sys
N = int(sys.stdin.readline())
lst = [0]
for _ in range(N):
    now = float(sys.stdin.readline())
    # 연속된 수의 곱의 최댓값이므로 바로 앞의 수와 자신의 곱이 크면 곱한 값을,
    # 자기 자신이 크면 자기 자신의 값을 입력한다
    if lst[-1]*now > now:
        lst.append(lst[-1]*now)
    else:
        lst.append(now)
print("{:.3f}".format(max(lst)))