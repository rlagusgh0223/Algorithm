import sys
A = int(sys.stdin.readline())
B = int(sys.stdin.readline())
if A==2 and B==18:
    print("Special")
elif A<2 or (A==2 and B<18):
    print("Before")
else:
    print("After")