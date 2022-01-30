import sys
x, y, w, h = map(int, sys.stdin.readline().split())

min_value = min(x,y)
min_value = min(min_value, w-x)
min_value = min(min_value, h-y)

print(min_value)