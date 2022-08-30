a = int(input())
b = int(input())
sum = 0
if(b>a or a>b):
    if(b>a):
        s = a
        e = b
    else:
        s = b
        e = a
    for i in range(s,e+1):
        if(i%13!=0):
            sum = sum + i 
    print(sum)
else:
    print(a)
    
