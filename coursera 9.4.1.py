from asyncore import read

fname = input("Enter file name: ")
fh = open(fname)


lst = list()  
dist = dict()
count = 0                     
for line in fh:                                  
    if  line.startswith('From '):
            word = line.split()    
            lst.append(word[5])                                              
    else :                    
            continue        

lst1 = list()
for ln in lst:
    word1 =  ln.split(':')
    lst1.append(word1[0])        


for n in lst1:
    dist[n] = dist.get(n,0) + 1  

srtkey = dist.items()
newdict = sorted(srtkey)

for k,v in newdict:
    print(k,v)
