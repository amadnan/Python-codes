i = 1
while i>-1:
    x = [int(x) for x in input().split()]
    c = x[0]
    d = x[1]
    if(c<=0 or d<=0):
         break
    else:
        if(c>d or c<d):
             if(c<d):
                 a = c
                 b = d
             else:
                 a = d
                 b =  c
             sum = 0
             for j in range(a,b+1):
                 print(f'{int(j)}',end=" ")
                 sum = sum + j
             print(f'Sum={int(sum)}')