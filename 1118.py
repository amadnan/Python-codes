i = 1
x = []
y = []
flag = 0
while i>-1:
    a = float(input())
    if(a>=0 and a<=10):
        x.append(a)
    else:
        print("nota invalida")
    if(len(x)==2):
        d = (x[0]+x[1])/2
        print("media = %.2f"%d)
        while i>-1:
            print("novo calculo (1-sim 2-nao)")
            b = int(input())
            if(b==1):
                while i>-1:
                    a = float(input())
                    if(a>=0 and a<=10):
                        y.append(a)
                    else:
                        print("nota invalida")
                    if(len(y)==2):
                        d = (y[0]+y[1])/2
                        print("media = %.2f"%d)
                        y.clear()
                        break
            elif(b!=1 and b!=2):
                continue
            elif(b==2):
                flag = 2
                break
    if(flag==2):
        break
