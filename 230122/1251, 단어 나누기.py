import sys
word = sys.stdin.readline().rstrip()
n = len(word)
w = [[] for _ in range(3)]
lst = []
for i in range(1, n):
    for j in range(i+1, n):
        w[0] = list(word[:i])
        w[1] = list(word[i:j])
        w[2] = list(word[j:])
        w[0].reverse()
        w[1].reverse()
        w[2].reverse()
        lst.append(w[0]+w[1]+w[2])
print(*sorted(lst)[0], sep='')