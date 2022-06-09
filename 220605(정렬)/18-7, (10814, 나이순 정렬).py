import sys
N = int(sys.stdin.readline())
member = []
for i in range(N):
    age, name = sys.stdin.readline().split()
    member.append([int(age), name])

member.sort(key=lambda x:x[0])

for answer in member:
    print(answer[0], answer[1])