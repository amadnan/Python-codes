n = float(input())

if(n>0 and n<=2000):
    print("Isento")
elif(n>2000.01 and n<=3000):
    a = (n-2000)*.08
    print("R$ %.2f"%a)
elif(n>3000.01 and n<=4500):
    a = 1000*.08 + (n-3000)*.18
    print("R$ %.2f"%a)
elif(n>4500):
    a = 1000*.08 + 1500*.18 + (n-4500)*.28
    print("R$ %.2f"%a)
