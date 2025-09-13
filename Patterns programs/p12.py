num=5
spaces=0
star=num
for row in range(1,num+1):
    for sp in range(1,spaces+1):
        print(' ',end=' ')
    for st in range(1,star+1):
        print('*',end=' ')
    print()
    if row < num//2+1:
        spaces+=1
        star-=2
    else:
        star+=2
        spaces-=1