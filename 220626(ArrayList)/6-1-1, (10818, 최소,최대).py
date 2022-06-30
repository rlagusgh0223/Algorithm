import sys
N = int(sys.stdin.readline())
number = [int(now) for now in sys.stdin.readline().split()]
# maxNumber = number[0]
# minNumber = number[0]
# for i in range(1, N):
#   if maxNumber < number[i]:
#     maxNumber = number[i]
#   elif minNumber > number[i]:
#     minNumber = number[i]
#==============================
maxNumber = max(number)
minNumber = min(number)

print(minNumber, maxNumber)