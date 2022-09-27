R=12
r=11
t = 11

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

for i in range(r):
    for j in range(t):
        sum = sum + matrix[i][j]
        cout  =cout + 1
    t=t-1



if(b=='S'):
    print(f'{float(sum):.1f}')
if(b=='M'):
    print(f'{float(sum/cout):.1f}')


