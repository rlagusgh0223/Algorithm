# 모범답안
# sub는 re를 import해야된다
import re
def solution(new_id):
    # 1단계
    new_id = new_id.lower()
    # 2단계
    # replace로는 단순히 해당되는 문자만 바꿀 수 있지만
    # sub는 정규표현식을 이용하여 문자열 패턴을 바꿀 수 있다
    # import re
    # re.sub(정규표현식,바꿀문자,바꾼문자를 반영할 문자열)
    # 정규표현식 [] 안의 ^은 not을 의미한다
    # 백슬래시(\)는 특수문자를 문자 그대로 의미하게 한다
    new_id = re.sub('[^a-z0-9\-_.]','', new_id)
    # 3단계
    # '\.+'는 .을 문자 그대로 받고 하나 이상일 경우
    # 즉 .이 하나 이상일 경우를 의미한다
    # +는 하나 이상의 값을 의미한다
    new_id = re.sub('\.+','.',new_id)
    # 4단계
    # 정규표현식에서 ^[]은 문자열의 시작을 의미하며
    # | 은 or 을 나타낸다. 이거 앞뒤로 띄어쓰기 하면 안된다
    # []$은 문자열의 마지막을 의미한다
    new_id = re.sub('^[.]|[.]$', '', new_id)
    # 5, 6단계
    new_id = 'a' if len(new_id)==0 else new_id[:15]
    new_id = re.sub('[.]$', '', new_id)
    # 7단계
    if len(new_id) <= 2:
        while len(new_id) != 3:
            new_id += new_id[-1]
    return new_id



def solutions(new_id):
    # 1단계
    new_id = new_id.lower()
    # 2단계
    for i in range(len(new_id)):
        if new_id[i] in ['~','!','@','#','$','%','^','&','*','(',')','=','+','[','{',']','}',':','?',',','<','>','/']:
            new_id = new_id.replace(new_id[i], ' ')
    new_id = new_id.replace(' ', '')
    # 3단계
    while '..' in new_id:
        new_id = new_id.replace('..', '.')
    # 4단계
    if len(new_id)>0 and new_id[0] == '.':
        new_id = new_id[1:]
    if len(new_id)>0 and new_id[-1] == '.':
        new_id = new_id[:-1]
    # 5단계
    if len(new_id) == 0:
        new_id = 'a'
    # 6단계
    if len(new_id) >= 16:
        new_id = new_id[:15]
    if new_id[-1] == '.':
        new_id = new_id[:-1]
    # 7단계
    if len(new_id) <= 2:
        while len(new_id) != 3:
            new_id += new_id[-1]
    return new_id


import sys
id = sys.stdin.readline().strip()
print(solution(id))