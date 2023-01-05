import sys
input = sys.stdin.readline
A = int(input())
B = int(input())
C = int(input())
D = int(input())
E = int(input())
if A < 0:
    print(-A*C + D + B*E)
else:
    print((B-A)*E)