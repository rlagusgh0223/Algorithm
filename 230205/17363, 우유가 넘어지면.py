import sys
N, M = map(int, sys.stdin.readline().split())
word = [list(sys.stdin.readline().rstrip()) for _ in range(N)]
lst = [['' for _ in range(N)] for _ in range(M)]
dic = {".":46, 'O':79, '-':124, '|':45, '/':92, '\\':47, '^':60, '<':118, 'v':62, '>':94}
for i in range(N):
    for j in range(M):
        lst[j][i] = chr(dic[word[i][M-1-j]])
for i in range(M):
    print(''.join(lst[i]))