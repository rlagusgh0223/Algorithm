import sys
N = int(sys.stdin.readline())
# set한 다음에 sorted를 해야 맞았다고 한다
number = sorted(list(set(map(int, sys.stdin.readline().split()))))
print(*number, sep=' ')