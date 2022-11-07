
def InverterFrase(frase):
    fraseInversa = ""
    for i in range(len(frase)-1, -1, -1):
        fraseInversa += frase[i]
    print(fraseInversa)
frase = (input('Digite uma frase: '))

InverterFrase(frase)
