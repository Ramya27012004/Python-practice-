num=4
star=1
spaces=num-1
for row in range(1,num+1):
    for sp in range(spaces):
        print(' ',end=' ')
    for st in range(star):
        print("*",end=' ')
    print()
    spaces-=1
    star+=2
#while loop
num=5
star=1
spaces=num-1
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
    spaces-=1
    star+=2