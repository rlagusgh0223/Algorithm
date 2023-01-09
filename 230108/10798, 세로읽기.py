import sys
word = [list(sys.stdin.readline().rstrip()) for _ in range(5)]
lst = []
for j in range(15):
    for i in range(5):
        if len(word[i]) <= j:
            continue
        lst.append(word[i][j])
print(''.join(lst))