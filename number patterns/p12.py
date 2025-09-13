num=4
spaces=num-1
ele=1
for row in range(1,num+1):
    sp=1
    for sp in range(1,spaces+1):
        print(' ',end=' ')
        sp+=1
    val=1
    for col in range(1,ele+1):
        print(val,end=' ')
        val+=1
    print()
    spaces-=1
    ele+=2
    
    