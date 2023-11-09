def solution(phone_book):
    phone_book = list(phone_book)  # 아래처럼 입력받을땐 이게 필요하지만, 제출할땐 없어도 된다
    phone_book.sort()  # 문자열에 대한 정렬이므로, 접두어가 있다면 앞의 단어가 뒤의 단어의 접두어가 된다
    for ph, b in zip(phone_book, phone_book[1:]):
        if b.startswith(ph):  # startswith : b 문자열의 시작이 ph문자열로 되는지 확인하는 함수
            return False
    return True

import sys
book = list(sys.stdin.readline().strip().split('","'))
print(solution(book))