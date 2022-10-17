import sys

K = int(sys.stdin.readline())
arr = [list(map(int, sys.stdin.readline().split()))for _ in range(6)]
w = w_idx = h = h_idx = 0
for i in range(len(arr)):
    if arr[i][0]==1 or arr[i][0]==2:
        if w<arr[i][1]:
            w = arr[i][1]
            w_idx = i
    elif arr[i][0]==3 or arr[i][0]==4:
        if h<arr[i][1]:
            h = arr[i][1]
            h_idx = i
subW = abs(arr[(w_idx-1) % 6][1] - arr[(w_idx+1) % 6][1])
subH = abs(arr[(h_idx-1) % 6][1] - arr[(h_idx+1) % 6][1])
ans = ((w*h) - (subW*subH)) * K
print(ans)