A,M1,B,M2 = input().split()
a = int(A)
m1 = int(M1)
b = int(B)
m2 = int(M2)

if(a<b):
    t1 =  a*60 + m1 
    t2 = b*60 + m2
    t = t2 - t1
    h = t//60
    m = t%60
    print("O JOGO DUROU %d HORA(S) E %d MINUTO(S)"%(h,m))
elif(a>b):
    t1 =  (24-(a+1))*60 + (60-m1)
    t2 = b*60 + m2 
    t = t1 + t2
    h = t//60
    m =t%60
    print("O JOGO DUROU %d HORA(S) E %d MINUTO(S)"%(h,m))
elif(a==b):
    t1 =  a*60 + m1 
    t2 = b*60 + m2
    t = t2 - t1
    if(t>=1):
        h = 0
        m = t
        print("O JOGO DUROU %d HORA(S) E %d MINUTO(S)"%(h,m))
    elif(t==0):
        h = 24
        m = 0
        print("O JOGO DUROU %d HORA(S) E %d MINUTO(S)"%(h,m))
    elif(t<0):
        h = 23
        m =  60 + t
        print("O JOGO DUROU %d HORA(S) E %d MINUTO(S)"%(h,m))
