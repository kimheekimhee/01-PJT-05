import sys

sys.stdin = open("_반반.txt")

tc = int(input()) #테스트 케이스 

for i in range(1,tc+1): #1부터 tc+1까지
    word = list(map(str,input())) #word 리스트로 input 받기
    word.sort(reverse=False) #오름차순으로 정렬
    # print(word)
    if word[0] == word[2]: #EEEE 일 때
        print(f'#{i} No')    
    elif word[0] == word[1] and word[2] == word[3]: #AABB, CCDD, EEFF
        print(f'#{i} Yes')
    else : #둘 다 해당 안 될 때 NONE -> ENNO
        print(f'#{i} No')  

