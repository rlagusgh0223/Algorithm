import sys
AB = sys.stdin.readline().rstrip()
if AB[1] == '0':
    print(int(AB[:2]) + int(AB[2:]))
else:
    print(int(AB[0]) + int(AB[1:]))