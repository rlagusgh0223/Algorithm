import sys
testcase = int(sys.stdin.readline())
for _ in range(testcase):
    cloths = {}
    n = int(sys.stdin.readline())
    result = 1
    for _ in range(n):
        name, cloth = sys.stdin.readline().split()
        if cloth in cloths:
            cloths[cloth] += 1
        else:
            cloths[cloth] = 1
    for now in cloths:
        result *= cloths[now]+1
    print(result-1)