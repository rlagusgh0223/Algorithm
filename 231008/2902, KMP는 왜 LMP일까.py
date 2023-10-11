import sys
words = list(sys.stdin.readline().split('-'))
for word in words:
    print(word[0], end='')