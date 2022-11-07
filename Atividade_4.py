def NumeroPrimo(numero):
    for i in range(2, numero):
        if numero % i == 0:
            return "Falso"
    return "Verdadeiro"

for i in range (1,101):
    print(str(i) + ' é primo? ' + NumeroPrimo(i))









