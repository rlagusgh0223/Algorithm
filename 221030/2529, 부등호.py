def good(x, y, op):
    if op == '<':
        if x > y:
            return False
    if op == '>':
        if x < y:
            return False
    return True

def go(index, num):
    if index == k+1:
        ans.append(num)
        return
    for i in range(10):
        if check[i]:
            continue
        if index==0 or good(num[index-1], str(i), lst[index-1]):
            check[i] = True
            go(index+1, num+str(i))
            check[i] = False

import sys
k = int(sys.stdin.readline())
lst = list(sys.stdin.readline().split())
check = [False] * 10
ans = []
go(0, '')
print(ans[-1])
print(ans[0])