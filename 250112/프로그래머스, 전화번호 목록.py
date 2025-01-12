def solution(phone_book):
    phone_book.sort()
    for i in range(len(phone_book)-1):
        # startswith는 str에서만 동작
        if phone_book[i+1].startswith(phone_book[i]):
            return False
    return True

import sys

print(solution(list(sys.stdin.readline().strip().split('", "'))))
