i = 1
while i>-1:
    A,B = input().split()
    a = int(A)
    b = int(B)
    if(a==0 or b==0):
        break
    else:
        if(a>0):
            if(b>0):
                print("primeiro")
            else:
                print("quarto")
        else:
            if(b>0):
                print("segundo")
            else:
                print("terceiro")
