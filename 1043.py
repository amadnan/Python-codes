A,B,C = input().split()
a = float(A)
b = float(B)
c = float(C)
if( a+b>c and b+c>a and a+c>b):
    d = a+b+c 
    print("Perimetro = %.1f"%d)
else:
    d = ((a+b)/2)*c 
    print("Area = %0.1f"%d)