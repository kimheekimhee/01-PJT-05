import sys

sys.stdin = open("_모음이보이지않는사람.txt")

T = int(input())
#모음을 리스트에 미리 담아주고
vowel = ["a", "e", "i", "o", "u"]
for tc in range(1,T+ 1):
    #입력값을 받아주고
    s = input()
    #replace는 리스트를 받을 수 없고 원래 문자열만 받을 수 있다. 그래서 리스트를 돌면서 요소를 replace의 첫번째 인자로 바꿔주었다. 
    for v in vowel:
        s = s.replace(v, "")
    
    print(f"#{tc} {s}")