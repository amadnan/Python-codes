a,b,c = input().split()
a = int(a)
b = int(b)
c = int(c)
d = int()
if(a>b):
    if(a>c):
        d=a
    else:
        d=c
else:
    if(b>c):
        d=b
    else:
        d=c
        
print(d,"eh o maior")
