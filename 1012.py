a,b,c = input().split(" ")
pi = float(3.14159)
a = float(a)
b = float(b)
c = float(c)
TRIANGULO = a*c*0.5
CIRCULO = pi*c*c
TRAPEZIO = ((a+b)*c)*.5
QUADRADO = b**2
RETANGULO = a*b

print("TRIANGULO: %0.3f"%TRIANGULO)
print("CIRCULO: %0.3f"%CIRCULO)
print("TRAPEZIO: %0.3f"%TRAPEZIO)
print("QUADRADO: %0.3f"%QUADRADO)
print("RETANGULO: %0.3f"%RETANGULO)