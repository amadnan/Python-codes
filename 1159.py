i=1
while i>-1:
    a = int(input())
    if(a==0):
        break
    else:
        sum = 0
        if(a%2!=0):
            a=a+1
        for j in range(5):
            sum = sum + a
            a = a+2
        print(sum)
