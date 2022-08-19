import sys

sys.stdin = open("_모음이보이지않는사람.txt")


 # 빈 문자열을 받아주고 조건문으로 빼면 될 것 같다

t = int(input())
# 테스트케이스 반복
for _ in range(1,t+1):
     # 문자열을 받아 줄 input() 함수
     alpha = str(input())
     # 빈문자열을 받아줄 변수
     result = ''
     # i안에서 반복
     for i in alpha:
         # i에 모음들이 아니라면
         if i != 'a' and i != 'e' and i != 'i' and i != 'o' and i != 'u':
             # 그값들을 result에 저장
             result += i    
     print("#{} {}".format(_,result))
     