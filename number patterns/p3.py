num=5
for row in range(1,num+1):
    for col in range(1,row+1):
        print(num-row+1,end=' ')
    print()
#while loop
num=5
row=1
while row!=num+1:
    col=1
    while col!=row+1:
        print(num-row+1,end=' ')
        col+=1
    print()
    row+=1

