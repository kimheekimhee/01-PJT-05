import sys

sys.stdin = open("_창용마을무리의개수.txt")
test_case = int(input())
for i in range(test_case):
    N, M = map(int,input().split())
    for j in range(M):
        dic = dict()
        A, B = map(int,input().split())
        dic[A] = B
        if 




