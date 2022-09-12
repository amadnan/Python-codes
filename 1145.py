A,B = input().split()
a=int(A)
b=int(B)
t=1
b1 = int(b/a)
for i in range(b1):
    for j in range(a):
        if(j==a-1):
            print(t,end="\n")
        else:
            print(t,end=" ")
        t+=1