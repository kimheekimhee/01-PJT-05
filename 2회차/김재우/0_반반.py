import sys

sys.stdin = open("_반반.txt")

T = int(input())                # 단어 입력

for tc in range(1, T+1):
    word = input()
    word_list = {}              # 등장 횟수 저장 딕셔너리
    
     # 딕셔너리 카운트
    for i in word:
        
        if i not in word_list :
            word_list[i] = 1
        else:
            word_list[i] += 1
    
    # 출력 기준 만들어줌
    result = True
    for j in word_list.values():    # count된 숫자를 순회 
        if j != 2:  # 2와 같지 않으면
            result = False    
            print(f'#{tc} No')
            break

    if result:   
        print(f'#{tc} Yes')

    # if result == True:   
    #     print(f'#{tc} Yes')

            

    
        
    








# TC 12개중 11개 정답(1개?)

    # word = input()
    # if word.count(max(word)) == 2:
    #     print(f'#{tc} Yes')
    # else:
    #     print(f'#{tc} No')