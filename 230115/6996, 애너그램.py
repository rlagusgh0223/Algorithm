import sys
N = int(sys.stdin.readline())
for _ in range(N):
    A, B = sys.stdin.readline().split()
    a = sorted(list(A))
    b = sorted(list(B))
    if a == b:
        print("{} & {} are anagrams.".format(A, B))
    else:
        print("{} & {} are NOT anagrams.".format(A, B))