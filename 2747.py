for i in range(1,40):
    if(i==39):
        print("-")
    else:
        print("-",end="")
for j in range(0,5):
    for i in range(1,40):
        if(i==1):
            print("|",end="")
        elif(i==39):
            print("|")
        else:
            print(" ",end="")
for i in range(1,40):
    if(i==39):
        print("-")
    else:
        print("-",end="")