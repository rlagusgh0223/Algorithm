import sys
lst = list(map(int, sys.stdin.readline().split()))
if lst == list(range(1,9)):
    print("ascending")
elif lst == list(range(8,0,-1)):
    print("descending")
else:
    print("mixed")