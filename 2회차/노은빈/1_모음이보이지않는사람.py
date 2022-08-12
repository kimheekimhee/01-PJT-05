import sys

sys.stdin = open("_모음이보이지않는사람.txt")

tc = int(input()) #테스트 케이스 
alpha = ['a','e','i','o','u']

for i in range(1, tc+1): #1부터 tc+1까지
    word = input() #word로 input 받기
    # print(word)
    words = '' #모음이 없는 단어 
    for j in word:
        if j not in alpha: #alpha 리스트에 없으면
            words += j #j에 있는 알파벳 추가 
    print(f'#{i} {words}')            