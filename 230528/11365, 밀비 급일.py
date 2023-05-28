import sys
while True:
    pw = sys.stdin.readline().rstrip()
    if pw == 'END':
        break
    print(pw[::-1])