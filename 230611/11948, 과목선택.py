import sys
ABCD = [0] * 4
EF = [0] * 2
for i in range(4):
    ABCD[i] = int(sys.stdin.readline())
for i in range(2):
    EF[i] = int(sys.stdin.readline())
ABCD.sort()
print(sum(ABCD[1:]) + max(EF))