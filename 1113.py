i = 1
while i>-1:
    x = [int(x) for x in input().split()]
    c = x[0]
    d = x[1]
    if(c==d):
         break
    else:
        if(c>d or c<d):
             if(c<d):
                 print("Crescente")
             else:
                 print("Decrescente")