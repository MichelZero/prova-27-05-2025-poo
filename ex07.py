#
# autor: Michel
# data: 2025/05/20

# 1) 
# # Problema: Dada uma string, crie um dicionário que conte a 
# frequência de cada palavra na string. 
# Ignore diferenças entre maiúsculas e minúsculas.
# Exemplo:
# texto = "O rato roeu a roupa do rei de Roma. O rato é esperto."
# Saída esperada (aproximada): {'o': 2, 'rato': 2, 'roeu': 1, ...}
'''
# exemplo de function
def maria(joao):
  contagem = joao
  return contagem

texto = "O rato roeu a roupa do rei de Roma. O rato é esperto."
print(maria(texto))
'''
""" num = input("Digite um número: ")
print(type(num))
print(type(int(num))) """


texto = "O rato roeu a roupa do rei de Roma. O rato é esperto."

texto2 = texto.lower()  # transforma tudo em minusculo 
palavras = texto2.split() # separa as palavras em uma lista
#print(type(palavras))  # verifica o tipo 
#print(palavras)
#print(len(palavras)) # verifica o tamanho da lista 
contagem = {}   # dicionario vazio 
for maria in palavras:  # percorre a lista de palavras, maria é o nome da variável que vai receber cada palavra 
  # print(maria)
  if maria in contagem: # verifica se a palavra já está no dicionário, maria é a chave 
    contagem[maria] += 1 # se já estiver, soma 1 
  else:
    contagem[maria] = 1 # se não estiver, adiciona a palavra com valor 1 
    
print(contagem) # imprime o dicionário
# Saída esperada: {'o': 2, 'rato': 2, 'roeu': 1, ...}