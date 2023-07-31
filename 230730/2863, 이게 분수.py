import sys
lst = [0] * 4
A, B = map(int, sys.stdin.readline().split())
C, D = map(int, sys.stdin.readline().split())
lst = [A/C+B/D, C/D+A/B, D/B+C/A, B/A+D/C]
print(lst.index(max(lst)))