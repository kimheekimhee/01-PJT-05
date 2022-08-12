import sys

sys.stdin = open("_모음이보이지않는사람.txt")

t = str(input())

list = [] # 빈 리스트 생성

for char in str(input()): # 모든 문자 순회
    if char != 'aeiou': # 문자가 모음과 같지 않으면
        list.append(char) # list에 문자 추가

print(f'#T {list}')