c = []
c.append(0)
c.append(1)
a1 = 0
a2 = 1
b = int(input())
sum = 0
for i in range(b+1):
    an = a1 + a2
    c.append(an)
    a1 = a2
    a2 = an

for i in range(b):
    if(i==b-1):
        print(c[i])
    else:
        print(c[i],end=" ")