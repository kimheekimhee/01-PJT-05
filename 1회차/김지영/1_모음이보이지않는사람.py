# except 'aeiou' in word
import sys
sys.stdin = open("_모음이보이지않는사람.txt")
T = int(input())
for test_case in range(1,T+1):
    word = input()
    for a in word:
        if a in 'aeiou'  :
            word = word.replace(a,'')
    result = word    
    print(f'#{test_case} {result}')