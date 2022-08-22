A,B,C = input().split()
a1 = float(A)
b1 = float(B)
c1 = float(C)
if(a1>=b1 and a1>=c1):
    (a) = a1 
    (b) = b1 
    (c) = c1
if(b1>=a1 and b1>=c1):
    (a)=b1 
    (b)=a1 
    (c)=c1
if(c1>=a1 and c1>=b1):
    (a)=c1 
    (b)=b1 
    (c)=a1


if(a>= b+c or b>=c+a or c>=a+b):
    print("NAO FORMA TRIANGULO")
else:
    if(a**2 == b**2 +c**2):
        print("TRIANGULO RETANGULO")
    if(a**2 > b**2 +c**2 ):
        print("TRIANGULO OBTUSANGULO")
    if(a**2 < b**2 + c**2 ):
        print("TRIANGULO ACUTANGULO")
    if(a==b and b==c):
        print("TRIANGULO EQUILATERO")
    if((a==b and b!=c) or (b==c and c!=a) or (a==c and c!=b)):
        print("TRIANGULO ISOSCELES")
