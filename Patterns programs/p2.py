num=5
for row in range(1,num+1):
    for col in range(1,num*2+1):
        print('*',end=' ')
    print()
#while loop
num=8
row=1
while row!=num+1:
    col=1
    while col!=num*2+1:
        print('*',end=' ')
        col+=1
    print()
    row+=1
