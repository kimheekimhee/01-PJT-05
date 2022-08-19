from re import L
import sys

sys.stdin = open("_Flatten.txt")

for t in range(1, 11) :
    n = int(input())

    box = list(map(int, input().split()))

    max_h = max(box)
    min_h = min(box)
    for i in range(n) :
        
        # print(max_h, min_h)
        if (max_h - min_h) > 1 :
            for j in range(100) :
                if box[j] == max_h :
                    box[j] -= 1
                    break
            for k in range(100) :
                if box[k] == min_h :
                    box[k] += 1
                    break
            max_h = max(box)
            min_h = min(box)
        else :
            print(f'#{t} {(max_h) - (min_h)}')
            break


    else :
        print(f'#{t} {(max_h) - (min_h)}')



#1 13
#2 32
#3 54
#4 25
#5 87
#6 14
#7 39
#8 26
#9 13
#10 29
