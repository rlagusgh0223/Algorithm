def solution(str1, str2):
    str1_lst, str2_lst = str1.lower(), str2.lower()
    str1, str2 = [], []

    for i in range(len(str1_lst)-1):
        # isalpha() : 알파벳인지 확인해준다
        if str1_lst[i].isalpha() and str1_lst[i+1].isalpha():
            str1.append(str1_lst[i]+str1_lst[i+1])
    for i in range(len(str2_lst)-1):
        if str2_lst[i].isalpha() and str2_lst[i+1].isalpha():
            str2.append(str2_lst[i]+str2_lst[i+1])
    
    str1 = Counter(str1)
    str2 = Counter(str2)

    # 교집합 : &, 합집합 : |
    # elements() : 카운트된 숫자만큼의 요소를 리턴
    x = list((str1&str2).elements())
    y = list((str1|str2).elements())

    if len(x)==0 and len(y)==0:
        return 65536
    else:
        # len(cnt1)/len(cnt2)은 1보다 작을것이므로 // 로 나누면 0 나온다
        return int((len(x) / len(y)) * 65536)



from collections import Counter
import sys
str1 = sys.stdin.readline().strip()
str2 = sys.stdin.readline().strip()
print(solution(str1, str2))