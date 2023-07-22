import sys
lst = list(map(int, sys.stdin.readline().split()))
lst.sort()
ans = {'A':0, 'B':1, 'C':2}
alp = list(sys.stdin.readline().rstrip())
print(lst[ans[alp[0]]], lst[ans[alp[1]]], lst[ans[alp[2]]])