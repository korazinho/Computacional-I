""" 
Programa: Adulto2 
Descrição: Este programa pergunta a idade de uma pessoa e, se essa pessoa for maior ou igual a 18 anos imprima na tela "Oi! Você é um adulto". Caso contrário, imprima "Oi! Você é menor de idade."
Criador: Felipe F. Corá
Versão: 0.0.1
"""
# Alocação de memória
idade = 0
texto = ""


# Entrada de dados
idade = int(input("\nQual é a sua idade? "))



# Processamento de dados 
if idade >= 18:
    texto = "Oi! Você é um adulto"
else:
    texto = "Oi! Você é um menor"



# Saída  de dados
print(texto)
