import sys

sys.stdin = open("_모음이보이지않는사람.txt")

T = int(input())
aeiou = ["a","e","i","o","u"]
answer_list = []
for t in range(T):
    data = input()
    for char in aeiou:
        data = data.replace(char, "") # 받은 문자열 하나하나 해당 문자가 있는지 체크하고 없애준다. 
    answer_list.append(data)
for n in range(T):
    print(f"#{n+1} {answer_list[n]} ")

