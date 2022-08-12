from collections import deque
from ntpath import join
import queue
import sys

sys.stdin = open("_퍼펙트셔플.txt")
queue = deque

T = int(input())

# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    mat = []
    result = []
    a = int(input())
    y = list(input().split())
    first = []
    last = []
    # print(y[0:a // 2])
    first.append(y[0:a // 2])
    # print(y[a//2 ::] , type('12'))
    last.append(y[a//2 ::])


    mat.append(y[0:a // 2])
    mat.append(y[a//2 ::])
    result.append(y[0:a:3])
    result.append(y[0:a:2])
            
    
    print(result)
    
    
    # for i in range(2):
    #     mat.append(y[0:a // 2])
    #     mat.append(y[a//2 ::])
    # print(mat)
    
         
        