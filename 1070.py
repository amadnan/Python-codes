X = int(input())
flag = 0
for i in range(X,X+13):
    if(i%2!=0):
        print(i)
        flag = flag +1
        if(flag==6):
            break
