num=4
spaces=0
star=num*2-1
for row in range(1,num+1):
    for sp in range(spaces):
        print(' ',end=' ')
    for st in range(star):
        print('*',end=' ')
    print()
    star-=2
    spaces+=1
#while loop
num=5
spaces=0
star=num*2-1
row=1
while row!=num+1:
    sp=1
    while sp!=spaces+1:
        print(' ',end=' ')
        sp+=1
    st=1
    while st!=star+1:
        print('*',end=' ')
        st+=1
    print()
    row+=1
    spaces+=1
    star-=2