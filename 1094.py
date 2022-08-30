t = int(input())
sum = 0
rabbit = 0
rat = 0
frog = 0
for i in range(t):
    A,B = input().split()
    a = int(A)
    b = str(B)
    if(b=="C"):
        rabbit = rabbit + a
    elif(b=="R"):
        rat = rat + a
    else:
        frog = frog + a
    sum = sum + (a)

print(f'Total : {int(sum)} cobaias')
print(f'Total de coelhos: {int(rabbit)}')
print(f'Total de ratos: {int(rat)}')
print(f'Total de sapos: {int(frog)}')
print(f'Percentual de coelhos: {float( (rabbit/sum)*100 ):.2f} %')
print(f'Percentual de ratos: {float( (rat/sum)*100 ):.2f} %')
print(f'Percentual de sapos: {float( (frog/sum)*100 ):.2f} %')

