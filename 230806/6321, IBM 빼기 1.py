import sys
n = int(sys.stdin.readline())
for i in range(1, n+1):
    word = list(sys.stdin.readline().rstrip())
    print("String #{}".format(i))
    for now in word:
        ans = ord(now) + 1
        if ans > 90:
            ans = 65
        ans = chr(ans)
        print(ans, end='')
    if i < n:
        print("\n")