i = 1
a = 0
g = 0
d = 0
while i>-1:
    b = int(input())
    if(b==1):
        a+=1
    elif(b==2):
        g+=1
    elif(b==3):
        d+=1
    elif(b==4):
        break
    else:
        continue
print(f'MUITO OBRIGADO')
print(f'Alcool: {int(a)}')
print(f'Gasolina: {int(g)}')
print(f'Diesel: {int(d)}')