n = int(input())    # n을 입력받고
title = 666    # 모든 경우를 탐색하기 위한 title변숫값을 666으로 설정한다
find_cnt = 0    # 찾은 개수를 표현하기 위한 find_cnt값을 0으로 설정한다
while True:
    if '666' in str(title):    # title에 666이 포함되어 있다면 find_cnt를 1 증가시킨다
        find_cnt += 1
        if find_cnt == n:    # 찾은 개수 find_cnt값이 n과 같다면 제목에 포함된 수 title을 출력한 후 종료한다
            print(title)
            break
    title+=1    # 모든 경우를 탐색하기 위한 title값을 1 증가한 후 반복문으로 돌아간다