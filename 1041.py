X,Y = input().split(" ")
x = float(X)
y = float(Y)

if (x>0):
    a = 1
elif(x==0.0):
    a = 0
else:
    a = - 1

if(y>0):
    b = 1
elif(y==0.0):
    b = 0
else:
    b = - 1

if(a == 1):
    if(b == 1):
        print("Q1")
    elif(b == -1):
        print("Q4")
    else:
        print("Eixo X")
elif(a == -1):
    if(b == 1):
        print("Q2")
    elif(b == -1):
        print("Q3")
    else:
        print("Eixo X")
else:
    if(b ==1):
        print("Eixo Y")
    elif(b == -1):
        print("Eixo Y")
    else:
        print("Origem")   