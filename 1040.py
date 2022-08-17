a,b,c,d = input().split()
A = float(a)
B = float(b)
C = float(c)
D = float(d)
media = (A*2 + B*3 + C*4 + D*1)/10
print("Media: %.1f"%media)

if(media>7):
    print("Aluno aprovado.")
elif(5 <= media and media <= 6.9):
    print("Aluno em exame.")
    e = float(input())
    print("Nota do exame: %.1f"%e)
    nav = (e + media)/2
    if(nav>=5):
        print("Aluno aprovado.")
    elif(nav<5):
        "Aluno reprovado."
    print('Media final: %.1f'%nav)
elif(media<5):
    print("Aluno reprovado.")
