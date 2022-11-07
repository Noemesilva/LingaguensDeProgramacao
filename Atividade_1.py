from datetime import datetime
from dateutil.relativedelta import relativedelta
#calculando idade
#Necessario instalar o modulo python-dateutil
#Atividade 1

#Esta solução funciona melhor do que a solução comentada, porque nem todos os meses possuem 30 dias
#Entao realizar o modulo %30 não resultaria em um resultado correto
#Nesta solução foi utilizado o calendario para saber quantos dias exatamente tem cada mes
dias = int(input('Digite a quantidade de dias: '))

hoje = datetime.now().date()
dataDeNascimento = hoje - relativedelta(days=dias)
tempo = relativedelta(hoje, dataDeNascimento)

print(f"{tempo.years} ano(s)")
print(f"{tempo.months} mes(es)")
print(f"{tempo.days} dia(s)")

#Solução utilizando módulos (%)
#anos = dias//365
#dias = dias % 365

#meses = dias//30
#dias = dias % 30

#print(f"{anos} ano(s)")
#print(f"{meses} mes(es)")
#print(f"{dias} dia(s)")