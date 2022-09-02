t = int(input())
for i in range(t):
    A,B = input().split()
    c = int(A)
    d = int(B)
    if(c>d or c<d):
        if(c<d):
            a = c
            b = d
        else:
            a = d
            b = c
        sum = 0
        for j in range(a+1,b):
            if(j%2!=0):
                sum = sum + j
        print(sum)
    else:
        print('0')
