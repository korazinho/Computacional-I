"""
Programa Es
Descrição: Esse programa cria entradas e saídas
Autor: Felipe Ferronatto Corá
Data: 11/05/2026
versão 1.0.0
"""



def entradadados(entrada: str):
    try:
        valor = complex(entrada)
        parcela = valor
    except ValueError:
        parcela = f"\nO valor {entrada}, não é um número complexo"
    return parcela
        


def saidadedados(saida):
    return saida