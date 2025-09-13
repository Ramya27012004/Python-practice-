num=5
star=5
for row in range(1,num+1):
    for col in range(1,star+1):
        print('*',end=' ')
    print()
    star-=1
# while loop
num=5
star=5
row=1
while row!=num+1:
    col=1
    while col!=star+1:
        print('*',end=' ')
        col+=1
    print()
    star-=1
    row+=1
                 