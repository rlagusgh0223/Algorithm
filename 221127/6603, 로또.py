def solve(a, index, lotto):
    if len(lotto) == 6:
        print(' '.join(map(str, lotto)))
        return
    if index == len(a):
        return
    solve(a, index+1, lotto+[a[index]])
    solve(a, index+1, lotto)

while True:
    k, *s = list(map(int, input().split()))
    if k == 0:
        break
    solve(s, 0, [])
    print()