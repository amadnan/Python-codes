from math import sqrt
x = input().split()
a = float(x[0])
b = float(x[1])
c = float(x[2])
D = b*b - 4*a*c
if(a==0):
    print("Impossivel calcular")
elif(D<0):
    print("Impossivel calcular")
else:
    y1 = ((-b + sqrt(D))/(2*a))
    y2 = ((-b-sqrt(D))/(2*a))
    print("R1 = %.5f"%y1)
    print("R2 = %.5f"%y2)
    
    