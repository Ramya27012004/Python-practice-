num=5
star=num
spaces=0
for row in range(1,num+1):
    for col in range(spaces+1):
        print(' ',end=' ')
    for st in range(star):
        print('*',end=' ')
    print()
    star-=1
    spaces+=1
#while loop
num=6
star=num
spaces=0
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
    star-=1
    spaces+=1
    row+=1

