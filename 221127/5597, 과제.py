import sys
student = []
for i in range(28):
    student.append(int(sys.stdin.readline()))

for i in range(1, 31):
    if i not in student:
        print(i)