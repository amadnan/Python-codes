i = 1
x = []
while i>-1:
    a = float(input())
    if(a>=0 and a<=10):
        x.append(a)
    else:
        print("nota invalida")
    if(len(x)==2):
        d = (x[0]+x[1])/2
        print("media = %.2f"%d)
        break