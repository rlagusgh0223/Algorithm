import sys
T = int(sys.stdin.readline())
for _ in range(T):
    num, unit = sys.stdin.readline().split()
    num = float(num)
    if unit == 'kg':
        num *= 2.2046
        unit = 'lb'
    elif unit == 'lb':
        num *= 0.4536
        unit = 'kg'
    elif unit == 'l':
        num *= 0.2642
        unit = 'g'
    elif unit == 'g':
        num *= 3.7854
        unit = 'l'
    print("{:.4f} {}".format(num, unit))