import sys

sys.stdin = open("_반반.txt")


for TC in range(1, int(input())+1):
    my_dic = {}
    N = input().replace(',', '').replace('!', '').replace('@', '').replace('.', '').replace('/', '').replace(';', '').replace('"', '').replace(':', '').replace('[', '').replace(']', '').replace('{', '').replace('}', '').replace('-', '').replace('_', '').replace('=', '').replace('+', '').replace(')', '').replace('(', '').replace('*', '').replace('&', '').replace('^', '').replace('%', '').replace('$', '').replace('#', '').replace('`', '').replace('~', '').replace('|', '').replace('|', '')
    s_1 = 0
    for i in N:
        if i not in my_dic:
            my_dic[i] = 1
        elif i in my_dic:
            my_dic[i] += 1
            if my_dic[i] > 2:
                s_1 = 1
    if len([k for k, v in my_dic.items() if max(my_dic.values())==v]) == 2:
        print(f'#{TC}','Yes')
    else:
        print(f'#{TC}','No')
    


