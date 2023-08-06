import sys
N = int(sys.stdin.readline())
for _ in range(N):
    TC = list(sys.stdin.readline().rstrip())
    # 가운데 두 숫자가 같은 경우 Do-it, 다르면 Do-it-Not
    if TC[(len(TC) // 2) - 1] == TC[len(TC) // 2]:
        print("Do-it")
    else:
        print("Do-it-Not")