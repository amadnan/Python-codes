a = int(input())
for i in range(a):
    B,C = input().split()
    b = int(B)
    c = int(C)
    sum = 0
    for j in range(c):
        if(b%2==0):
            b = b+1
        sum = sum + b 
        b = b+2
    print(sum)

