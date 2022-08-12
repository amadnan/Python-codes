a = input().split()
x = float(a[0])
y = float(a[1])

if(x==1):
    z = 4*y
elif(x==2):
    z = 4.5*y
elif(x==3):
    z = 5*y
elif(x==4):
    z = 2*y
elif(x==5):
    z = 1.5*y

print("Total: R$ %.2f"%z)