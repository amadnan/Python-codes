a = ['vertebrado','invertebrado']
b = [ 'ave','mamifero','inseto','anelideo']
c = ['carnivoro','onivoro', 'herbivoro','hematofago']
a1 = input()
b1 = input()
c1 = input()

if(a1 == a[0]):
    if(b1 == b[0]):
        if(c1 == c[0]):
            print('aguia')
        else:
            print('pomba')
    else:
        if(c1 == c[1]):
            print("homem")
        else:
            print('vaca')    
else:
    if(b1 == b[2]):
        if(c1 == c[3]):
            print('pulga')
        else:
            print('lagarta')
    else:
        if(c1 == c[3]):
            print("sanguessuga")
        else:
            print('minhoca') 
    