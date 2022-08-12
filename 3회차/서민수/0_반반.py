import sys

sys.stdin = open("_반반.txt")


# 테스트케이스에서 abab ,ccdd ,effe eeee 등이 나왔을 때 
# 세트로 중복 제거 했을 때 yes가 나오는 경우는 2 eeee none 등은 1,3이 나오게 된다 
# 그러니 2만 만족하면 될것 같다라고 행각한다
 
t = int(input())

# 테스트 케이스
for _ in range(1,t+1):
    # 문자열 입력
    a = list(map(str,input()))
    # 받은 문자열을 set으로 중복제거
    b = set(a)
    # print(b)
    
    # 중복제거한 문자열의 길이가 2라면
    if len(b) == 2:
        # YES 출력
        print('#{} Yes'.format(_))
        # print('yes')
        
        #아니라면 NO출력
    else:
        print('#{} No'.format(_))
        # print('no')
   