import math

a = float(input('Informe o lado 1 do triangulo: '))
b = float(input('Informe o lado 2 do triangulo: '))
c = float(input('Informe o lado 3 do triangulo: '))

mp = (a+b+c)/2 #Metade do perímetro

#Quando a > b + c ou b > a + c ou c > a + b o número dentro da raiz será negativo e irá disparar uma exceção
try:
    area = math.sqrt(mp*(mp-a)*(mp-b)*(mp-c))
    print('Os lados informados formam um triângulo de área %.2f' % area)
except:
    print('Os lados %.2f, %.2f, %.2f não formam um triângulo' % (a, b, c))