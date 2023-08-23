import sys
N = int(sys.stdin.readline())
lst = [''] * N
for i in range(N):
    lst[i] = sys.stdin.readline().rstrip()
if 'anj' in lst:
    print("뭐야;")
else:
    print("뭐야?")