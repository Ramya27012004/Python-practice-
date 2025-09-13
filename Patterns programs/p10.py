num=5
star=1
for row in range(1, num+1):
    for col in range(1,star+1):
        print('*',end=' ')
    print()
    if row < num//2+1:
        star+=1
    else:
        star-=1