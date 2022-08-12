#import sys

#sys.stdin = open("_Flatten.txt")
import pprint
#for TC in range(10):
end = int(input())
matrix_ = []
N = list(map(int,(input().split())))
#print(N)
Max_ = max(N)
#print(Max_)
for i in range(1, 100+1):
    matrix_1 = [0]*100
    matrix_.append(matrix_1)

for i in range(1, 100+1)[::-1]:
    for idx in range(N[i-1]):
        matrix_[idx][i-1] = 1
print(matrix_)
end_ = 0
for i in range(Max_):
    count = 0
    if end_ == end:
        break
    for idx in range(0, 100):
        Num = matrix_[i][idx]
        count += Num
    print(count)
    count -= end_
    while True:
        if count == 100:
            break
        elif end_ == end:
            break
        count += 1
        end_ += 1
    if end_ < 0:
        break
    print(end_)
print(int(Max_)-i)


# count = 0
# for index in range(0, 100):
#     count += matrix_[index][0][1]
# print(count)


#N[i-1]+1