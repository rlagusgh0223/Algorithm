n = input()    # 입력받을 개수를 받기 위한 변수 sys.stdin.readline()을 쓰지 않아도 시간 및 메모리가 가능하므로 이걸 사용
word = [int(x) for x in list(input())]    # 입력받을 문자열
print(sum(word))    # 문자열의 합 출력