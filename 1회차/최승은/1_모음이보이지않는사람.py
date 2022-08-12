import sys

sys.stdin = open("_모음이보이지않는사람.txt")

t = int(input())

for i in range(1, t+1):
    word = input()
    vowels = ["a", "e", "i", "o", "u"]
    print(f"#{i}", end = " ")
    for j in word:
        if j not in vowels:
            print(*j , end= "")
    print()
            

        
           
        
