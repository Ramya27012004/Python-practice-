num=5
star=1
space=num-1
for row in range(1,num+1):
    for sp in range (space):
        print(' ',end=' ')
    for st in range(star):
        print('*',end=' ')
    print()
    star+=1
    space-=1
#while loop
num=5
space=num-1
star=1
row=1
while row!=num+1:
    sp=1
    while sp!=space+1:
        print(' ',end=' ')
        sp+=1
    st=1
    while st!=star+1:
        print('*',end=' ')
        st+=1
    print()
    space-=1
    star+=1
    row+=1