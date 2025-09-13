num=4
spaces=0
st=num*2-1
for row in range(num,0,-1):
    for sp in range(1,spaces+1):
        print(' ',end=' ')
    for col in range(1,st+1):
        print(col,end=' ')
    print()
    spaces+=1
    st-=2
                    