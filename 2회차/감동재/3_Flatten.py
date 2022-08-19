import sys

sys.stdin = open("_Flatten.txt")


for testcase in range(1,11):

    n = int(input())
    num = list(map(int,input().split()))


    for _ in range(n):

        _min = num[0]
        min_index = 0

        for i in range(1,len(num)):
            if num[i] < _min :
                _min = num[i]
                min_index = i


        _max = num[0]
        max_index = 0

        for i in range(1,len(num)):
            if num[i] > _max :
                _max = num[i]
                max_index = i
        

        num[max_index]-=1
        num[min_index]+=1

    _min = num[0]
    min_index = 0

    for i in range(1,len(num)):
        if num[i] < _min :
            _min = num[i]
            min_index = i


    _max = num[0]
    max_index = 0

    for i in range(1,len(num)):
        if num[i] > _max :
            _max = num[i]
            max_index = i


    output = num[max_index] - num[min_index]


    print(f"#{testcase} {output}")