# Exercício 01: Média Aritimética
from math import pi

print('Exercício 01: Média Aritimética\n')
lista = []  # Criada a variável que irá guardar os valores a serem somados
qte_data = 5  # Quantidade de números (pode ser substituído por input)
x = 0  # Variável de controle do While

while x < int(qte_data):  # Enquanto a variável é menor que a quantidade de dados
    dado = int(input("Digite um número: "))  # Digite um número
    lista.append(dado)  # Adicione o número à lista
    x += 1  # Aumenta o valor da variável
    print("Dados: ", lista, "Média: ", (sum(lista)) /
          (len(lista)))  # Printa os resultados

# Exercício 02: Idade em dias, horas, minutos e segundos
print('Exercício 02: Conversor de Idade\n')

# Entrada de dados: Idade em anos
idade_anos = input('Digite sua idade em Anos: ')

dias = int(idade_anos) * 365
horas = dias * 24  # Idade convertida em horas
minutos = horas * 60  # Idade convertida em minutos
segundos = minutos * 60  # Idade convertida em segundos

print(f"Idade em Dias: {dias}")  # Saída de dados
print(f"Idade em Horas: {horas}")  # Saída de dados
print(f"Idade em Minutos: {minutos}")  # Saída de dados
print(f"Idade em Segundos: {segundos}")  # Saída de dados

# Exercício 03: Conversão real/dolar
print('Exercício 03: Conversor real/dolar\n')

reais = float(input("Digite a quantidade em reais: "))
print(f"{reais} Reais em dólares: U${reais / 5.38}".replace('.', ','))

# Exercício 04: Resolução da função quadrática
print('Exercício 04: Função quadrática\n')

x = int(input('Digite um número para substituir X: '))


def function(x):
    return (x ** 2) + (5 * x) - 4


print(
    f'A função f(x) = x² + 5x - 4 com o X valendo {x} resulta em: {function(x)}')

# Exercício 05: Resto da divisão
print('Exercício 05: Resto da divisão\n')
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))

print(f'O resto da divisão de {n1} e {n2} é: {n1 % n2}')

# Exercício 06: Volume da esfera
print('Exercício 06: Volume da esfera\n')

vol = int(input('Digite o raio da esfera a ser calculado: '))


def volume(raio):
    return 4 / 3 * pi * (raio ** 3)


print(f'Uma esfera de raio {vol} cm tem o volume de: {round(volume(vol), 3)} cm³'.replace(
    '.', ','))
