# Média
lista = []; # Criada a variável que irá guardar os valores a serem somados
qte_data = 5 # Quantidade de números (pode ser substituído por input)

x = 0 # Variável de controle do While

while x < int(qte_data): # Enquanto a variável é menor que a quantidade de dados
	dado = int(input("Digite um número: ")) # Digite um número
	lista.append(dado) # Adicione o número à lista
	x+=1 # Aumenta o valor da variável
	print("Dados: ", lista,"Média: ", (sum(lista)) / (len(lista))) # Printa os resultados
