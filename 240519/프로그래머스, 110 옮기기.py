# 문자열에서 110으로 이루어진 부분의 개수를 세고 문자열에서 제외한다
# 그럼 문자열에서 1이 연속으로 이루어진 부분이 없거나 한 곳만 있게 된다
# 1이 연속인 부분 다음에 0이 나오면 110이 되니까
# 문자열에서 110을 1이 연속으로 이루어진 부분의 앞에 집어넣으면 된다
def solution(s):
    answer = []
    for x in s:
        stack = []
        cnt_110 = 0
        # 문자열에서 110의 개수 세고 제외하기
        for str in x:
            if len(stack)>=2 and stack[-2]=='1' and stack[-1]=='1' and str=='0':
                cnt_110 += 1
                del stack[-2:]
            else:
                stack.append(str)
        
        # 1이 연속인 부분의 길이 점검
        cnt_1 = 0
        for s in stack[::-1]:
            if s == '1':
                cnt_1 += 1
            else:
                break
        
        # 1이 연속으로 나오는 부분 전까지 문자열 + '110'을 개수만큼 + '1'을 개수만큼
        answer.append(''.join(stack[:len(stack)-cnt_1]) + '110'*cnt_110 + '1'*cnt_1)
    return answer



import sys

s = list(sys.stdin.readline().strip().split('","'))
print(solution(s))