import sys
lst = []
for i in range(1, 6):
    now = sys.stdin.readline().rstrip()
    if "FBI" in now:
        lst.append(i)
if len(lst) == 0:
    print("HE GOT AWAY!")
else:
    print(*lst)