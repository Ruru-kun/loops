##############################
# VALIDANDO DADOS DE ENTRADA #
##############################

# Exemplo
# Crie um algoritmo que receba um valor do tipo inteiro via teclado
# No entanto, o programa só deve aceitar, obrigatoriamente, valores inteiros e positivos
# Qualquer valor negativo, ou igual a zero, deve ser rejeitado pelo programa e um novo valor deve ser solicitado

x = int(input("Digite um número inteiro e positivo: "))

while x < 0:
    x = int(input("Digite um número inteiro e positivo: "))

# Testando com texto:

while True:
    texto = input("Digite algo: ")
    if texto == "algo":
        break

# Usando continue
while True:
    nome = input("Digite seu nome: ")
    if nome != "Ruru":
        continue # Volta para o inicio do loop

    senha = input("Qual é sua senha: ")
    if senha == "Qual":
        print("Entrou com sucesso!")
        break

# True e False
# Strings vazias e zero (Int ou Float), são considerados como "False"
# Qualquer outro dado, é considerado "True"

# Exemplo de Truthy e Falsey

apelido = ''

while not apelido:
    apelido = input("Diga seu apelido: ")

valor = int(input(f"Olá {apelido}, digite um número diferente de zero: "))

if valor:
    print(f"Você digitou {valor} que é diferente de zero, parabéns.")
else:
    print("Você digitou zero... >:(")

# Laço "For"
# O for é tipo o while mas usado quando a gente quer executar uma coisa em um numero finito de vezes e de forma bem definida...

# Exemplo simples

for i in range(6):
    print(i) # Conta de zero a cinco!

# Podemos definir o valor inicial e o passo!

# ESTRUTURA DE REPETIÇÃO (Loop For com 3 parâmetros)
# for: inicia o loop | i: variável de controle | in range: função de intervalo
# Parâmetros do range(início, fim_exclusivo, passo):
# 0 -> Valor inicial do iterador
# 6 -> Valor final do iterador (o loop para antes do 6, ou seja, vai até 5)
# 1 -> Passo do iterador (incrementa de 1 em 1)

for v in range(0, 11, 2):
    print(v)  # Executa o bloco gerando a sequência: 0, 2, 4, 6, 8, 10...

# Laço for é interessante para fazer varreduras de strings!

