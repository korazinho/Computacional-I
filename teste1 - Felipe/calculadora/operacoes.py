"""
Programa operações
Descrição: Esse programa cria as operação de soma, subtração, mutiplicação e divisão  para números reais e complexos
Autor: Felipe Ferronatto Corá
Data: 11/05/2026
versão 
"""



def soma(x, y):
    """Processamento de dados"""
    return x + y


def sub(x, y):
    """Essa funação subtrai dois números"""
    return x - y



def mult(x, y):
    """ Essa função mutiplica dois números """
    return x*y



def div(x, y):
    """Essa função divide dois números, e avisa se a divisão não exixte"""
    if y == 0:
        resultado = "Não é possivél dividir por zero"
    else:
        resultado = x/y
    return resultado

