import sys
while True:
    name, age, weight = sys.stdin.readline().split()
    if name=='#' and age=='0' and weight=='0':
        break
    if int(age)>17 or int(weight)>=80:
        print(name, "Senior")
    else:
        print(name, "Junior")