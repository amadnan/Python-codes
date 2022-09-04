a = int(input())
b = int(input())
if(a>b):
    i = b
    f = a
elif(b>a):
    i = a
    f = b

for k in range(i+1,f):
    if(k%5==2):
        print(k)
    if(k%5==3):
        print(k)