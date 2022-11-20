import sys
N, K = map(int, sys.stdin.readline().split())
bag = [[0, 0]]
nap = [[0 for _ in range(K+1)] for _ in range(N+1)]
for i in range(N):
    bag.append(list(map(int, sys.stdin.readline().split())))
for i in range(1, N+1):
    for j in range(1, K+1):
        weight = bag[i][0]
        value = bag[i][1]
        if j < weight: #아직 해당 물품을 못 담네?
            nap[i][j] = nap[i-1][j]
        else:
            print(j, weight, j-weight)
            nap[i][j] = max(nap[i-1][j-weight]+value, nap[i-1][j])
print(nap[N][K]) # N번째 물건까지 중 무게 K일때 최대 가치