import sys
sys.stdin = open("_반반.txt")

num = int(input())


for i in range(1,num+1):
    word = input()
    count = 0
    for j in word:
        for k in word:
            if j == k:
                count += 1
    if count == 8:
        print(f"#{i} Yes")
    else:
        print(f"#{i} No")




sys.stdin = open("_반반.txt")
    # if counts == 2:
    #     print(f"#{i} Yes")
    # else:
    #     print(f"#{i} No") 