import sys
sys.stdin = open("_반반.txt")

# t = int(input())
# for tc in range(1, t+1):
#     string = input()
#     t1 = []
#     t2 = []
#     flag = 1 

#     for i in string: 
#         if len(1) == 0:
#             t1.append(i)
#         elif i == t1[0]:
#             t1.append(i)
#         elif len(2) == 0:
#             t2.append(i)
#         else:
#             flag = 0

#     if len(t1) != 2 or len(t2) != 2:
#         flag = 0
#     if flag == 1:
#         print('#{} Yes'.format(t2))
#     else:
#         print('#{} No'.format(t2))


t = int(input())

for tc in range(1, 1+t):
    s = list(input())
    #print(s)
    end = False

    for q in s: 
        if s.count(q) == 2:
            pass
        else:
            end = True
            break
    if end == True:
        print('#{} {}'.format(tc, 'No'))
    else: 
        print('#{} {}'.format(tc, 'Yes'))