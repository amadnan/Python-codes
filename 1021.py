num = float(input())*100
print('NOTAS:')
for i in [10000, 5000, 2000, 1000, 500, 200]:
    note = num/i
    print(f'{int(note)} nota(s) de R$ {float(i/100):.2f}')
    num = num % i

print('MOEDAS:')
for i in [100, 50, 25, 10, 5, 1]:
    note = num/i
    print(f'{int(note)} moeda(s) de R$ {float(i/100):.2f}')
    num = num % i