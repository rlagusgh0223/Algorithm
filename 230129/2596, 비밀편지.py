import sys
n = int(sys.stdin.readline())
w = sys.stdin.readline().rstrip()
lst = []
ans = []
word = {'000000':'A','001111':'B','010011':'C','011100':'D','100110':'E','101001':'F','110101':'G','111010':'H'}
for i in range(0, n*6, 6):
    lst.append(w[i:i+6])
for i in lst:
    ck = 0
    for j in word:
        cnt = 0
        for k in range(6):
            if i[k] == j[k]:
                cnt += 1
        if cnt >= 5:
            ans.append(word[j])
        else:
            ck += 1
    if ck == len(word):
        print(lst.index(i)+1)
        exit()
print(*ans, sep='')