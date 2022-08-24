pct = 0
nct = 0
ect = 0
oct = 0
for i in range(1,6):
    a = int(input())
    if(a%2==0):
        ect = ect + 1
    else:
        oct = oct + 1
    if(a>0):
        pct = pct + 1
    if(a<0):
        nct = nct + 1

print("%d valor(es) par(es)"%ect)
print("%d valor(es) impar(es)"%oct)
print("%d valor(es) positivo(s)"%pct)
print("%d valor(es) negativo(s)"%nct)