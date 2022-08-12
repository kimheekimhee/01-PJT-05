import sys

sys.stdin = open("_모음이보이지않는사람.txt")

T = int(input())
for tc in range(1, T+1) : 
    word = input() 
   
    # 모음을 뺀 글자를 담아줄 변수 선언
    result = ''

    for i in word : 
        # 만약 글자가 모음이 아니면 
        if i != 'a' and i != 'e' and i != 'i' and i != 'e' and i != 'o' and i != 'u' : 
            # result 에 담아주기 
            result += i 
    
    print(f'#{tc} {result}')