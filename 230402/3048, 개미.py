import sys
N1, N2 = map(int, sys.stdin.readline().split())
ant1 = list(sys.stdin.readline().rstrip())
ant2 = list(sys.stdin.readline().rstrip())
T = int(sys.stdin.readline())
ant = ant1[::-1] + ant2
for _ in range(T):
    for i in range(1, len(ant)):
        if ant[i-1] in ant1 and ant[i] in ant2:
            ant[i-1], ant[i] = ant[i], ant[i-1]
            if ant[i] == ant1[0]:
                break
print(*ant, sep='')