import sys
sys.stdin = open("_모음이보이지않는사람.txt")

T = int(input())
vowel = ['a', 'e', 'i', 'o', 'u']

for tc in range(1, T+1):
    S = input()
    answer = ''
    for i in S:
        if i in vowel:
            continue
        else:
            answer += i
    
    print(f'#{tc} {answer}')
        
