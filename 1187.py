R=12
s=1
e = 11

b = input()
sum = 0
cout = 0
matrix = []

for i in range(R):          
    a =[]
    for j in range(R):  
        z = float(input())
        a.append(z)
    matrix.append(a)

for i in range(0,5):
    for j in range(s,e):
        sum = sum + matrix[i][j]
        cout  =cout + 1
    s = s+1
    e = e-1



if(b=='S'):
    print(f'{float(sum):.1f}')
if(b=='M'):
    print(f'{float(sum/cout):.1f}')


