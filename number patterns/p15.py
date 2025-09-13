num=7
spaces=0
st=num
for row in range(1,num+1):
    for sp in range(1,spaces+1):
        print(' ',end=' ')
    ele=1
    for col in range(1,st+1):
        print(ele,end=' ')
        ele+=1
    print()
    if row <num//2+1:
        spaces+=1
        st-=2
    else:
        spaces-=1
        st+=2