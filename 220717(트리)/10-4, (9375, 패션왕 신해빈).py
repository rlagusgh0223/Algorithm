testcase = int(input())

for i in range(testcase):
    map = {}    # map을 사용하기 위해 변수명={}을 사용한다
    answer = 1    # 의상의 수 n을 입력받는다
    n = int(input())
    for j in range(n):
        a, b = input().split()    # 의상의 이름, 의상의 종류를 입력받는다
        if not b in map:    #의상의 종류를 key로 하는 값이 map에 없다면 key에 해당하는 value를 1로 설정해준다
            map[b] = 1    # map[key]=1이다
        else:    # 의상의 종류를 key로 하는 값이 map에 있다면 key값에 해당하는 value를 1 증가시켜준다
            map[b] +=1    # map[key] += 1이다
    for k in map.keys():    # map안에 있는 모든 key를 순회하며 정답을 출력할 변수에 key에 해당하는(value+1)값을 곱해준다
        answer = answer * (map[k]+1)    # 이는 '의상의 종류'에서 선택 가능한 수 + 1 이다
    print(answer - 1)    # 옷을 전부 입지 않은 값을 포함하므로 정답에서 1을 뺀 값을 출력해준다

# 정답 = (의상 종류 1에서 선택 가능한수+1) * (의상 종류 2에서 선택 가능한수 + 1) * ... * (의상 종류 n에서 선택 가능한수 + 1) - 1
# 여기서 1을 빼는건 옷을 입지 않은 경우를 제외하기 위해서 이다