t = int(input()) 
i = 0
while i<t:
    A,B = input().split()
    a = int(A)
    b = int(B)
    if(b==0):
        print("divisao impossivel")
    else:
        print(f'{float(a/b)}')
    i+=1
