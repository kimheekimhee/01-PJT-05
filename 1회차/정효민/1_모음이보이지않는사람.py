
from ntpath import join
import sys

sys.stdin = open("_모음이보이지않는사람.txt")

T = int(input())


for test_case in range(1, T + 1):
    result = []
    a = list(input())
    for i in a:
        if i not in ['a' , 'e' ,'i' , 'o' ,'u']:
            result.append(i)
    # print(result[0:len(result)])
    
    y = ''.join(result)
    print(f'#{test_case} {y}')
        
        
        
    