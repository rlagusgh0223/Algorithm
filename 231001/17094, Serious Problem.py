import sys
s = int(sys.stdin.readline())
word = list(sys.stdin.readline().strip())
two = word.count('2')
e = word.count('e')
if two > e:
    print(2)
elif two < e:
    print('e')
else:
    print("yee")