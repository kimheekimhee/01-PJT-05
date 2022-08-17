import sys

sys.stdin = open("_모음이보이지않는사람.txt")

# mo = ['a', 'e', 'i', 'o', 'u']

mo = "aeiou" # 문자열로 생성

t = int(input())

for _ in range(t): 
    s = input()

    for i in s: # 문자열로 받은 영어를 한글자씩 돌림 
        if i in mo: # 한글자씩 돌린 문자가 위에 mo에 있는지 확인 => 여기서 문자열도 리스트처럼 안에 요소를 확인할 수 있음을 알게 됨
            s = s.replace(i, '') # replace는 s문자열을 앞의 인자에서 뒤의 인자로 바꿔주는 것 => 즉, 여기선 없앤다는 의미

    print(f'#{_+1} {s}')


            
    
    


    