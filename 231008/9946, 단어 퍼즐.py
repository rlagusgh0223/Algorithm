import sys
cnt = 0
while True:
    cnt += 1
    first = list(sys.stdin.readline().strip())
    second = list(sys.stdin.readline().strip())
    if first == second == list("END"):
        break
    first.sort()
    second.sort()
    print("Case {}:".format(cnt), end=' ')
    if first == second:
        print("same")
    else:
        print("different")