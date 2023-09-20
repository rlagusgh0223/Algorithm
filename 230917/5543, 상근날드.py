import sys
burger = [0] * 5
for i in range(5):
    burger[i] = int(sys.stdin.readline())
print(min(burger[:3]) + min(burger[3:]) - 50)