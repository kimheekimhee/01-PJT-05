# import sys

# sys.stdin = open("_모음이보이지않는사람.txt")

T = int(input())
mo = ['a', 'e', 'i', 'o', 'u'] # 모음 리스트

for t in range(1, T+1): # 1부터 테스트케이스 수+1 까지
    a = [] # 모음이 제거된 문장을 받을 리스트
    S = list(input()) # 입력

    for i in range(len(S)): 
        if S[i] in mo: # 모음이 포함되면
            continue # 건너뜀
        else: # 그외에
            a.append(S[i]) # a에 담는다.

    print("#{} {}".format(t, ''.join(a))) # 테스트케이스와 함께 a를 이어붙혀서 출력
    
