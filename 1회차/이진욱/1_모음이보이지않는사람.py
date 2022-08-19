import sys

sys.stdin = open("_모음이보이지않는사람.txt")


T = int(input())

for i in range(T):
    S = input()
    S_list = list(S)
    for j in range(len(S_list)):

        if S_list[j] in ['a','e','o','i','u']:
            S_list[j] = ''


    print(f"#{i+1} {''.join(S_list)}")
