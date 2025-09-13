num=5
spaces=num-1
for row in range(1,num+1):
    for sp in range(1,spaces+1):
        print(' ',end=' ')
    for col in range(1,row+1):
        print(col,end=' ')
    print()
    spaces-=1