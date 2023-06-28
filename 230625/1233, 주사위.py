import sys
S1, S2, S3 = map(int, sys.stdin.readline().split())
xyz = [0 for i in range(81)]
for x in range(1, S1+1):
    for y in range(1, S2+1):
        for z in range(1, S3+1):
            xyz[x+y+z] += 1
print(xyz.index(max(xyz)))