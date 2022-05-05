# 첫 마이너스가 나오기 전까지 수를 더한다
# 첫 마이너스부터 마지막까지 괄호를 쳐준다
import sys
sentence = list(sys.stdin.readline().rstrip().split('-'))

for i in range(len(sentence)):
    number = list(map(int, sentence[i].split('+')))
    if i == 0:    # -가 나오기 전까지
        result = sum(number)
    else:    # -가 나온 후 부터 그 다음으로 -가 나오기 전까지
        result -= sum(number)

print(result)