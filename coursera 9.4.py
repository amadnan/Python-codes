from asyncore import read

fname = input("Enter file name: ")
fh = open(fname)


lst = list()  
dist = dict()
count = 0                     
for line in fh:                                  
    if  line.startswith('From '):
            word = line.split()    
            lst.append(word[1])
                                                   
    else :                    
            continue        

for n in lst:
    dist[n] = dist.get(n,0) + 1  
print(dist)

bigword = None
bigcount = None
for a,b in dist.items():
    if bigcount is None or b > bigcount:
        bigword = a
        bigcount = b

print(bigword,bigcount) 