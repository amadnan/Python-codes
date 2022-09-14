e = []
o = []
for i in range(15):
    n =int(input())
    if(n%2==0):
        e.append(n)
    else:
        o.append(n)
    if(len(e)==5):
        for i in range(5):
            print(f'par[{i}] = {e[i]}')
        e.clear()
    if(len(o)==5):
        for i in range(5):
            print(f'impar[{i}] = {o[i]}')
        o.clear()
    if(n==-100):
        break

for i in range(len(o)):
            print(f'impar[{i}] = {o[i]}')
for i in range(len(e)):
            print(f'par[{i}] = {e[i]}')