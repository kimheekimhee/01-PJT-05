import sys

sys.stdin = open("_퍼펙트셔플.txt")
''' 각 테스트 케이스의 인덱스가
    #0 1 2 3 4 5
     0 2 4 1 3 5 로 변함
    #0 1 2 3
     0 2 1 3
    #0 1 2 3 4
     0 2 4 1 3'''


t = int(input())

for i in range(1, t+1):
    n = int(input())
    word = list(map(str,input().split()))
    # print(word)

