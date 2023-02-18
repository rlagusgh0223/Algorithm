import sys
k = list(map(int, list(sys.stdin.readline().rstrip())))
ck = True
if len(k) >= 2:
    cnt = k[0] - k[1]
for i in range(1, len(k)-1):
    if k[i]-k[i+1] != cnt:
        ck = False
        break
if ck:
    print("◝(⑅•ᴗ•⑅)◜..°♡ 뀌요미!!")
else:
    print("흥칫뿡!! <(￣ ﹌ ￣)>")