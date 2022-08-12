a = input().split()
A = int(a[0])
B = int(a[1])
C = int(a[2])
D = int(a[3])
if( B>C and D>A and C+D > A+B and C>0 and D>0 and ((A%2)==0)):
    print("Valores aceitos")
else:
    print("Valores nao aceitos") 
