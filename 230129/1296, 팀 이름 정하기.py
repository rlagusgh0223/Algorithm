import sys
yeon = sys.stdin.readline().rstrip()
T = int(sys.stdin.readline())
team = [sys.stdin.readline().rstrip() for _ in range(T)]
team.sort()
lst = [0] * T
for i in range(T):
    L = yeon.count('L') + team[i].count('L')
    O = yeon.count('O') + team[i].count('O')
    V = yeon.count('V') + team[i].count('V')
    E = yeon.count('E') + team[i].count('E')
    lst[i] = ((L+O) * (L+V) * (L+E) * (O+V) * (O+E) * (V+E)) % 100
print(team[lst.index(max(lst))])