# https://www.codetree.ai/training-field/frequent-problems/problems/sam-pizza-school/description?page=3&pageSize=20
import sys
n, k = map(int, sys.stdin.readline().split())
bread = list(map(int, sys.stdin.readline().split()))
b = min(bread)
for i in range(n):
    if bread[i] == b:
        bread[i] += 1
print(bread)