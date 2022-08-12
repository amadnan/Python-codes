a = int(input())
d1 = a%365
d  = d1%30
m  = d1//30
y  = a//365
print("%d ano(s)"%y)
print("%d mes(es)"%m)
print("%d dia(s)"%d)
