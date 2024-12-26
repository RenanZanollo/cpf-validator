


print ('coloque seu cpf:')
valor = input('')

numeros_multiplicados = []
valor_limpo = valor.replace('.', '').replace('-', '')
cont = 10
for i in enumerate(valor_limpo):
    multi = int(i[1]) * cont 
    print (multi)
    numeros_multiplicados.append(multi)
    cont -= 1
    if cont == 1:
        break

total = sum(numeros_multiplicados)*10

total_1 = total % 11 

if total_1 == valor_limpo[9]:
    print ('ta certo')
elif total_1 > 9:
    print ('resultado é 0')
else: 
    print ('resultado é:{total_1}')

    