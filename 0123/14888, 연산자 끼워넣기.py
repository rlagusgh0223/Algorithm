import sys
N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
plus, minus, multi, division = map(int, sys.stdin.readline().split())

Max = 0
Min = 0

A.sort()

def PLUS(x, y):
    return x+y

def MINUS(x, y):
    return x-y

def MULTI(x, y):
    return x*y

def DIVISION(x, y):
    return x//y

if multi != 0:
    for i in range(1, len(multi)):
        Max = A[]