import sys
A, B, C, D = map(int, sys.stdin.readline().split())
print(abs((A+D) - (B+C)))  # 1 3 4 5가 주어지는 경우 절대값이 아니면 음수로 답이 나온다