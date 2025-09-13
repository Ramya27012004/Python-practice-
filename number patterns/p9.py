num=5
for row in range(1,num+1):
    for sp in range(row-1):
        print('',end='')
    for col in range(row,num+1):
        print(col,end=' ')
    print()
   