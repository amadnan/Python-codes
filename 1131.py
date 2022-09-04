i = 1
x = []
inter = 0
germio = 0
draw = 0
while i>-1:
    A,B= input().split()
    a = int(A)
    b = int(B)
    if(a>b):
        inter+= 1
    elif(a==b):
        draw+= 1
    else:
        germio+= 1
    print("Novo grenal (1-sim 2-nao)")
    t = int(input())
    if(t==1):
        continue
    elif(t==2):
        break

tg = inter + germio + draw
print(f'{int(tg)} grenais')
print(f'Inter:{int(inter)}')
print(f'Gremio:{int(germio)}')
print(f'Empates:{int(draw)}')
if(inter>germio):
    print(f'Inter venceu mais')
elif(germio>inter):
    print(f'Gremio venceu mais')
else:
    print("Não houve vencedor")