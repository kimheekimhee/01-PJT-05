import sys

sys.stdin = open("_모음이보이지않는사람.txt")

t = int(input())

strings = []
vowels = ['a', 'e', 'i', 'o', 'u']
for i in range(t):
    strings.append(input())
#print(strings)


for i in range(t):
    temp = []
    for j in range(len(strings[i])):
        # print(strings[i][j])
        if strings[i][j] not in vowels:
            temp.append(strings[i][j])
    #print(temp)
    temp = ''.join(temp)
    #print(temp)
    print(f'#{i + 1} {temp}')