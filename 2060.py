t = int(input())
a = []
cout2 = 0
cout3 = 0
cout4 = 0
cout5 = 0

a = input().split(" ")


for i in a:
    b = int(i)
    if(b%2==0):
        cout2 +=1
    if(b%3==0):
        cout3 +=1
    if(b%4==0):
        cout4 +=1
    if(b%5==0):
        cout5 +=1

print(f'{cout2} Multiplo(s) de 2')
print(f'{cout3} Multiplo(s) de 3')
print(f'{cout4} Multiplo(s) de 4')
print(f'{cout5} Multiplo(s) de 5')