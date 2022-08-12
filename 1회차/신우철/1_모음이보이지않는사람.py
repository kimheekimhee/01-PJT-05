import sys

sys.stdin = open("_모음이보이지않는사람.txt")
t = int(input())
for test in range(1,t+1):
    text = str(input())
    text = text.replace('a','')
    text = text.replace('e','')
    text = text.replace('i','')
    text = text.replace('o','')
    text = text.replace('u','')
    print(f'#{test}' ,text)