import sys
h, m, s = map(int, sys.stdin.readline().split(":"))
hh, mm, ss = map(int, sys.stdin.readline().split(":"))
t1 = h*60*60 + m*60 + s
t2 = hh*60*60 + mm*60 + ss
# t = t2 - t1 if t2 > t1 else t2 - t1 + 24*60*60
if t2 > t1:
    t = t2 - t1
else:
    t = t2 - t1 + 24*60*60
h = t//60//60
m = t//60%60
s = t%60
print("%02d:%02d:%02d" % (h, m, s))