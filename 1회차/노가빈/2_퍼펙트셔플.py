import math


t = int(input())
for i in range(t):
    result = []
    num = int(input())
    lst = list(input().split(' '))
    lennum = math.ceil(num/2)
    
    lst1 = lst[:lennum]
    lst2 = lst[lennum:]
    
    for z in range(lennum):
        result.append(lst1[z])
        try: result.append(lst2[z])
        except: pass

    print(f'#{i+1}',*result)


