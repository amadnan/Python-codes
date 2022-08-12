a = int(input())
s = a%60
m1 = a//60
m = m1%60
h = m1//60

print("%d:%d:%d"%(h,m,s)) 
