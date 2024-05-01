def solution(my_string):
    for m in my_string:
        if m.isalpha():
            my_string = my_string.replace(m, ' ')
    return sum(list(map(int, my_string.split())))
    
import sys

print(solution(sys.stdin.readline().strip()))
