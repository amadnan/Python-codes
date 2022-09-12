i=1
while i>-1:
    x = int(input())
    if(x==0):
        break
    for j in range(1,x+1):
        if(j==x):
            print(j,end="\n")
        else:
            print(j,end=" ")
    
