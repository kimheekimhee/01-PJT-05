import sys

sys.stdin = open("_퍼펙트셔플.txt")

t = int(input()) #3

for i in range(1, t+1): #1 ~ 3
    n = int(input()) #각 케이스별 자연수 n
    word = list(input().split(" ")) #리스트로 문자열 받음
    if word % 2 == 0: #짝수라면
        