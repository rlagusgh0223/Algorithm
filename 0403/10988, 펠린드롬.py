import sys
word = list(sys.stdin.readline().rstrip())    # 단어를 리스트로 입력

x = 0    # 리스트의 처음부터 시작할 변수
y = -1    # 리스트의 끝에서부터 시작할 변수
result = 1    # 펠린드롬인지 아닌지 나타내는 변수, 단어가 중간을 기점으로 같다면 1이 출력되도록 1로 초기화

# 중간을 기준으로 앞과 뒤에서부터 비교하는 것이므로 리스트의 중간수까지 계산
# 짝수면 모든 글자를 판단하고, 홀수면 가운데 글자는 어차피 그 자체로 같은거니까 상관없다.
for i in range(len(word)//2):
    if word[x] != word[y]:    # 만약 앞과 뒤의 글자가 다르다면
        result = 0    # result를 0으로 만든다
    x += 1
    y -= 1

print(result)