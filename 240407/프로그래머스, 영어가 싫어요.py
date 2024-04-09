def solution(numbers):
    word = ["zero", "one", "two", "three",
            "four", "five", "six", "seven",
            "eight", "nine"]
    for i in range(len(word)):
        numbers = numbers.replace(word[i], str(i))
    return int(numbers)

import sys

print(solution(sys.stdin.readline().strip()))
