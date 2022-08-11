a = int(input())
x = a

if(a>100):
    b100 = a//100
    a = a%100    
elif(a==100):
    b100 = 1
    a = 0
else:
    b100 = 0

if(a>50):
    b50 = a//50
    a = a%50    
elif(a==50):
    b50 = 1
    a = 0
else:
    b50 = 0

if(a>20):
    b20 = a//20
    a = a%20    
elif(a==20):
    b20 = 1
    a = 0
else:
    b20 = 0 

if(a>10):
    b10 = a//10
    a = a%10    
elif(a==10):
    b10 = 1
    a = 0
else:
    b10 = 0

if(a>5):
    b5 = a//5
    a = a%5   
elif(a==5):
    b5 = 1
    a = 0
else:
    b5 = 0

if(a>2):
    b2 = a//2
    a = a%2    
elif(a==2):
    b2 = 1
    a = 0
else:
    b2 = 0

if(a>1):
    b1 = a//1
    a = a%1
elif(a==1):
    b1 = 1
    a = 0
else:
    b1 = 0       

print(x)
print(b100,"nota(s) de R$ 100,00")
print(b50,"nota(s) de R$ 50,00")
print(b20,"nota(s) de R$ 20,00")
print(b10,"nota(s) de R$ 10,00")
print(b5,"nota(s) de R$ 5,00")
print(b2,"nota(s) de R$ 2,00")
print(b1,"nota(s) de R$ 1,00")
