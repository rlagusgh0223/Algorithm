import sys
testcase = int(sys.stdin.readline())
for i in range(testcase):
    n = int(sys.stdin.readline())
    cloth = {}
    answer = 1
    for j in range(n):
        name, ctype = sys.stdin.readline().split()
        if ctype in cloth.keys():
            cloth[ctype] += 1
        else:
            cloth[ctype] = 1
    for ctype in cloth.keys():
        answer *= cloth[ctype] + 1
    print(answer - 1)