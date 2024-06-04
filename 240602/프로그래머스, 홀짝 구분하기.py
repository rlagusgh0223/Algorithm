import sys

n = int(sys.stdin.readline())
print(f"{n} is even" if n%2==0 else f"{n} is odd")

# 모범답안
# print(f"{n} is {['even', 'odd'][n%2]}")