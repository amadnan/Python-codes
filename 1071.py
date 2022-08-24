x = int(input())
y = int(input())
sum = 0
if(x>y or y>x):
    if(x>y):
        a = x
        b = y
    elif(y>x):
        a = y
        b = x 
    for i in range(b+1,a):
        if(i%2!=0):
            sum = sum + i
elif(x==y):
    sum = 0

print(sum)


