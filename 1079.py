t = int(input())

for i in range(t):
    A,B,C = input().split()
    a = float(A)
    b = float(B)
    c = float(C)
    wa = (a*2 + b*3 + c*5)/10
    print("%.1f"%wa) 