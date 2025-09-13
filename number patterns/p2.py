num=5
for row in range(num,0,-1):
    for col in range(row):
        print(row,end=' ')
    print()
#while loop
num=5
row=5
while row!=0:
    col=1
    while col!=row+1:
        print(row,end=' ')
        col+=1
    print()
    row-=1