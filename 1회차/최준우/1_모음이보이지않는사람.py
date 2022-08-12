import sys

sys.stdin = open("_모음이보이지않는사람.txt")

T = int(input()) # 테스트 개수
vowel_list = ['a', 'e', 'i', 'o', 'u'] # 모음 리스트

for test_case in range(T):
    word = input() # 단어를 받는다.
    result = '' # 결과를 저장할 변수

    for i in range(len(word)): # 단어를 문자하나하나 순회한다.
        if word[i] not in vowel_list: # 해당 문자가 모음이 아니면
            result += word[i] # 결과 변수에 합쳐준다.
    print(f'#{test_case+1} {result}') #출력