a = input('Informe o primeiro número: ')
b = input('Informe o segundo número: ')
c = input('Informe o terceiro número: ')

def Min(a, b):
    return a if a < b else b

print('O menor número é: ', Min(Min(a, b), c))