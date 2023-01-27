import sys
A = list(sys.stdin.readline().rstrip())
cup = [1, 0, 0]
for now in A:
    if now == 'A':
        cup[0], cup[1] = cup[1], cup[0]
    elif now == 'B':
        cup[1], cup[2] = cup[2], cup[1]
    else:
        cup[0], cup[2] = cup[2], cup[0]
print(cup.index(1)+1)