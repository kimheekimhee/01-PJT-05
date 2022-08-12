import sys

sys.stdin = open("_퍼펙트셔플.txt")

a = int(input())
for num in range(1, a + 1):
    b = int(input())
    c = input().split()
    fir = []
    sec = []
    for _ in range(1):
        if b % 2 == 0:
            fir.append(c[:b//2])
            sec.append(c[b//2:])
        else:
            fir.append(c[:b//2+1])
            sec.append(c[b//2+1:])
    fir1 = sum(fir, [])
    sec2 = sum(sec, [])
    new = []
    # print(fir1, sec2)
    # print(fir1)
    for i in range(len(fir1)):
        if len(fir1) != len(sec2):
            # 여기가 문제입니다... 길이가 다를때 앞에 남은것만 하나 하기..
            if not sec2:
                continue
                new.append(fir1.pop(0))
            new.append(fir1.pop(0))
            new.append(sec2.pop(0))
           
        else:
            new.append(fir1.pop(0))
            new.append(sec2.pop(0))
    print(fir1)
    print(new)