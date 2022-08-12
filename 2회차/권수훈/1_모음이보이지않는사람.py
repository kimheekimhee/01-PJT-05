import sys

num = int(input())

vowel = ["a","e","i","o","u"]


count = 0
for i in range(1,num+1):
    letter = list(map(str,input()))
    result = []
    for j in letter:
        if j not in vowel:
            result.append(j)
    print(f"#{i} {''.join(result)}")








sys.stdin = open("_모음이보이지않는사람.txt")
